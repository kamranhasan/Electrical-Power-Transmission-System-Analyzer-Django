from django import forms
from .models import Contact
from django.db import models


class Messages(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('First_Name', 'Last_Name','Contact_Number','Business_Email', 'How_Can_We_Help_You' )

