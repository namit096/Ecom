from django.contrib import admin
from .models import Product , Variant , Image , Collection , Categories

# Register your models here.
#Product(title, description, created_at, updated_at)
#Variant(title, created_at, updated_at, available_for_sale, price)
#Image(source, alt_text, updated_at)
#Collection(title, published, updated_at)
#Categories/subcategories (title, created_at, updated_at)

admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(Image)
admin.site.register(Collection)
admin.site.register(Categories)
