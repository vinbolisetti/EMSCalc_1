from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from .models import QuoteInputModel, LocationModel
from .forms import QuoteInputForm, MultiRegionForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def QuoteInputView(request):  # Add DR Planning Cost Form
    form = QuoteInputForm(request.POST or None)
    if request.method == 'POST':
        form = QuoteInputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('quote')

    # notice this comes after saving the form to pick up new objects
    objects = QuoteInputModel.objects.all()
    return render(request, 'AddQuote/add_quote.html', {'objects': objects, 'form': form})


def load_location(request):
    hostingProvider_id = request.GET.get('hostingProvider_id')
    locations = LocationModel.objects.filter(hostingProvider_id=hostingProvider_id).all()
    # return render(request, 'QuoteInput/addquote.html', {'locations': locations})
    return JsonResponse(list(locations.values('id', 'name')), safe=False)


from .resources import CurrencyResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .models import CurrencyModel


def simple_upload(request):
    if request.method == 'POST':
        currency_resource = CurrencyResource()
        dataset = Dataset()
        new_currency = request.FILES['myfile']

        if not new_currency.name.endswith('xlsx'):
            messages.info(request, 'unsupported format, save as xlsx and try uploading again')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_currency.read(), format='xlsx')
        for data in imported_data:
            value = CurrencyModel(
                data[0],
                data[1]
            )
            value.save()
    return render(request, 'upload.html')


class AddQuoteListView(ListView):  # List View
    template_name = 'AddQuote/list_quote.html'
    queryset = QuoteInputModel.objects.all()
    form = QuoteInputModel.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form': self.queryset}
        return render(request, self.template_name, context)


class AddQuoteDetailView(DetailView):  # Update View
    template_name = 'AddQuote/detail_quote.html'
    form_class = QuoteInputForm
    object = QuoteInputModel.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuoteInputModel, id=id_)


class AddQuoteUpdateView(UpdateView):  # Update View
    template_name = 'AddQuote/add_quote.html'
    form_class = QuoteInputForm
    queryset = QuoteInputModel.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuoteInputModel, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AddQuoteDeleteView(DeleteView):  # Delete View
    template_name = 'AddQuote/delete_quote.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuoteInputModel, id=id_)

    def get_success_url(self):
        return reverse('list_quote')


def errorPage(request):
    return render(request, '404.html')


def login(request):
    return render(request, 'AddQuote/login.html')


def MultiRegionCreate(request):

    form1 = MultiRegionForm(request.POST or None)
    if form1.is_valid():
        instance = form1.save(commit=False)
        instance.user_id = request.user
        instance.save()
        pk_value = instance.pk
        return HttpResponse(
            '<script>opener.closeAddPopup(window, "%s", "%s", "#id_group_id");</script>' % (pk_value, instance.name))

    context = {
        "form1": form1,
        "title": "Multiple Active Regions"
    }
    return render(request, "AddQuote/multi-region.html", context)
