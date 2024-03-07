from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Course
from .models import Group

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-email'})
    )
    username = forms.CharField(label=_("Username"), widget=forms.TextInput(attrs={'class': 'form-username'}))
    
    
    ROLE_CHOICES = [
        ('teacher', _('Вчитель')),
        ('student', _('Студент')),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, label=_("Я є"), required=True)
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label=_("Курс"),required=False)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label=_("Group"),required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-lastname'}))
    
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "role",'course','group','first_name','last_name')
