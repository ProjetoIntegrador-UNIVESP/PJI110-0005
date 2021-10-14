import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.shortcuts import redirect
from example.forms import LogMessageForm
from example.models import LogMessage
from django.http import HttpResponse
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "example/about.html")

def contact(request):
    return render(request, "example/contact.html")

def hello_there(request, name):
    return render(
        request,
        'example/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "example/log_message.html", {"form": form})