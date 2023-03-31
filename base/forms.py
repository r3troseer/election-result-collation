from django import forms
from .models import PollingUnit

# polling_unit_name=PollingUnit.objects.all().values_list('polling_unit_name')
class PollingUnitResultForm(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields ='__all__'

    def clean(self):
        cleaned_data = self.cleaned_data
        polling_unit_id = cleaned_data.get('polling_unit_id')
        ward_id = cleaned_data.get('ward_id')
        lga_id=cleaned_data.get('lga_id')
        uniquewardid=cleaned_data.get('uniquewardid')
        polling_unit_number=cleaned_data.get('polling_unit_number')
        polling_unit_name=cleaned_data.get('polling_unit_name')
        entered_by_user=cleaned_data.get('entered_by_user')
        date_entered=cleaned_data.get('date_entered')
        user_ip_address=cleaned_data.get('user_ip_address')
