from django.shortcuts import render
from django.views import generic
from .models import Sala, Reserva, Empleador

# Create your views here.

def index(request):
    """
    	página de inicio del sitio
    """
    num_salas=Sala.objects.all().count()
    num_reservas=Reserva.objects.all().count()
    # Salas confirmadas (estado = 'c')
    num_reservas_disponibles=Reserva.objects.filter(estado__exact='c').count()
    num_empleadores=Empleador.objects.count()

    return render(
        request,
        'index.html',
        context={'num_salas':num_salas,'num_reservas':num_reservas,'num_reservas_disponibles':num_reservas_disponibles,'num_empleadores':num_empleadores},
    )

def sala_detail_view(request,pk):
    try:
        sala_id=Sala.objects.get(pk=pk)
    except Sala.DoesNotExist:
        raise Http404("Sala no existe")

    #sala_id=get_object_or_404(Sala, pk=pk)
    
    return render(
        request,
        'rooms/sala_detail.html',
        context={'sala':sala_id,}
    )

class SalaListView(generic.ListView):
    model = Sala
    context_object_name = 'sala_list' # your own name for the list as a template variable
    queryset = Sala.objects.filter(nombre__icontains='sala')[:5] # Get 5 salas containing the title sala
    template_name = 'rooms/sala_list.html' # Specify your own template name/location
    paginate_by = 1

class SalaDetailView(generic.DetailView):
    model = Sala
    context_object_name = 'sala_detail'