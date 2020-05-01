from django.contrib import admin
from resturant.models import Branch
from resturant.models import Table
from resturant.models import TableStatus
from resturant.models import Customer
from resturant.models import Reservation
from resturant.models import Order
from resturant.models import TableTrack
from resturant.models import Tax
from resturant.models import DiscountType
from resturant.models import Bill
from resturant.models import Menu
from resturant.models import MenuItem
from resturant.models import Deal
from resturant.models import DealItem
from resturant.models import OrderDetails
from resturant.models import Employee
from resturant.models import DeliveryTrack
from resturant.models import PayRoll
from resturant.models import Revenue
from resturant.models import Feedback


# Register your models here.
admin.site.register(Branch)
admin.site.register(Table)
admin.site.register(TableStatus)
admin.site.register(Customer)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(TableTrack)
admin.site.register(Tax)
admin.site.register(DiscountType)
admin.site.register(Bill)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Deal)
admin.site.register(DealItem)
admin.site.register(OrderDetails)
admin.site.register(Employee)
admin.site.register(DeliveryTrack)
admin.site.register(PayRoll)
admin.site.register(Revenue)
admin.site.register(Feedback)