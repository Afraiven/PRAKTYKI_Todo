from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from .models import Todo, Projekt
from .forms import TodoForm, ProjektForm, NewUserForm
from django.db.models import Count
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect(frontend)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})

def frontend(request):
    form = TodoForm()
    form_projekt = ProjektForm()
    projekty = Projekt.objects.all()
    todo_do_zrobienia = Todo.objects.all().filter(status="Do zrobienia").order_by('projekt').order_by('-priorytet')
    todo_realizowane = Todo.objects.all().filter(status="Realizowane").order_by('projekt').order_by('-priorytet')
    todo_wykonane = Todo.objects.all().filter(status="Wykonane").order_by('projekt').order_by('-priorytet')
    context = {"todo_do_zrobienia": todo_do_zrobienia, "todo_realizowane": todo_realizowane, "todo_wykonane": todo_wykonane, "form": form, "form_projekt": form_projekt, "projekty": projekty}
    return render(request, 'base.html', context)

def dodaj(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.autor = request.user
        instance.save()
        return redirect(frontend)

def dodaj_projekt(request):
    form = ProjektForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.autor = request.user
        instance.save()
        return redirect(frontend)    

def delete(request, id):
    zadanie = Todo.objects.get(id=id)
    zadanie.delete()

    return redirect(frontend)

def delete_projekt(request, id):
    projekt = Projekt.objects.get(id=id)
    projekt.delete()

    return redirect(frontend)



def edit(request, id):
    zadanie = Todo.objects.get(id=id)
    form = TodoForm(instance=zadanie)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=zadanie)
        print(form.is_valid())
        if form.is_valid():
            form.save()

    return redirect(frontend)


def edit_projekt(request, id):
    projekt = Projekt.objects.get(id=id)
    form = ProjektForm(instance=projekt)
    if request.method == 'POST':
        form = ProjektForm(request.POST, instance=projekt)
        if form.is_valid():
            form.save()

    return redirect(frontend)
