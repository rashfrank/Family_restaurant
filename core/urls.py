from django.urls import path
from . import views
urlpatterns=[path('',views.home,name='home'),path('menu/',views.menu,name='menu'),path('challenges/',views.challenges,name='challenges'),path('booking/',views.booking,name='booking')]
