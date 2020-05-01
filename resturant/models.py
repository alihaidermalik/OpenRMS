from django.db import models

# Create your models here.

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    phone = models.IntegerField(max_length=10, null=True)

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    chairs = models.IntegerField()
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

class TableStatus(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = (('free','Free'),('reserved','Reserved'),('busy','Busy'))

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10, unique=True)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=10)

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    reservation_date = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    order_choices = (('takeAway','Take away'), ('dineIn','Dine in'), ('homeDelivery','Home delivery'))
    order_type = models.CharField(choices=order_choices,max_length=200)

class TableTrack(models.Model):
    serial = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Tax(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(max_length=2)
    active = models.BooleanField(default=True)
    order_choices = (('takeAway','Take away'), ('dineIn','Dine in'), ('homeDelivery','Home delivery'))
    order_type = models.CharField(choices=order_choices,max_length=200)

class DiscountType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    amount = models.IntegerField(max_length=2)
    active = models.BooleanField(default=True)
    order_choices = (('takeAway','Take away'), ('dineIn','Dine in'), ('homeDelivery','Home delivery'))
    order_type = models.CharField(choices=order_choices,max_length=200)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.IntegerField()
    discount_id = models.ForeignKey(DiscountType, null=True, blank=True, on_delete=models.SET_NULL)
    tax_id = models.ForeignKey(Tax, on_delete=models.CASCADE)

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(unique=True, upload_to = 'pictures')

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(max_length=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(unique=True, upload_to = 'pictures')

class Deal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(unique=True, upload_to = 'pictures')

class DealItem(models.Model):
    deal_id = models.ForeignKey(Deal, on_delete=models.CASCADE)
    item_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

class OrderDetails(models.Model):
    serial = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(MenuItem, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    role_choice = (('admin','Admin'), ('superAdmin','Super Admin'), ('manager','Manager'), ('deliveryBoy','Delivery Boy'), ('waiter','Waiter'), ('cashier','Cashier'))
    role = models.CharField(choices=role_choice,max_length=200)
    salary = models.IntegerField()
    password = models.CharField(max_length=10)
    active = models.BooleanField(default=True)

class DeliveryTrack(models.Model):
    serial = models.AutoField(primary_key=True)
    estimated_time = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliverd = models.BooleanField(default=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)

class PayRoll(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField()
    bonus = models.IntegerField()

class Revenue(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Feedback(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    phone = models.IntegerField(max_length=10)
    name = models.CharField(max_length=200)
    comment = models.TextField()
