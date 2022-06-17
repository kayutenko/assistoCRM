from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('ocrm/', include('ocrm.urls')),
    path('admin/', admin.site.urls),
]