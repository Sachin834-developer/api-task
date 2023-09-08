from django.db import models

# Create your models here.

class Commodity(models.Model):
    commodity_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    date=models.DateField(auto_now_add=True)
    availibilty=models.BooleanField(default=True)

    """
    {
{
"commodity_name" : 'Tomato',
"price" : 200.00,
"date" : '08/09/2023',
"availibilty": True
}
    
    """