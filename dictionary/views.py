from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404, render

from .models import*
# Create your views here.
def home(request):
    return render(request,'dictionary/home.html')

def about(request):
    return render(request,'dictionary/about.html')

def search(request):
    drugs = Drug.objects.all()
    drug2s = Drug2.objects.all()
    drugds = Drug.objects.all()
    drug2ds = Drug2.objects.all()
    drugis = Drug.objects.all()
    drug2is = Drug2.objects.all()
    name = None
    if 'src' in request.GET:
        name = request.GET['src']
        if name:
            drugs = drugs.filter(name2__icontains = name )
            drug2s = drug2s.filter(name2__icontains = name )
            drugds = drugds.filter(description__icontains = name )
            drug2ds = drug2ds.filter(description__icontains = name )
            drugis = drugis.filter(indication__icontains = name )
            drug2is = drug2is.filter(indication__icontains = name )
            
    context = {'drugs':drugs, 'drug2s':drug2s,'drugds':drugds, 'drug2ds':drug2ds,'drugis':drugis, 'drug2is':drug2is, }

    return render(request,'dictionary/search.html',  context )


class DrugDetails(DetailView):
    model =  Drug
    template_name = 'dictionary/drug.html'
    queryset = Drug.objects.all()



    



#def get_object(self):
        #id = self.kwargs.get('id')
        #return get_object_or_404(Drug, id=id)
    

