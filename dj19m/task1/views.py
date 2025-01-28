from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm, is_valid_data
from .models import *
# Create your views here.


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if is_valid_data(username, password, repeat_password, age, users, info):
            Buyer.objects.create(name=username, age=age)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            return render(request, 'task1/registration_page.html', info)

    return render(request, 'task1/registration_page.html', info)


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if is_valid_data(username, password, repeat_password, age, users, info):
                Buyer.objects.create(name=username, age=age)
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                return render(request, 'task1/registration_page.html', info)

    else:
        form = RegistrationForm()
    return render(request, 'task1/registration_page.html', {'form': form})


def platform(request):
    return render(request, 'task1/main_page.html')


def shop(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'task1/shop.html', context)


def basket(request):
    return render(request, 'task1/basket.html')
