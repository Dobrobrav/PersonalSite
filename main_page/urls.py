from django.urls import path
from .views import *


urlpatterns =[
    path('main_info/', (MainInfoAPIView.as_view())),
    path('contact_details/', (ContactDetailsAPIView.as_view()))
]