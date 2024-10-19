from django.urls import path

from DjangoCV.urls import urlpatterns
from .views import MonCV_view # Make sure you have this view defined

urlpatterns =[
    path('', MonCV_view, name='MonCV'), # Default route for the MonCV page
]