from drug.models import Drugs, Category
from django import forms
from django.utils import timezone


class DrugRegistration(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = ['brand_name', 'generic_name', 'des', 'category',
                  'price', 'discount_price', 'batch_no', 'image', 'expiry_date']
        # widget = {'expiry_date': forms.DateField(widget=forms.DateInput())}
        input_formats = {'expiry_date': ['%d/%m/%Y %H:%M']}

    # def __init__(self, request, *args, **kwargs):
    #     # question_pk = kwargs.pop('question_pk')
    #     user_pharmacy = request.user.pharmacyuser.works_at.name
    #     super(DrugRegistration, self).__init__(*args, **kwargs)
    #     if request:
    #         self.fields['pharmacy'].initial = user_pharmacy
    #         self.fields['pharmacy'].widget = forms.HiddenInput()

    def clean_expiry_date(self):
        drug_name = self.cleaned_data['generic_name']
        expiry_date = self.cleaned_data['expiry_date']
        present_date = timezone.now().date()
        # gets the number of days difference
        difference = int(str(expiry_date - present_date).split()[0])
        if difference < 1:
            raise forms.ValidationError(
                "The drug '{}' is expired".format(drug_name))
        elif difference < 7:
            raise forms.ValidationError(
                "The drug '{}' expiration date is too close".format(drug_name))
        else:
            return expiry_date
