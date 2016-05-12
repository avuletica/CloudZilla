from django import forms
from django.contrib.auth.models import User
from .models import FileUpload


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file']

    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields['file'].label = "Choose a file"


class UserPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']

    def __init__(self, *args, **kwargs):
        super(UserPasswordForm, self).__init__(*args, **kwargs)
        self.initial['password'] = 'New password'

