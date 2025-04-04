from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_index, name='index'),
    path('catalog', views.model_catalog, name='catalog'),
    path('<int:pk>/', views.model_show, name='show'),
    path('new/', views.model_new, name='new'),
    path('<int:pk>/edit', views.model_edit, name='edit'),
    path('<int:pk>/delete', views.model_delete, name='delete'),
]