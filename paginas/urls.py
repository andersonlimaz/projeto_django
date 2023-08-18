from django.urls import path
from .views import IndexView

urlpatterns = [ 
    # Sempre que for criar path caminho 
    #path('endereço', MinhaView.as_view(), name='Nome-da-url'),
    path('', IndexView.as_view(), name='inicio'),
]