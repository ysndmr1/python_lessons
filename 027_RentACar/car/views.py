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

        # tarihe göre filtreleme
        # https://localhost/api/car?from=2023-01-20&to=2023-01-25
        start = self.request.query_params.get("from", None)
        end = self.request.query_params.get("to", None)

        if start and end:
            #     not_available_car_ids = Reservation.objects.filter(
            #         start_date__gte=start, start_date__lte=end
            #     ).values_list("car_id", flat=True)

            #     queryset=queryset.exclude(id__in=not_available_car_ids)
            # AND ve OR kullanmak için Q parametresini kullabiliriz:
            from django.db.models import Q

            not_available_car_ids = Reservation.objects.filter(
                Q(start_date__gte=start)
                and Q(start_date__lte=end)
                or Q(end_date__gte=start)
                and Q(end_date__lte=end)
            ).values_list("car_id", flat=True)

            queryset = queryset.exclude(id__in=not_available_car_ids)

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
