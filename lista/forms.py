from django.forms import ModelForm
from .models import Todo, Projekt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['nazwa','opis','status', 'priorytet', 'projekt']
        CHOICES= (
        ('Do zrobienia', 'Do zrobienia'),
        ('Realizowane', 'Realizowane'),
        ('Wykonane', 'Wykonane'),
        )
        PRIORITY_CHOICES= (
        ('1', 'Niski'),
        ('2', 'Normalny'),
        ('3', 'Wysoki'),
        )
        widgets = {
                'nazwa': forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Nazwa'}),
                'opis': forms.TextInput(attrs={'class':'form-control', 'id':'opis', 'placeholder':'Opis'}),
                'status': forms.Select(attrs={'class':'form-control', 'id':'status'}, choices=CHOICES),
                'priorytet': forms.Select(attrs={'class':'form-control', 'id':'priority'}, choices=PRIORITY_CHOICES),
                'projekt': forms.Select(attrs={'class':'form-control', 'id':'projekt'},choices=Projekt.objects.all()),
            } 

            
class ProjektForm(ModelForm):
    class Meta:
        model = Projekt
        fields = ['nazwa','motyw']
        widgets = {
                'nazwa': forms.TextInput(attrs={'class':'form-control', 'id':'name_projekt', 'placeholder':'Nazwa projektu'}),
                'motyw': forms.TextInput(attrs={'class':'form-control','id':'motyw','type': 'color'}),
                
            } 

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

            