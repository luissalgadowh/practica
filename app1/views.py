from django.shortcuts import render, HttpResponseRedirect, reverse

from .models import Person

from .forms import AddPersonForm

from .tasks import add

# Create your views here.
def index(request):

    persons = Person.objects.all()

    return render(request, 'index.html', {'persons': persons})

def add_person(request):

    form = AddPersonForm(request.POST or None)

    if request.POST:

        if form.is_valid():

            form.save()

            nombre = form.cleaned_data['name']
            print(nombre)
            apellido = form.cleaned_data['apellido']
            print(apellido)
            correo = form.cleaned_data['email']
            print(correo)
            task = add.delay(nombre, apellido, correo)
            print(task)

            return HttpResponseRedirect(reverse('index'))

    return render(request, 'add_person.html', {'form': form})