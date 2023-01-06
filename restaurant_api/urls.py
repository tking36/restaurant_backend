from django.urls import path
from . import views

urlpatterns = [
    path('api/restaurants', views.RestaurantList.as_view(), name='restaurant_list'), # api/restaurants will be routed to the ContactList view for handling
    path('api/restaurants/<int:pk>', views.RestaurantDetail.as_view(), name='restaurant_detail'), # api/restaurants will be routed to the RestaurantDetail view for handling
]