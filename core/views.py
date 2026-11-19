from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Dish, Challenge
from .forms import BookingForm
def home(request): return render(request,'core/index.html',{'dishes':Dish.objects.all()[:3],'challenges':Challenge.objects.all()[:3]})
def menu(request): return render(request,'core/menu.html',{'dishes':Dish.objects.all()})
def challenges(request): return render(request,'core/challenges.html',{'challenges':Challenge.objects.all()})
def booking(request):
 if request.method=='POST':
  form=BookingForm(request.POST)
  if form.is_valid(): form.save(); messages.success(request,'Бронирование принято! Мы свяжемся с вами для подтверждения.'); return redirect('booking')
 else: form=BookingForm()
 return render(request,'core/booking.html',{'form':form})
