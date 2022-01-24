from django.shortcuts import render, redirect
from .models import CPSCostModel, DRPlanningLaborCostRateModel
from .forms import CPSCostForm, DRPlanningLaborCostRateForm
from django.views.generic import CreateView, ListView
from django.db.models import Sum
from django.urls import reverse
import json


def DRCostView(request):  # Add DR Planning Cost Form
    form = DRPlanningLaborCostRateForm(request.POST or None)
    if request.method == 'POST':
        form = DRPlanningLaborCostRateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('drcost')

    # notice this comes after saving the form to pick up new objects
    objects = DRPlanningLaborCostRateModel.objects.all()
    return render(request, 'DRPlanning/drplanning.html', {'objects': objects, 'form': form})


def CPSCostView(request):  # Add DR Planning Cost Form
    form = CPSCostForm(request.POST or None)
    if request.method == 'POST':
        form = CPSCostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cpscost')

    # notice this comes after saving the form to pick up new objects
    objects = CPSCostModel.objects.all()
    return render(request, 'CPSInput/cpsinput.html', {'objects': objects, 'form': form})


'''class CPSCostView(CreateView):  # CPS Cost Input Form
    template_name = 'CPSInput/cpsinput.html'
    form_class = CPSCostForm
    queryset = CPSCostModel.objects.all()

    def get(self, request, *args, **kwargs):
        context = {'form_summary': self.queryset}
        return render(request, self.template_name, context)

    def form_valid(self, queryset):
        print(queryset.cleaned_data)
        return super().form_valid(queryset)

    def get_success_url(self):
        return reverse('cpscost')'''


'''class CPSSummaryView(ListView):        # Detail View 7. Perpetual sw
    template_name = 'CPS_Cost_Summary/cpssummary.html'
    queryset = CPSCostModel.objects.all()
    total_volDiscPrice_p = CPSCostModel.objects.aggregate(Sum('cpsHours'))['cpsHours__sum'] or 0.00

        def get_total(self):
            total = 0
            for instance in AddPerpetualModel.volDiscPrice_p.all():
                total += instance
            return total

        def get_queryset(self):
            return self.queryset

        def get(self, request, *args, **kwargs):
            context = {'form_cps': self.queryset}

        return render(request, self.template_name, context)'''


class CPSSummaryView(ListView):  # Detail View 7. Perpetual sw
    template_name = 'CPS_Cost_Summary/cpssummary.html'
    queryset = CPSCostModel.objects.all()

    def get(self, request, *args, **kwargs):
        context = {'form_summary': self.queryset}

        return render(request, self.template_name, context)
