from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from .models import CurrencyModel2, QuoteInputModel2, LocationModel2
from .forms import QuoteInputForm2


# Create your views here.


def QuoteInputView2(request):  # Add DR Planning Cost Form
    form = QuoteInputForm2(request.POST or None)
    if request.method == 'POST':
        form = QuoteInputForm2(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tables')

    # notice this comes after saving the form to pick up new objects
    objects = QuoteInputModel2.objects.all()
    return render(request, 'tables/tables.html', {'objects': objects, 'form': form})


def load_location(request):
    hostingProvider_id = request.GET.get('hostingProvider_id')
    locations = LocationModel2.objects.filter(hostingProvider_id=hostingProvider_id).all()
    # return render(request, 'QuoteInput/addquote.html', {'locations': locations})
    return JsonResponse(list(locations.values('id', 'name')), safe=False)


class AddQuoteListView(ListView):  # List View
    template_name = 'tables/list_quote.html'
    queryset = QuoteInputModel2.objects.all()
    form = QuoteInputModel2.objects.all()

    '''def get_queryset(self):
        return self.queryset'''

    def get(self, request, *args, **kwargs):
        context = {'form': self.queryset}
        return render(request, self.template_name, context)


class AddQuoteDetailView(DetailView):  # Update View
    template_name = 'tables/detail_quote.html'
    form_class = QuoteInputForm2
    object = QuoteInputModel2.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuoteInputModel2, id=id_)


class AddQuoteUpdateView(UpdateView):  # Update View
    template_name = 'tables/tables.html'
    form_class = QuoteInputForm2
    queryset = QuoteInputModel2.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuoteInputModel2, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class AddQuoteDeleteView(DeleteView):  # Delete View
    template_name = 'tables/delete_quote.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(QuoteInputModel2, id=id_)

    def get_success_url(self):
        return reverse('list_quote')


def errorPage(request):
    return render(request, '404.html')


def login(request):
    return render(request, 'login.html')


def table1(request):
    return render(request, 'tables2/tables1.html')


def table2(request):
    return render(request, 'tables2/tables_dynamic.html')