from django import forms
from .models import Product, ProductType, Review, Article, Job, Event


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model=ProductType
        fields='__all__'

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'