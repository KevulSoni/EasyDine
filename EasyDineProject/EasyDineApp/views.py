from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_owner.models import Restaurant
# from .forms import BookingForm
from EasyDineApp.models import Booking
from django.contrib import messages




# Create your views here.
def home(request):
    return render(request, 'EasyDineApp/index.html')

def login(request):
    #messages.success(request, "this is a test message")
    return render(request, 'EasyDineApp/login.html')
    #return HttpResponse("this is homepage")
def signup(request):
    return render(request, 'EasyDineApp/signup.html')

def about(request):
    return render(request, 'EasyDineApp/about.html')

   
def contact(request):
    return render(request, 'EasyDineApp/contact.html')

def booking(request):
    return render(request, 'EasyDineApp/booking.html')

def service(request):
    return render(request, 'EasyDineApp/service.html')

def rest_list(request):
    return render(request, 'EasyDineApp/restList.html')

def restDetails(request):
    return render(request, 'EasyDineApp/restDetails.html')

def paymentSuccess(request):
    latest_booking = Booking.objects.latest('id')
    total_payment = 50*latest_booking.people
    return render(request, 'EasyDineApp/paymentSuccess.html', {'latest_booking':latest_booking, 'total_payment':total_payment})

def payment(request):
    latest_booking = Booking.objects.latest('id')
    total_payment = 50*latest_booking.people
    return render(request, 'EasyDineApp/payment.html', {'latest_booking':latest_booking, 'total_payment':total_payment})

def paymentInvoice(request):
    restaurant = get_object_or_404(Restaurant= rest_list, pk=restaurant_id)
    return render(request, 'EasyDineApp/paymentInvoice.html', {'restaurant':restaurant})

def restaurantDetails(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'EasyDineApp/restDetails.html', {'restaurant':restaurant})

def rest_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'EasyDineApp/restList.html', {'restaurants':restaurants})
        
        
def booktable(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        datetime = request.POST['datetime']
        people = request.POST['people']
        phone = request.POST['phone']
        booking=Booking.objects.create(name=name, email=email, datetime=datetime, people=people, phone=phone)
        booking.save()
        messages.success(request, 'Wooh!Your Table is scheduled') 
        #payment_summary
        latest_booking = Booking.objects.latest('id')
        total_payment = 50*latest_booking.people
        return render(request, 'EasyDineApp/paymentInvoice.html', {'latest_booking':latest_booking, 'total_payment':total_payment})
    return render(request, 'EasyDineApp/booking.html')

#signup view
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # Replace 'home' with your desired URL after login
    else:
        form = SignUpForm()
    return render(request, 'EasyDineApp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/index.html')  # Replace 'home' with your desired URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'EasyDineApp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with your login URL




































           
    
