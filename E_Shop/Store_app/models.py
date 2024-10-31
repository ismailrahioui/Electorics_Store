from django.utils import timezone
from django.db import models

# Create your models here.

class Categories(models.Model):
    name=models.CharField(max_length=200)

class Brand(models.Model):   
    name=models.CharField(max_length=200)
class Color(models.Model):
    name=models.CharField(max_length=200)
    code=models.CharField(max_length=50)
class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('1000 TO 2000','1000 TO 2000'),
        ('2000 TO 3000','2000 TO 3000'),
        ('3000 TO 4000','3000 TO 4000'),
        ('4000 TO 5000','4000 TO 5000'),
        ('5000 TO 6000','5000 TO 6000'),
        )
    Price=models.CharField(choices=FILTER_PRICE,max_length=60)


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
    descriptions=models.TextField()
    stock=models.CharField(choices=STOCK,max_length=100)
    status=models.CharField(choices=STATUS,max_length=200)
    created_date=models.DateTimeField(default=timezone.now)

    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    def save(self,*ags,**kawgrs):
        if self.UNIQUE_Id is None and self.created_date and self.id:
            self.UNIQUE_Id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)