from django.shortcuts import render
from . import models
from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest


def index(request):
    team_members = models.TeamMember.objects.all()
    menu_item = models.MenuItem.objects.all()
    about_us = models.AboutUs.objects.last()
    reviews = models.ClientReview.objects.order_by('-id')[:3]
    milliy = models.MenuItem.objects.filter(cuisine=1)
    fast_food = models.MenuItem.objects.exclude(cuisine=1)
    delay = 0.1
    context = {
        'member':team_members,
        'item':menu_item,
        'about_us':about_us,
        'reviews':reviews,
        'milliy':milliy,
        'fast_food':fast_food,

        
    }

    

    return render(request, 'index.html', context)

def about(request):
    about_us = models.AboutUs.objects.last()

    context = {
        'about_us':about_us,
        
    }

    return render(request, 'about.html', context)



def contact(request):
    if request.method == 'POST':
        
            models.Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                body=request.POST['body']
            )
    return render(request, 'contact.html')



def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request,'login.html')
        except:
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':

        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            models.User.objects.create_user(
                username=username, 
                password=password, 
                first_name=f_name, 
                last_name=l_name
                )
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('index')


from django.contrib import messages

@login_required(login_url='login') 
def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        booking_date = request.POST['booking_date']  
        booking_time = request.POST['booking_time']  
        num_people = int(request.POST['num_people'])  
        special_request = request.POST.get('special_request', '')  

       
        if not name or not email or not booking_date or num_people <= 0:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'book_table.html')

     
        reservation = models.Reservation(
            name=name,
            email=email,
            booking_date=booking_date,
            booking_time=booking_time,
            num_people=num_people,
            special_request=special_request,
        )
        reservation.save()

        messages.success(request, 'Your table has been booked successfully!')
        return redirect('index')  

    return render(request, 'booking.html')

def menu(request):
    items = models.MenuItem.objects.all()
    milliy = models.MenuItem.objects.filter(cuisine=1)
    fast_food = models.MenuItem.objects.exclude(cuisine=1)
    context = {
        'items':items,
        'milliy':milliy,
        'fast_food':fast_food,
    }

    return render(request, 'menu.html',context)


from django.shortcuts import render


def dish_detail(request, slug):
    try:
        dish = models.MenuItem.objects.get(slug=slug)
    except models.MenuItem.DoesNotExist:
        return render(request, '404.html') 
    context = {'dish': dish}
    return render(request, 'dish_detail.html', context)


def add_to_cart(request, slug):
    dish = models.MenuItem.objects.get(slug=slug)
    cart_item, created = models.Cart.objects.get_or_create(user=request.user, dishes=dish)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, cart_id):
    cart_item = models.Cart.objects.get(id=cart_id)
    cart_item.delete()
    return redirect('cart')

def cart(request):
    cart_items = models.Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def checkout(request):
    cart_items = models.Cart.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.dishes.price for item in cart_items)
    if request.method == 'POST':
        ...
        
    else:
        return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price})


def update_cart(request):
    if request.method == 'POST':
        for item in request.POST:
            if item.startswith('quantity_'):
                cart_item_id = item.split('_')[1]
                quantity = request.POST[item]
                if quantity.isdigit() and int(quantity) >= 1:
                    cart_item = models.Cart.objects.get(id=cart_item_id)
                    cart_item.quantity = int(quantity)
                    cart_item.save()
                else:
                    return HttpResponseBadRequest('Invalid quantity value.')
        return redirect('cart')
    else:
        return HttpResponseBadRequest('Only POST requests are allowed.')
