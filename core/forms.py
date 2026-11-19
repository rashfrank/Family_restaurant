from django import forms
from .models import Booking
class BookingForm(forms.ModelForm):
 class Meta:
  model=Booking; fields=['name','email','date','guests','notes']; widgets={'date':forms.DateInput(attrs={'type':'date'}),'notes':forms.TextInput(attrs={'placeholder':'Напр., 4 и 7 лет. Аллергия на арахис.'})}
