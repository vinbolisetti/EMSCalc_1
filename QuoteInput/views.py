from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import QuoteInputModel, LocationModel, HostingProviderModel
from .forms import QuoteInputForm

# Hosting Imports
from .models import get_ot_strings, get_cu_strings, get_aw_strings, \
    get_gcp_strings, get_ca_strings, get_az_strings, get_au_strings, get_multi_strings, \
    get_japan_strings, get_usemea_strings, get_sydney_strings, get_canada_strings, \
    get_gcpbrazil_strings, get_gcpasiane_strings, get_gcpasiaeast_strings, \
    get_gcpasia_strings, get_gcpaustralia_strings, get_gcpeurope_strings, get_gcpnane_strings, \
    get_gcpus_strings, get_awsall_strings, get_drhrs_strings, get_drsla1_srings, \
    get_drsla2_srings, get_drsla3_srings, get_encatrest_strings, get_s2svpns_strings
import json


def QuoteInputView(request):  # Add DR Planning Cost Form
    form = QuoteInputForm(request.POST or None)
    if request.method == 'POST':
        form = QuoteInputForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addquote')

    # notice this comes after saving the form to pick up new objects
    objects = QuoteInputModel.objects.all()
    return render(request, 'QuoteInput/addquote.html', {'objects': objects, 'form': form})


def load_location(request):
    hostingProvider_id = request.GET.get('hostingProvider_id')
    locations = LocationModel.objects.filter(hostingProvider_id=hostingProvider_id).all()
    # return render(request, 'QuoteInput/addquote.html', {'locations': locations})
    return JsonResponse(list(locations.values('id', 'name')), safe=False)


'''
    ot_strings = get_ot_strings()
    au_strings = get_au_strings()
    az_strings = get_az_strings()
    ca_strings = get_ca_strings()
    gcp_strings = get_gcp_strings()
    aw_strings = get_aw_strings()
    cu_strings = get_cu_strings()

    json_ot_strings = json.dumps(ot_strings)
    json_au_strings = json.dumps(au_strings)
    json_az_strings = json.dumps(az_strings)
    json_ca_strings = json.dumps(ca_strings)
    json_gcp_strings = json.dumps(gcp_strings)
    json_aw_strings = json.dumps(aw_strings)
    json_cu_strings = json.dumps(cu_strings)

    context['json_ot_strings'] = json_ot_strings
    context['json_au_strings'] = json_au_strings
    context['json_az_strings'] = json_az_strings
    context['json_ca_strings'] = json_ca_strings
    context['json_gcp_strings'] = json_gcp_strings
    context['json_aw_strings'] = json_aw_strings
    context['json_cu_strings'] = json_cu_strings

    multi_strings = get_multi_strings()
    json_multi_strings = json.dumps(multi_strings)
    context['json_multi_strings'] = json_multi_strings

    usemea_strings = get_usemea_strings()
    japan_strings = get_japan_strings()
    json_usemea_strings = json.dumps(usemea_strings)
    json_japan_strings = json.dumps(japan_strings)
    context['json_usemea_strings'] = json_usemea_strings
    context['json_japan_strings'] = json_japan_strings

    sydney_strings = get_sydney_strings()
    json_sydney_strings = json.dumps(sydney_strings)
    context['json_sydney_strings'] = json_sydney_strings

    canada_strings = get_canada_strings()
    json_canada_strings = json.dumps(canada_strings)
    context['json_canada_strings'] = json_canada_strings

    # gcp strings
    gcpus_strings = get_gcpus_strings()
    json_gcpus_strings = json.dumps(gcpus_strings)
    context['json_gcpus_strings'] = json_gcpus_strings

    gcpnane_strings = get_gcpnane_strings()
    json_gcpnane_strings = json.dumps(gcpnane_strings)
    context['json_gcpnane_strings'] = json_gcpnane_strings

    gcpeurope_strings = get_gcpeurope_strings()
    json_gcpeurope_strings = json.dumps(gcpeurope_strings)
    context['json_gcpeurope_strings'] = json_gcpeurope_strings

    gcpaustralia_strings = get_gcpaustralia_strings()
    json_gcpaustralia_strings = json.dumps(gcpaustralia_strings)
    context['json_gcpaustralia_strings'] = json_gcpaustralia_strings

    gcpasia_strings = get_gcpasia_strings()
    json_gcpasia_strings = json.dumps(gcpasia_strings)
    context['json_gcpasia_strings'] = json_gcpasia_strings

    gcpasiaeast_strings = get_gcpasiaeast_strings()
    json_gcpasiaeast_strings = json.dumps(gcpasiaeast_strings)
    context['json_gcpasiaeast_strings'] = json_gcpasiaeast_strings

    gcpasiane_strings = get_gcpasiane_strings()
    json_gcpasiane_strings = json.dumps(gcpasiane_strings)
    context['json_gcpasiane_strings'] = json_gcpasiane_strings

    gcpbrazil_strings = get_gcpbrazil_strings()
    json_gcpbrazil_strings = json.dumps(gcpbrazil_strings)
    context['json_gcpbrazil_strings'] = json_gcpbrazil_strings

    # AWS
    awsall_strings = get_awsall_strings()
    json_awsall_strings = json.dumps(awsall_strings)
    context['json_awsall_strings'] = json_awsall_strings

    # DR Hours
    drhrs_strings = get_drhrs_strings()
    json_drhrs_strings = json.dumps(drhrs_strings)
    context['json_drhrs_strings'] = json_drhrs_strings

    drsla1_strings = get_drsla1_srings()
    json_drsla1_strings = json.dumps(drsla1_strings)
    context['json_drsla1_strings'] = json_drsla1_strings

    drsla2_strings = get_drsla2_srings()
    json_drsla2_strings = json.dumps(drsla2_strings)
    context['json_drsla2_strings'] = json_drsla2_strings

    drsla3_strings = get_drsla3_srings()
    json_drsla3_strings = json.dumps(drsla3_strings)
    context['json_drsla3_strings'] = json_drsla3_strings

    encatrest_strings = get_encatrest_strings()
    json_encatrest_strings = json.dumps(encatrest_strings)
    context['json_encatrest_strings'] = json_encatrest_strings

    s2svpns_strings = get_s2svpns_strings()
    json_s2svpns_strings = json.dumps(s2svpns_strings)
    context['json_s2svpns_strings'] = json_s2svpns_strings
    '''


from .resources import CurrencyResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from .models import LocalCurrencyModel


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
            value = LocalCurrencyModel(
                data[0],
                data[1]
            )
            value.save()
    return render(request, 'upload.html')
