from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
class AdvertiserForm(forms.ModelForm):
    class Meta:
        model = Advertiser
        fields="__all__"  
    def __init__(self,*args,**kwargs):
        super(AdvertiserForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        exclude=["status"]
        widgets={
            'date':DateInput(attrs={'type':"date"})
        }  
    def __init__(self,*args,**kwargs):
        super(AdsForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"

class AdsTypeForm(forms.ModelForm):
    class Meta:
        model = AdsType
        fields="__all__"
        
    def __init__(self,*args,**kwargs):
        super(AdsTypeForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"


class AddAdvertiserLoginTable(UserCreationForm):
    class Meta:
        model = User
        fields = ["password1", "password2","email"]
    def __init__(self,*args,**kwargs):
        super(AddAdvertiserLoginTable,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"