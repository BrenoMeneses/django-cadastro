from django import forms
from .models import user
from django.core.exceptions import ValidationError

class formularioCadastro(forms.ModelForm):
    
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "digite seu nome"}))
    
    idade = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "digite sua idade"}))

    class Meta:
        model = user
        fields = ['nome', 'idade']

    def clean_nome(self, *args, **kwargs):
        nome = self.cleaned_data.get("nome")
        if user.objects.filter(nome = nome):
            raise forms.ValidationError("nome já cadastrado")
        
        else:
            return nome