from django.db import models
from usermanagament.models import Profile
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['name']


class Item(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    photo = CloudinaryField('image', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    STUDENT = 'student'
    DOCTOR = 'doctor'

    ITEM_TYPES = [
        (STUDENT, 'Student'),
        (DOCTOR, 'Doctor'),
    ]
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES, null=False, blank=False)

    class Meta:
        ordering = ['-created_at']

        
    def __str__(self):
        return self.name
    

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="orders")
    items = models.ManyToManyField(Item, related_name="orders")
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.profile.username} - {self.status}"
    

class Package(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(default=0)
    photo = CloudinaryField('image')

    class Meta:
        ordering = ['name']


class PackageItem(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='items')
    photo = CloudinaryField('image', null=False, blank=False)



    class Meta:
        ordering = ['name']

        
    def __str__(self):
        return self.name


class PackageOrder(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='orders')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="packageOrders")
