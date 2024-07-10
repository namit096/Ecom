from django.db import models

#Product(title, description, created_at, updated_at)
#Variant(title, created_at, updated_at, available_for_sale, price)
#Image(source, alt_text, updated_at)
#Collection(title, published, updated_at)
#Categories/subcategories (title, created_at, updated_at)

class Collection(models.Model):
    title = models.CharField(max_length=50)
    published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    

class Categories(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.TimeField()
    updated_at = models.DateTimeField(auto_now=True)
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='child')

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    collection = models.ManyToManyField(Collection)
    category = models.OneToOneField(Categories, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    
class Image(models.Model):
    source = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE,null=True ,blank = True, related_name="images")

    def __str__(self):
        return f"{self.alt_text}"
    

class Variant(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_for_sale = models.BooleanField()
    price = models.PositiveIntegerField()
    image = models.OneToOneField(Image , on_delete=models.CASCADE,blank = False)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="variants")

    def __str__(self):
        return f"{self.title}"