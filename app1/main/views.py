
from django.shortcuts import redirect, render
from django.contrib import messages
from main.models import People
from .forms import AddDataForm

def index(request):
    if request.method == 'POST':
        form = AddDataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            People.objects.create(name=name, address=address)
            return redirect('index')
        else:
            messages.error(request, 'Пожалуйста, введите Ф.И.О.')
    else:
        form = AddDataForm()
    data = People.objects.all()
    return render(request, 'index.html', {'form': form, 'data': data})



            