from django.urls import path
from . import views

app_name = 'biblioteca'
urlpatterns = [
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/crear/', views.AutorCreateView.as_view(), name='autor_create'),
    path('autores/<slug:slug>/', views.AutorDetailView.as_view(), name='autor_detail'),
    path('autores/<slug:slug>/editar/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<slug:slug>/eliminar/', views.AutorDeleteView.as_view(), name='autor_delete'),
    
    path('libros/', views.LibroListView.as_view(), name='libro_list'),
    path('libros/crear/', views.LibroCreateView.as_view(), name='libro_create'),
    path('libros/<slug:slug>/', views.LibroDetailView.as_view(), name='libro_detail'),
    path('libros/<slug:slug>/editar/', views.LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<slug:slug>/eliminar/', views.LibroDeleteView.as_view(), name='libro_delete'),
    
    path('prestamos/', views.PrestamoListView.as_view(), name='prestamo_list'),
    path('prestamos/crear/', views.PrestamoCreateView.as_view(), name='prestamo_create'),
    path('prestamos/<int:pk>/', views.PrestamoDetailView.as_view(), name='prestamo_detail'),
    path('prestamos/<int:pk>/editar/', views.PrestamoUpdateView.as_view(), name='prestamo_update'),
    path('prestamos/<int:pk>/eliminar/', views.PrestamoDeleteView.as_view(), name='prestamo_delete'),
    
]