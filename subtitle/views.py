from subtitle.models import Subtitles

from subtitle.serializer import (
    SubtitlesSerializer,
    SubtitlesCreateUpdateSerializer
)

from rest_framework import generics

from rest_framework.permissions import (
    AllowAny,
)

class ListSubtitles(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Subtitles.objects.all()
    serializer_class = SubtitlesSerializer

class CreateSubtitles(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Subtitles.objects.all()
    serializer_class = SubtitlesCreateUpdateSerializer

class ListDetailSubtitles(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Subtitles.objects.all()
    serializer_class = SubtitlesSerializer
    lookup_field = 'id'

class UpdateSubtitlesAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Subtitles.objects.all()
    serializer_class = SubtitlesCreateUpdateSerializer
    lookup_field = 'code'
