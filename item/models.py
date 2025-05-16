from django.db import models
from usermanagament.models import Profile
from cloudinary.models import CloudinaryField
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    STUDENT = 'student'
    DOCTOR = 'doctor'

    ITEM_TYPES = [
        (STUDENT, 'Student'),
        (DOCTOR, 'Doctor'),
    ]
    category_type = models.CharField(max_length=10, choices=ITEM_TYPES, null=False, blank=False)

    class Meta:
        ordering = ['-created_at']


class Item(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    photo = CloudinaryField('image', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

        
    def __str__(self):
        return self.name


class PointItem(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    points = models.IntegerField(default=0)
    description = models.CharField(max_length=300, blank=True, null=True)
    photo = CloudinaryField('image', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

        
    def __str__(self):
        return self.name
    

class Package(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.IntegerField(default=0)
    photo = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    purchased_at = models.DateTimeField(null=True, blank=True, default=None)

    items = models.ManyToManyField(Item, through='OrderItem', related_name='orders', blank=True)
    point_items = models.ManyToManyField(PointItem, through='OrderPointItem', related_name='orders', blank=True)
    package = models.ManyToManyField(Package, through='OrderPackage', related_name='orders', blank=True)

    total_price = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)

    active_type = models.CharField(
        max_length=13,
        choices=[('price', 'price'), ('point', 'point')],
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['created_at']

    
    def update(self):
        if self.active_type == 'price':
            self.total_price = sum(order_item.quantity * order_item.item.price for order_item in self.orderitem_set.all())
            self.total_price += sum(orderpackage.quantity * orderpackage.package.price for orderpackage in self.orderpackage_set.all())
        elif self.active_type == 'point':
            self.total_points = sum(order_point_item.quantity * order_point_item.point_item.points for order_point_item in self.orderpointitem_set.all())
        
        if self.status == 'finished' and self.purchased_at is None:
            self.purchased_at = now()

        self.save()

    def save(self, *args, **kwargs):
        if self.status == 'finished' and self.purchased_at is None:
            self.purchased_at = now()
        super().save(*args, **kwargs) 
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name} in order {self.order.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.update()


class OrderPackage(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.package.name} in order {self.order.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.update()


class OrderPointItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    point_item = models.ForeignKey(PointItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.point_item.name} in order {self.order.id}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.order.update()