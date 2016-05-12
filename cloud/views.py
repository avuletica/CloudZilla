from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.contrib.auth.hashers import make_password

from .models import FileUpload
from .forms import FileUploadForm, UserPasswordForm
from src import settings
import os


def home(request):
    context = {
        "title": "CloudZilla",
    }
    if request.user.is_authenticated():
        return redirect(reverse('dashboard'))
    else:
        return render(request, "home.html", context)


@login_required
def dashboard(request):
    password_form = UserPasswordForm(request.POST or None, instance=request.user)
    files = FileUpload.objects.filter(file_fk=request.user.id)
    file_upload_form = FileUploadForm(request.POST or None, request.FILES or None)
    context = {
        "title": "Dashboard",
        "files": files,
        "file_upload_form": file_upload_form,
        "password_form": password_form,
    }

    if file_upload_form.is_valid() and 'add_file' in request.POST:
        instance = file_upload_form.save(commit=False)
        instance.file_fk = User.objects.get(id=request.user.id)
        minify_file_name = file_upload_form.cleaned_data.get("file")
        minify_file_name = str(minify_file_name)
        text = minify_file_name
        if len(minify_file_name) > 20:
            minify_file_name = text[0:10] + '...' + text[-10:]

        instance.filename = minify_file_name
        instance.save()
        return redirect(reverse('dashboard'))

    if password_form.is_valid() and 'Update' in request.POST:
        instance = password_form.save(commit=False)
        new_password = password_form.cleaned_data.get("password")
        instance.set_password(new_password)
        instance.save()

        return redirect(reverse('dashboard'))

    return render(request, "dashboard.html", context)


@login_required
def delete_file(request, file_id=None):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect(reverse('dashboard'))


@login_required
def download_file(request, file_id=None):
    file = FileUpload.objects.get(id=file_id)
    response = HttpResponse()
    response['Content-Type'] = ''
    response['Content-Disposition'] = "attachment; filename=" + file.filename
    response['X-Sendfile'] = smart_str(os.path.join(settings.MEDIA_ROOT, file.filename))
    return response
