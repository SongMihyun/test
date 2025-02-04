from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from accommodations.models import Accommodation
from pages.serializers.main_serializer import MainPageSerializer


# /api/v1/ui/main/
class MainListView(ListAPIView):
    serializer_class = MainPageSerializer
    permission_classes = (AllowAny,)
    queryset = Accommodation.objects.all().order_by("?")
