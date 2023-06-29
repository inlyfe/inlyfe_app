from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.api.routers')),
    path('dashboards/', include('dashboard.api.urls')),
    path('console/', include('dashboard.view_based.urls')),
    path('Ticket/', include('ticket_services.api.routers')),
    path('', include('visitors.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

