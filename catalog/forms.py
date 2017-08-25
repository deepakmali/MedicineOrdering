from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    Name_of_the_firm = forms.CharField(help_text="Enter the name of your firm.")
    Address = forms.CharField(help_text="Enter the Delivery address.")
    Pincode = forms.IntegerField()
    Email = forms.EmailField()
    Contact_person = forms.CharField(help_text="Enter the Name of the contact person.")
    Designation = forms.CharField(help_text="Enter the designation of the contact person.")
    Office_phone = forms.CharField(help_text="Enter office phone number.")
    Mobile_phone = forms.CharField(help_text="Enter mobile number.")
    Drug_License = forms.CharField(help_text="Enter the Valid Drug License Number.")
    DL_expiry_date = forms.DateField(help_text="Enter the Drug license Expiry date.")
    GSTIN = forms.CharField(help_text="Enter the GSTIN number.")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'Name_of_the_firm', 'Address', 'Pincode', 'Email', 'Contact_person',
                  'Designation', 'Office_phone', 'Mobile_phone', 'Drug_License', 'DL_expiry_date', 'GSTIN')

    # def save(self, commit=True, *args, **kwargs):
    #     # user = super(self).save()
    #     print self.cleaned_data.get('Name_of_the_firm')
    #     print self.cleaned_data.get('Address')
    #     print self.cleaned_data.get('Pincode')
    #     print self.cleaned_data.get('Email')
    #     print self.cleaned_data.get('Contact_person')
    #     print self.cleaned_data.get('Designation')
    #     print self.cleaned_data.get('Office_phone')
    #     print self.cleaned_data.get('Mobile_phone')
    #     print self.cleaned_data.get('Drug_License')
    #     print self.cleaned_data.get('DL_expiry_date')
    #     print self.cleaned_data.get('GSTIN')
        
