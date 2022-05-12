from django.db import models


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.cat_name
class Product(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='categ')
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Users(models.Model):
    objects = None
    tg_id = models.IntegerField()
    username = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=150)

class Date(models.Model):
    # stol_id = models.IntegerField(auto_created=True, unique=True)
    name = models.CharField(max_length=100)
    nachalo = models.DateTimeField()
    okonchanie = models.DateTimeField(null=True)
    price = models.IntegerField(null=True)
    active = models.BooleanField(default=False)

class Cart(models.Model):
    tg_id = models.IntegerField()
    name = models.TextField()
    quantity = models.IntegerField()
    price = models.TextField()

    def __str__(self):
        return self.name


class Bar(models.Model):
    bar_id = models.IntegerField()


class Bar_cart(models.Model):
    bar_id = models.IntegerField()
    name = models.TextField()
    quantity = models.IntegerField()
    price = models.TextField()