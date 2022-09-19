from django.shortcuts import render
from management.models import Product
from crm.forms import SubscribeForm
from crm.models import Crm
from telegramBot.sendmessage import sendTelegram

def index_page(request):
    products_list = Product.objects.all()
    form = SubscribeForm()
    dict_object = {'products_list':products_list,'form':form }
    return render(request, 'index.html', dict_object)

def product_page(request, id):
    product = Product.objects.get(id=id)
    dict_object = {'product': product}
    return render(request, 'product-details.html', dict_object)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        elemet = Crm(crm_name=name, crm_email=email)
        elemet.save()
        sendTelegram(tg_name=name, tg_phone=email)
        return render(request, './thanks.html', {'name':name, 'phone':email})
    else:
        return render(request, './thanks.html')

def shop_page(request):
    return render(request, 'shop.html')

def checkout_page(requests):
    return render(requests, 'checkout.html')

def cart_page(requests):
    return render(requests, 'cart.html')