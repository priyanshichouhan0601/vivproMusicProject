from rest_framework import viewsets, status # type: ignore
from rest_framework.decorators import action # type: ignore
from rest_framework.response import Response # type: ignore
from .models import Song
from .serializers import SongSerializer, SongRatingSerializer
from music.service import SongService

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        mode = self.request.query_params.get('mode', None)
        service = SongService()
        if title:
            return service.get_songs_by_title(title)
        if mode:
            return service.get_songs_by_mode(mode)
        return service.get_all_songs()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        if not serializer.data:
            return Response({'detail': 'No data available.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        title = self.request.query_params.get('title', None)
        if title:
            songs = Song.objects.filter(title__icontains=title)
            serializer = self.get_serializer(songs, many=True)
            if not serializer.data:
                return Response({'detail': 'Song not found.'}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=['get', 'patch'], url_path='rate')
    def rate_song(self, request, pk=None):
        song = self.get_object()

        if request.method == 'GET':
            return Response({'rating': song.rating}, status=status.HTTP_200_OK)

        serializer = SongRatingSerializer(data=request.data)
        if serializer.is_valid():
            rating = serializer.validated_data.get('rating')
            if 0 <= rating <= 5:
                song.rating = rating
                song.save()
                return Response({'status': 'rating set', 'rating': rating}, status=status.HTTP_200_OK)
            return Response({"error": "Rating must be between 0 and 5."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
