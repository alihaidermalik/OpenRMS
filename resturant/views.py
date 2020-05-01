# importing models
from django.shortcuts import render
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
#importing required libraries
from rest_framework import viewsets
from rest_framework import permissions
#importing serializers
from .serializers import BranchSerializer
from .serializers import TableSerializer
from .serializers import TableStatusSerializer
from .serializers import CustomerSerializer
from .serializers import ReservationSerializer
from .serializers import OrderSerializer
from .serializers import TableTrackSerializer
from .serializers import TaxSerializer
from .serializers import DiscountTypeSerializer
from .serializers import BillSerializer
from .serializers import MenuSerializer
from .serializers import MenuItemSerializer
from .serializers import DealSerializer
from .serializers import DealItemSerializer
from .serializers import OrderDetailsSerializer
from .serializers import EmployeeSerializer
from .serializers import DeliveryTrackSerializer
from .serializers import PayRollSerializer
from .serializers import RevenueSerializer
from .serializers import FeedbackSerializer

# Create your views here.

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('name')
    serializer_class = BranchSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all().order_by('name')
    serializer_class = TableSerializer

class TableStatusViewSet(viewsets.ModelViewSet):
    queryset = TableStatus.objects.all().order_by('table')
    serializer_class = TableStatusSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('name')
    serializer_class = CustomerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('reservation_date')
    serializer_class = ReservationSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('date')
    serializer_class = OrderSerializer

class TableTrackViewSet(viewsets.ModelViewSet):
    queryset = TableTrack.objects.all().order_by('table_id')
    serializer_class = TableTrackSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all().order_by('date')
    serializer_class = TaxSerializer

class DiscountTypeViewSet(viewsets.ModelViewSet):
    queryset = DiscountType.objects.all().order_by('date')
    serializer_class = DiscountTypeSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all().order_by('date')
    serializer_class = BillSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('name')
    serializer_class = MenuSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by('name')
    serializer_class = MenuItemSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all().order_by('name')
    serializer_class = DealSerializer

class DealItemViewSet(viewsets.ModelViewSet):
    queryset = DealItem.objects.all().order_by('item_id')
    serializer_class = DealItemSerializer

class OrderDetailsViewSet(viewsets.ModelViewSet):
    queryset = OrderDetails.objects.all().order_by('serial')
    serializer_class = OrderDetailsSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('name')
    serializer_class = DeliveryTrackSerializer

class PayRollViewSet(viewsets.ModelViewSet):
    queryset = PayRoll.objects.all().order_by('date')
    serializer_class = TaxSerializer

class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all().order_by('date')
    serializer_class = RevenueSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('date')
    serializer_class = FeedbackSerializer