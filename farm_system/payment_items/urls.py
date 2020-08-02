from django.urls import path, include

from payment_items.views import calculatePaymentPrice

app_name = 'Payment_items'
urlpatterns=[
    path('/hehe',calculatePaymentPrice,name="hehe")
]
