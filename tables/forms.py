from django import forms
from .models import QuoteInputModel2, LocationModel2


class QuoteInputForm2(forms.ModelForm):
    class Meta:
        model = QuoteInputModel2
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['location'].querset = LocationModel2.objects.none()

            if 'hostingProvider' in self.data:
                try:
                    hostingProvider_id = int(self.data.get('hostingProvider'))
                    self.fields['location'].queryset = LocationModel2.objects.filter(
                        hostingProvider_id=hostingProvider_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['location'].queryset = self.instance.hostingProvider.location_set.order_by('name')
