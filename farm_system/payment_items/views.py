from django.shortcuts import render

# Create your views here.
from cart.models import Cart
from products.models import *


def calculatePaymentPrice(request):
    #you can pass the ids of the carts the user has selected and query for the cart,
    # (replace the relevant parts in order for you to query) or you can
    #check for the carts which have not been checked out. Like in the line below
    uncheckedCarts = Cart.objects.filter(is_checked_out=False)
    # selectedCarts = Cart.objects.filter(id__in=#the list of the ids)

    totalAmountToPay = 0
    for cart in uncheckedCarts:
        product = Product.objects.filter(id=cart.id)
        if (product.objects.instance_of(Tools)):

            tool=product.objects.instance_of(Tools)
            totalAmountToPay += tool.price

        elif (product.objects.instance_of(Machinery)):
            machinery = product.objects.instance_of(Machinery)
            totalAmountToPay += machinery.price

        elif (product.objects.instance_of(Pesticide)):
            pesticide = product.objects.instance_of(Pesticide)
            totalAmountToPay = pesticide.price

        elif (product.objects.instance_of(Fertilizer)):
            fertilizer = product.objects.instance_of(Fertilizer)
            totalAmountToPay = fertilizer.price

        elif (product.objects.instance_of(Food)):
            food = product.objects.instance_of(Food)
            totalAmountToPay = food.price
        else:
            print("No product selected")

    print(totalAmountToPay)

