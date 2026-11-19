from django.db import models
class Category(models.Model):
 name=models.CharField(max_length=100)
 def __str__(self): return self.name
class Dish(models.Model):
 category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='dishes',null=True,blank=True)
 name=models.CharField(max_length=150); description=models.TextField(); price=models.DecimalField(max_digits=8,decimal_places=2); image=models.CharField(max_length=255,blank=True); tags=models.CharField(max_length=255,blank=True); is_child_friendly=models.BooleanField(default=False)
 def __str__(self): return self.name
class Challenge(models.Model):
 title=models.CharField(max_length=150); description=models.TextField(); age_range=models.CharField(max_length=50); duration=models.CharField(max_length=50); reward=models.CharField(max_length=150); status=models.CharField(max_length=50,default='Активный квест')
 def __str__(self): return self.title
class Booking(models.Model):
 name=models.CharField(max_length=120); email=models.EmailField(); date=models.DateField(); guests=models.CharField(max_length=100); notes=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True); status=models.CharField(max_length=30,default='Новая')
 def __str__(self): return f'{self.name} — {self.date}'
