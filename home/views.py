from django.shortcuts import render, redirect, HttpResponse


# Create your views here.


def home(request):
    '''form = AddQuote.objects.all()
    context = {
        'form': form
    }'''
    return render(request, 'home/index.html')


