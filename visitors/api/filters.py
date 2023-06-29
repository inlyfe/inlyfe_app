import django_filters
from visitors.models import Visitor

class VisitorFilter(django_filters.FilterSet):
    class Meta:
        model = Transaction
        fields = {
            'vendor__name' : ['icontains'],
            'timestamp' : ['lt', 'gt']
        }