from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotel/search/', hotel_search, name='hotel_search'),
    path('', main, name='index'),  # Asosiy sahifa sifatida universitetlar ro'yxati
    path('hotel/', MainListView.as_view(), name='rooms'),
    path('hotel/hotel-details/', InfoListView.as_view(), name='rooms-single'),
    path('hotel/search/hotel-details/', InfoListView.as_view(), name='rooms-single'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
