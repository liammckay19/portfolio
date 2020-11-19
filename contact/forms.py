from .models import Contact
from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from crispy_forms.bootstrap import FormActions


class ContactForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.layout = Layout(Submit('Submit', 'Submit', css_class='btn btn-primary'))

    class Meta:
        model = Contact
        fields = ["subject", "email", "message"]
