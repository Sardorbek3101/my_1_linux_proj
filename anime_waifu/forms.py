from django import forms
from anime_waifu.models import CustomUSer

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUSer
        fields = ('username', 'last_name', 'first_name', 'email', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
