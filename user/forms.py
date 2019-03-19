from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User,Group


class UserRegistrationForm(UserCreationForm):

    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        help_texts = {
            'username': None,
            'password2': None,
        }


class UserGroup(forms.Form):
    users = User.objects.all()

    #user = forms.ChoiceField(choices=users,widget=forms.Select())
    name = forms.MultipleChoiceField(widget=forms.Select(),choices=(('a','abc'),('b','ads')))
    names = forms.Field()




