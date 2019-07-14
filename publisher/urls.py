from django.urls import path
from . import views

app_name = 'publisher'

urlpatterns = [
    path('<int:pk>/', views.PublisherDetailView.as_view(), name='detail'),
]