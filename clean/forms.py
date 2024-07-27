from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'  # You can also use a list of the fields like this ['name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['service'].empty_label = "Select a service"  # Adds the default placeholder option for selecting a service
        
        
        