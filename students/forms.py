from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from courses.models import Course

class UserRegistrationForm(UserCreationForm):
    username=forms.CharField(label="Имя пользователя")
    password1=forms.CharField(label="Введите пароль")
    password2=forms.CharField(label="Подтвердите пароль")
    class Meta:
        model=User
        fields=["username",]
    
class CourseEnrollForm(forms.Form):
    course=forms.ModelChoiceField(queryset=Course.objects.all(),
   widget=forms.HiddenInput) 













   