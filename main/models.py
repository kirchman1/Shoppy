from django.db import models

# Create your models here.

class Item(models.Model):
    slug = models.SlugField('Unique name', unique=True)
    title = models.CharField('Title of the Item', max_length=200)
    image = models.CharField('Image', max_length=50)
    desc = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField('Name', max_length=200)
    surname = models.CharField('Surname', max_length=200)
    email = models.CharField('Email', max_length=200)
    number = models.CharField('Phone number', max_length=200)
    basket = models.TextField('Basket')

    def __str__(self):
        return self.name + ' ' + self.surname + ' (' + self.number + ')'