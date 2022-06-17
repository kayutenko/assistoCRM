from django.db import models
from django.forms import ModelForm
from django import forms
from django.utils import timezone

class Contact(models.Model):
    type = models.CharField(max_length=200, choices=[('Lead','Lead'),('Contact','Contact')], default='Contact')
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6, choices=[('Male','Male'),('Female','Female')])
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    image_url = models.CharField(max_length=1000,default='/static/ocrm/img/generic-customer.jpg')
    def __str__(self):
        return ' '.join([self.first_name, self.second_name])


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['image_url']
        widgets = {'type': forms.HiddenInput()}


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    max_tenor = models.IntegerField(default=0)
    max_limit = models.IntegerField(default=0)
    min_price = models.FloatField(default=0)
    base_price = models.FloatField(default=0)
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class Channel(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    response = models.CharField(max_length=30)
    offered_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return ' - '.join([self.contact.first_name, self.channel.name, self.offered_product.name])

class OwnedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, default=1)
    purchase_date = models.DateTimeField(auto_now=True)
    tenor = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.product.name


class OwnedProductForm(ModelForm):
    class Meta:
        model = OwnedProduct
        fields = '__all__'
        widgets = {'contact': forms.HiddenInput()}

