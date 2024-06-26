from django.shortcuts import render
from .models import Product , Variant

#Product(title, description, created_at, updated_at)
#Variant(title, created_at, updated_at, available_for_sale, price)

# Create your views here.
def Product_dict(request):
    products_list = Product.objects.all()
    return render(request , 'myapp/products_list.html' , {'products_list' : products_list})

def Variant_dict(request):
    variants_list = Variant.objects.all()
    return render(request, 'myapp/variants_list.html', {'variants_list': variants_list})

def home(request):
    return render(request,'myapp/home.html')