from django.shortcuts import render
from .models import ShoppingList, ShoppingItem
from django.contrib.auth.models import User
from .serializers import UserSerializer, ShoppingListSerializer, ShoppingItemSerializer
from rest_framework import viewsets, serializers
from rest_framework import generics
from django.http import Http404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView

from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for User management
    """
    queryset = User.objects.all().order_by('-username')
    serializer_class = UserSerializer


class ShoppingListAPIView(APIView):
    def get_object(self, pk):
        try:
            # pylint: disable=no-member
            return ShoppingList.objects.get(pk=pk)
        except ShoppingList.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        if request.user:
            request.data['owner'] = request.user.pk
        serializer = ShoppingListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            saved_list = serializer.save()
        return Response({'saved':saved_list})
        
    def get(self, request, format=None):
        if request.user:
            # pylint: disable=no-member
            shoppingLists = ShoppingList.objects.filter(owner=request.user)
            serializer = ShoppingListSerializer(shoppingLists, many=True)
            return Response(serializer.data)

    def patch(self, request, format=None):
        # pylint: disable=no-member
        shoppingList = ShoppingList.objects.filter(list_name=request.data['list_name'])[0]
        serializer = ShoppingListSerializer(shoppingList, data=request.data, partial=True)
        serializer.overall_budget = request.data['overall_budget']
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'modified'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppingListItemsInstanceAPIView(APIView):
    def get_object(self, pk):
        try:
            # pylint: disable=no-member
            return ShoppingList.objects.get(pk=pk)
        except ShoppingList.DoesNotExist:
            raise Http404
    def getShoppingItems(self, list_ref):
        # pylint: disable=no-member
        return ShoppingItem.objects.filter(list_ref=list_ref)

    def editOveralBudjet(self, id):
        # pylint: disable=no-member
        items = ShoppingItem.objects.all()
        shoppingList = ShoppingList.objects.get(pk=id)
        overall_budjet = sum(item.price for item in items)
        shoppingList.overall_budget = overall_budjet
        shoppingList.save()
        return overall_budjet

    def get(self, request, id, format=None):
        # pylint: disable=no-member
        selectedShoppingList = ShoppingListSerializer(ShoppingList.objects.get(pk=id), many=False)
        serializer = ShoppingItemSerializer(self.getShoppingItems(id), many=True)
        return Response({'shopping list':selectedShoppingList.data, 'shopping items':serializer.data})

    def post(self, request, id):
        request.data['list_ref'] = id
        serializer = ShoppingItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'saved': serializer.data, 'new overall budjet':self.editOveralBudjet(id)})

    def patch(self, request, id, format="None"):
        # pylint: disable=no-member
        print(request.data)
        shoppingItem = ShoppingItem.objects.get(pk=request.data['item_id'])
        serializer = ShoppingItemSerializer(shoppingItem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Patch success', 'new overall budjet':self.editOveralBudjet(id)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
