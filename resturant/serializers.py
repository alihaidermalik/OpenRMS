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
from rest_framework import serializers


class BranchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class TableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class TableStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableStatus
        fields = '__all__'

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableStatus
        fields = ('id','name','phone','address','longitude', 'latitude')

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TableTrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TableTrack
        fields = '__all__'

class TaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'

class DiscountTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiscountType
        fields = '__all__'

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'

class DealItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DealItem
        fields = '__all__'

class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeliveryTrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryTrack
        fields = '__all__'

class RevenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'

class PayRollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PayRoll
        fields = '__all__'

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

