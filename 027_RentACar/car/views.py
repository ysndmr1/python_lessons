from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Car,
    CarSerializer,
    Reservation,
    ReservationSerializer,
)


# ---------------------------------
# FixView
# ---------------------------------
class FixView(ModelViewSet):
    pass


# ---------------------------------
# CarView
# ---------------------------------
from .permissions import IsStaffOrReadOnly


class CarView(FixView):
    queryset = Car.objects.filter(availability=True)
    serializer_class = CarSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Car.objects.all()
        else:
            queryset = super().get_queryset()

        return queryset


# ---------------------------------
# ReservationView
# ---------------------------------
from .permissions import IsStaffOrOnlyOwnerObjects


class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsStaffOrOnlyOwnerObjects]

    def get_queryset(self):
        if self.request.user.is_staff:
            return (
                super().get_queryset()
            )  # Eğer user.is_staff ise default veriyi göster.
        else:
            return Reservation.objects.filter(
                user=self.request.user
            )  # Sadece kendi objelerini görsün.
