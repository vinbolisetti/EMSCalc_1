from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemMasterForm, CompanyForm, ChainForm
from django.views import View


# Create your views here.
from .models import Company


class CreateItem(View):
    template_name = 'popup_form.html'

    def get(self, request):
        item_form = ItemMasterForm(request.POST or None)
        context = {
            "form": item_form,
            'is_create': True,
        }
        return render(self.request, self.template_name, context)


def CompanyCreate(request):

    form1 = CompanyForm(request.POST or None)
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        "form1": form1,
        "title": "Company Form"
    }
    return render(request, "create.html", context)


def CompanyEdit(request, pk=None):

    form = CompanyForm(request.POST or None)
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        "form": form,
        "title": "Company Form"
    }
    return render(request, "create.html", context)
