from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Variant, Collection, Categories
from .serializers import ProductSerializer, VariantSerializer, CollectionSerializer, CategoriesSerializer, UserSerializer
from .permissions import IsStaffOrReadOnly
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def list_collections(request):
    if request.method == 'GET':
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated, IsStaffOrReadOnly])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_products_by_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    products = collection.product_set.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_variants_by_collection(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    variants = Variant.objects.filter(product__collection=collection)
    serializer = VariantSerializer(variants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_variants_by_categories(request, category_id):
    category = get_object_or_404(Categories, pk=category_id)
    variants = Variant.objects.filter(product__category=category)
    serializer = VariantSerializer(variants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
