from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

listaTareas=[
    ['Tarea1','Tarea1','12-04-2024','Pendiente','Martin'],
    ['Tarea2','Tarea2','13-04-2024','Pendiente','Marco'],
    ['Tarea3','Tarea3','13-04-2024','Pendiente','Harry']
]

def index(request):
    return render(request,'index.html',{
        'listaTareas' : listaTareas
    })
def nuevaTarea(request):
    if request.method == 'POST':
        print(request.POST)
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fechaFin = request.POST.get('fechaFinalizacion')
        estatus = 'Pendiente'
        responsable = request.POST.get('responsable')
        listaTareas.append([nombre,descripcion,fechaFin,estatus,responsable])
        return HttpResponseRedirect(reverse('tareasApp:index'))

    return render(request,'nuevaTarea.html')