from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', RedirectView.as_view(url='libros/', permanent=False)),
    path('', include('biblioteca.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
