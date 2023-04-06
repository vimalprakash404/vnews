from django import forms
from .models import *
from django.forms.widgets import DateInput,TextInput
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields="__all__"
        widgets={
            'date':DateInput(attrs={'type':"date"}),
            "content":TextInput(attrs={"hidden":"","required" :False})
        }
    def __init__(self,*args,**kwargs):
        super(NewsForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control form-control-user"
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields="__all__"
        
    def __init__(self,*args,**kwargs):
        super(CategoryForm,self).__init__(*args,**kwargs)
        for i in self.fields.values():
            i.widget.attrs['class']="form-control"