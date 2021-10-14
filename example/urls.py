from example.models import LogMessage
from django.urls import path
from example import views

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="example/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("example/<name>", views.hello_there, name="hello_there"),
]