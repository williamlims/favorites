import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Customer, FavoriteList
from .serializers import CustomerSerializer, FavoriteListSerializer

class CustomersAPIView(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	
class FavoritesAPIView(APIView):
    def post(self, request):
        code = request.data['product_id']
        link = 'http://challenge-api.luizalabs.com/api/product/'
        api_link = str(link) + str(code) + "/"
        confirmation = requests.get(api_link)
        if confirmation.status_code == 200:
            serializer = FavoriteListSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('This product does not exist!')

    def get(self, request):
        favorites = FavoriteList.objects.all()
        serializer = FavoriteListSerializer(favorites, many=True)
        return Response(serializer.data)

class FavoriteAPIView(APIView):
    def get(self, request, pk):
        favorite = FavoriteList.objects.filter(id=pk)
        serializer = FavoriteListSerializer(favorite, many=True)
        return Response(serializer.data)