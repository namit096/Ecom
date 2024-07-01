from django.shortcuts import render
from .models import Product , Variant

#Product(title, description, created_at, updated_at)
#Variant(title, created_at, updated_at, available_for_sale, price)

def list_collections(request):
    collections = Collection.objects.values('title', 'published', 'updated_at')
    collections_list = list(collections)
    return JsonResponse(collections_list, safe=False)

def list_products_by_collection(request, collection_id):
    collection = get_object_or_404(Collection.objects.prefetch_related('product_set__images'), id=collection_id)
    products = collection.product_set.all().values('id', 'title', 'description', 'created_at', 
                                                   'updated_at', 'images__source', 'images__alt_text')
    products_dict = {}
    for product in products:
        product_id = product['id']
        if product_id not in products_dict:
            products_dict[product_id] = {
                'id': product['id'],
                'title': product['title'],
                'description': product['description'],
                'created_at': product['created_at'],
                'updated_at': product['updated_at'],
                'images': []
            }
        products_dict[product_id]['images'].append({
            'source': product['images__source'],
            'alt_text': product['images__alt_text']
        })

    products_list = list(products_dict.values())
    return render(request, 'myapp/home.html', {'products_list': products_list})

def list_variants_by_collection(request, collection_id):
    collection = get_object_or_404(Collection.objects.prefetch_related('product_set__variants__image'), id=collection_id)
    variants = Variant.objects.filter(product__collection=collection).values(
        'title', 'created_at', 'updated_at', 'available_for_sale', 'price', 'image__source', 'image__alt_text', 'product__title'
    )

    variants_list = [
        {
            'title': f"{variant['product__title']} - {variant['title']}",
            'created_at': variant['created_at'],
            'updated_at': variant['updated_at'],
            'available_for_sale': variant['available_for_sale'],
            'price': variant['price'],
            'image': {'source': variant['image__source'], 'alt_text': variant['image__alt_text']}
        }
        for variant in variants
    ]
    return render(request, 'myapp/home.html', {'variants_list': variants_list})

def list_variants_by_categories(request, category_id):
    category = get_object_or_404(Collection.objects.prefetch_related('product_set__variants__image'), id=category_id)
    variants = Variant.objects.filter(product__collection=category).values(
        'title', 'created_at', 'updated_at', 'available_for_sale', 'price', 'image__source', 'image__alt_text', 'product__title'
    )

    variants_list = [
        {
            'title': f"{variant['product__title']} - {variant['title']}",
            'created_at': variant['created_at'],
            'updated_at': variant['updated_at'],
            'available_for_sale': variant['available_for_sale'],
            'price': variant['price'],
            'image': {'source': variant['image__source'], 'alt_text': variant['image__alt_text']}
        }
        for variant in variants
    ]
    return JsonResponse(variants_list, safe=False)


# Create your views here.
def Product_dict(request):
    products_list = Product.objects.all()
    return render(request , 'myapp/products_list.html' , {'products_list' : products_list})

def Variant_dict(request):
    variants_list = Variant.objects.all()
    return render(request, 'myapp/variants_list.html', {'variants_list': variants_list})

def home(request):
    return render(request,'myapp/home.html')
