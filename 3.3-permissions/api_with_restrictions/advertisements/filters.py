from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, CharFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateTimeFromToRangeFilter()
    status = CharFilter()
    creator = CharFilter()

    class Meta:
        model = Advertisement
        fields = ["created_at", "status", "creator"]