from django.urls import include, path
from rest_framework import routers
from resturant import views

router = routers.DefaultRouter()
router.register(r'branch', views.BranchViewSet)
router.register(r'table', views.TableViewSet) 
router.register(r'table-status', views.TableStatusViewSet) 
router.register(r'customer', views.CustomerViewSet) 
router.register(r'reservation', views.ReservationViewSet) 
router.register(r'order', views.OrderViewSet) 
router.register(r'table-track', views.TableTrackViewSet) 
router.register(r'tax', views.TaxViewSet) 
router.register(r'discount', views.DiscountTypeViewSet) 
router.register(r'bill', views.BillViewSet) 
router.register(r'menu', views.MenuViewSet) 
router.register(r'menu-item', views.MenuItemViewSet) 
router.register(r'deal', views.DealViewSet) 
router.register(r'deal-item', views.DealItemViewSet) 
router.register(r'order', views.OrderDetailsViewSet) 
router.register(r'employee', views.EmployeeViewSet) 
router.register(r'payroll', views.PayRollViewSet) 
router.register(r'revenue', views.RevenueViewSet) 
router.register(r'feedback', views.FeedbackViewSet) 


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('admin/', admin.site.urls),
]


