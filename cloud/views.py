from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


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
    context = {
        "title": "Dashboard",
    }

    return render(request, "dashboard.html", context)
