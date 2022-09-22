from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def dashboard(request):
    context = {
        "all_the_dojos": Dojo.objects.all(),
        "all_the_ninjas": Ninja.objects.all()
    }
    return render(request, 'dashboard.html', context)

def create_dojo(request):
    print('Got Post Info')
    name_from_form = request.POST['name']
    city_from_form = request.POST['city']
    state_from_form = request.POST['state']
    print(name_from_form)
    print(city_from_form)
    print(state_from_form)
    Dojo.objects.create(name = name_from_form, city = city_from_form, state = state_from_form)
    return redirect('/')

def create_ninja(request):
    first_name_from_form = request.POST['first_name']
    last_name_from_form = request.POST['last_name']
    dojo_from_form = request.POST['dojo']
    Ninja.objects.create(first_name = first_name_from_form, last_name = last_name_from_form, dojo_id = dojo_from_form)
    ninja_dojo = Dojo.objects.get(id=dojo_from_form)
    ninja_dojo.num_of_ninjas += 1
    print(ninja_dojo.num_of_ninjas)
    ninja_dojo.save()
    return redirect('/')

def delete_dojo(request,dojo_id):
    dojo_ninjas = Ninja.objects.filter(dojo_id = dojo_id)
    print(dojo_ninjas)
    dojo_ninjas.delete()
    selected_dojo = Dojo.objects.get(id=dojo_id)
    selected_dojo.delete()
    return redirect('/')