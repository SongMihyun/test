from rest_framework.generics import RetrieveAPIView

from bookings.models import Booking
from pages.serializers.booking_status_serializer import BookingStatusSerializer


class BookingStatusView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingStatusSerializer
