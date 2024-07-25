from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("comment/", include('application.comment.urls')),
    path("dish/", include('application.dish.urls')),
    path("restaurant/", include('application.restaurant.urls')),
    path("user/", include('application.user.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
