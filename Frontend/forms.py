from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Frontend.models import PaymentDb
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CreateUserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

    def __init__(self,*args,**kwargs):
        super(CreateUserform,self).__init__(*args,**kwargs)

        self.fields['password1'].widget.attrs = {'class': 'form-control', 'placeholder': 'Confirm password',
                                                 'required': 'required'}
        self.fields['password2'].widget.attrs = {'class': 'form-control', 'placeholder': 'Confirm password',
                                                 'required': 'required'}
class CarPaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDb
        fields = "__all__"

    def __init__(self,*args,**kwargs):
        super(CarPaymentForm,self).__init__(self,*args,**kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'car_name'
            'car_id'
            'amount',
            Submit('submit','Pay',css_class='button white btn-block btn-primary')
        )