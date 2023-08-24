from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "index.html"

class Paginapg(TemplateView):
    template_name ="pagamento.html"