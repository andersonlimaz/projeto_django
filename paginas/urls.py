from django.urls import path
from .views import PaginaInicial

urlpatterns = [ 
    # Sempre que for criar path caminho 
    #path('endereço', MinhaView.as_view(), name='Nome-da-url'),
    path('', PaginaInicial.as_view(), name='inicio'),
]