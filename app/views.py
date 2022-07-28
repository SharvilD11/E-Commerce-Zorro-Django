import json
from pyexpat.errors import messages
from turtle import update
from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Product, Orders, OrderUpdate

# Create your views here.
def index(request):
    
    return render(request, 'index.html',)
  
def deals(request):
    products = Product.objects.all()
    print(products)
    parameters = {'product' : products}
    return render(request, 'deals.html', parameters)

def iPhone13(request):
    return render(request, 'iPhone13.html')

def sonybravia(request):
    return render(request, 'sonybravia.html')

def applepro(request):
    return render(request, 'applepro.html')
    
def electronics(request):
    return render(request, 'electronics.html')

def fashion(request):
    return render(request, 'fashion.html')

def children(request):
    return render(request, 'children.html')

def women(request):
    return render(request, 'women.html')
   
def men(request):
    return render(request, 'men.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'tracker.html')
      
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone,)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id=order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id':id})
    return render(request, 'checkout.html')


def handleSignup(request):
    
        name =  request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        #pass2 = request.POST['pass2']
        
        myUser=User.objects.create_user(name, email, pass1)
        myUser.save()
        messages.success(request, "Registered on Zorro Successfully")
        return redirect('/')
    
def handleSignin(request):
   
    loginusername = request.POST['loginusername']
    loginpass = request.POST['loginpass']

    user = authenticate(username=loginusername , password=loginpass)

    if user is not None:
        login(request, user)
        messages.success(request, "LogIn Successful")
        return redirect('/')
    else:
        messages.error(request, "Invalid Credentials, Please Enter The Correct Information")
        return redirect('/')

def handleLogout(request):
    
    logout(request)
    messages.success(request, "LogOut Successful")
    return redirect('/')

def address(request):
    add = User.objects.filter(user=request.user)
    return render(request, 'address.html', {'add' :add})