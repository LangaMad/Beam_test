from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Profile, Product, Order
from .serializers import UserSerializer, ProfileSerializer, ProductSerializer, OrderSerializer
from django.views.generic import TemplateView
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class IndexView(TemplateView):
    template_name = 'index.html'



