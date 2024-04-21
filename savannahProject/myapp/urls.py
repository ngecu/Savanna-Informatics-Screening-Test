from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world_view),
    path('sms_callback', views.sms_callback),

    path('customers/', views.customer_list),
    path('customers/<int:pk>/', views.customer_detail),
]

    # https://3712-102-212-236-180.ngrok-free.app/sms_callback
