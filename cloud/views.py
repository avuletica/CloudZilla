from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.encoding import smart_str

from .models import FileUpload
from .forms import FileUploadForm
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
    files = FileUpload.objects.filter(file_fk=request.user.id)
    file_upload_form = FileUploadForm(request.POST or None, request.FILES or None)
    context = {
        "title": "Dashboard",
        "files": files,
        "file_upload_form": file_upload_form,
    }

    if file_upload_form.is_valid() and 'add_file' in request.POST:
        instance = file_upload_form.save(commit=False)
        instance.file_fk = User.objects.get(id=request.user.id)
        instance.filename = file_upload_form.cleaned_data.get("file")
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
