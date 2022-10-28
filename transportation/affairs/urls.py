from django.urls import path
from affairs import views

urlpatterns = [
    path('index',views.MainPageView),
    ]   