from django.views.generic import TemplateView  # Generic class based view


# Create your views here.


class home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"
