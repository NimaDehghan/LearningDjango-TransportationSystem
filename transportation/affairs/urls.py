from django.urls import path
from affairs import views

urlpatterns = [
    
    path('courier/list',views.CourierListView),
    path('courier/create',views.CourierCreateView),
    path('courier/update/<int:id>',views.CourierUpdateView),
    path('courier/delete/<int:id>',views.CourierDeleteView),
    path('customer/list',views.CustomerListView),
    path('customer/create',views.CustomerCreateView),
    path('customer/update/<int:id>',views.CustomerUpdateView),
    path('customer/delete/<int:id>',views.CustomerDeleteView),
    path('index',views.MainPageView),
    ]   