from django.shortcuts import render

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
    return render(request,'formTareas.html')