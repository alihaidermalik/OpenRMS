from django.db import models

# Create your models here.

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    phone = models.IntegerField(max_length=10, null=True)

class Table(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    chairs = models.IntegerField()
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

class TableStatus(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.TextChoices('Free', 'Reserved', 'Busy')

class TableTrack(models.Model):
    serial = models.AutoField(primary_key=True)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    reservation_date = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class OrderType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextChoices('Take away', 'Dine in', 'Home delivery')

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    orderType_id = models.ForeignKey(OrderType, on_delete=models.SET_NULL)

class OrderDetails(models.Model):
    serial = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(MenuItem, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    amount = models.IntegerField()
    discount_id = models.ForeignKey(DiscountType, on_delete=models.SET_NULL)
    tax_id = models.ForeignKey(Tax, on_delete=models.CASCADE)

class Tax(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(max_length=2)
    active = models.BooleanField(default=True)
    orderType_id = models.ForeignKey(OrderType, on_delete=models.SET_NULL)

class DiscountType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(max_length=2)
    active = models.BooleanField(default=True)
    orderType_id = models.ForeignKey(OrderType, on_delete=models.SET_NULL)

class DeliveryTrack(models.Model):
    serial = models.AutoField(primary_key=True)
    estimated_time = models.DateTimeField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deliverd = models.BooleanField(default=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(max_length=2)
 
 class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    salary = models.IntegerField()

class PayRoll(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField()
    bonus = models.IntegerField()

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextChoices('Admin', 'Super Admin', 'Manager', 'Delivery Boy', 'Waiter', 'Cashier')

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
