from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.home),
    path('hotellist/', views.gethotels),
    path('hotellist/<int:id>/', views.get_hotel_by_id),
    path('reservation/', views.create_reservation)
]