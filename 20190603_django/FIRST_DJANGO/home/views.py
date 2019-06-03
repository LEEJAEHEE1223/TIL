from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def contact(request):
    value = f'값 넘기기'
    return render(request, 'home/contact.html', {'value': value})


def help_me(request):
    return render(request, 'home/help_me.html')
