from django.utils import timezone
from django.db import models

# Create your models here.

class Categories(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):   
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Color(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('1000 to 2000','1000 to 2000'),
        ('2000 to 3000','2000 to 3000'),
        ('3000 to 4000','3000 to 4000'),
        ('4000 to 5000','4000 to 5000'),
        ('5000 to 6000','5000 to 6000'),
        )
    Price=models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.Price


class Product(models.Model):
    CONDITIONS=(
        ('NEW','NEW'),
        ('OLD','OLD')
     )
    STOCK=(('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK'))
    STATUS=(('Publish','Publish'),('Draft','Draft'))

    UNIQUE_Id=models.CharField(unique=True,null=True,blank=True,max_length=1000)
    image=models.ImageField(upload_to='Product_IMG/IMG/%Y%m%d')
    name=models.CharField(max_length=500)
    price=models.IntegerField()
    condition=models.CharField(choices=CONDITIONS,max_length=100)
    information=models.TextField()
    description=models.TextField()
    stock=models.CharField(choices=STOCK,max_length=100)
    status=models.CharField(choices=STATUS,max_length=200)
    created_date=models.DateTimeField(default=timezone.now)

    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if self.UNIQUE_Id is None and self.created_date and self.id:
            self.UNIQUE_Id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)

class Images(models.Model):
    images=models.ImageField(upload_to='Product_IMG/IMG/%Y%m%d')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.images.name

class Tag(models.Model):
    name=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name