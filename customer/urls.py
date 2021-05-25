from django.urls import path

from .views import CustomerAPIView, CustomersAPIView, FavoritesAPIView, FavoriteAPIView

urlpatterns = [
	path('customers/', CustomersAPIView.as_view(), name='customers'),
	path('customers/<int:pk>/', CustomerAPIView.as_view(), name='customer'),
	path('favorites/', FavoritesAPIView.as_view(), name='favorites'),
	path('favorites/<int:pk>/', FavoriteAPIView.as_view(), name='favorite'),
]