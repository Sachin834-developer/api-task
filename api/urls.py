from django.urls import path
from .views import *

urlpatterns = [
    path('commodity-list/',commodity_list,name='list'),
    path('commodity-edit/<int:pk>',commodity_detail,name='update'),
]
