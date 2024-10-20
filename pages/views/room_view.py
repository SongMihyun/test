from rest_framework.generics import RetrieveAPIView

from pages.serializers.room_serializer import RoomSerializer
from rooms.models import Room


class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
