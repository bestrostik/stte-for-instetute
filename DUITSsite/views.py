from django.shortcuts import render, get_object_or_404, redirect
from .models import Corse, Material
from .forms import CorseForm, MaterialForm 
from django.http import HttpResponse


def corse_list(request):
    corses = Corse.objects.all()
    return render (request, 'corses/corse_list.html',  {'corses': corses,})

def corse_detail(request, pk):
    corse = get_object_or_404(Corse, id=pk)
    materials = corse.materials.all()
    return render(request, 'corses/corse_detail.html', {'corse': corse, 'materials': materials})

def add_corse(request):
    if request.method == "POST":
        form = CorseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('corse_list')
    else:
        form = CorseForm()
    return render(request, 'corses/add_corse.html', {'form': form})

def add_material(request):
    corse = get_object_or_404(Corse)
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.corse = corse 
            material.save()
            return redirect('corse_detail', pk=corse.pk) 
    else:
        form = MaterialForm()
    return render(request, 'corses/add_material.html', {'form': form, 'corse': corse})


