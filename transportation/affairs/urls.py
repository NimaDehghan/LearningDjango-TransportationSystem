from django.urls import path
from affairs import views

urlpatterns = [
    path('courier/list',views.CourierListView),
    path('courier/create',views.CourierCreateView),
    path('courier/update/<int:id>',views.CourierUpdateView),
    path('courier/delete/<int:id>',views.CourierDeleteView),
    path('transport/create', views.TransportCreateView,name="transportInsert"),
    path('transport/list',views.TransportListView),
    path('transport/update/<int:id>',views.TransportUpdateView),
    path('transport/delete/<int:id>',views.TransportDeleteView),
    path('delivery/create',views.DeliveryCreateView),
    path('delivery/list',views.DeliveryListView),
    path('delivery/update/<int:id>',views.DeliveryUpdateView),
    path('delivery/delete/<int:id>',views.DeliveryDeleteView),
    path('customer/list',views.CustomerListView),
    path('customer/create',views.CustomerCreateView),
    path('customer/update/<int:id>',views.CustomerUpdateView),
    path('customer/delete/<int:id>',views.CustomerDeleteView),
    path('index',views.MainPageView),
    ]   