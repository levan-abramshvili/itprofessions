from django.shortcuts import render
from .models import Profession
from .models import Career
from .models import CareerProfs
from django.views.generic import DetailView


def index(request):
    data = {
        'title': 'It-профессии',
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Про нас'
    }

    return render(request, 'main/about.html', data)


def project(request):
    professions = CareerProfs.objects.all()
    data = {
        'title': 'Профессии',
        'professions': professions
    }
    return render(request, 'main/project.html', data)


class CareerProfsDetailView(DetailView):
    model = CareerProfs
    template_name = 'main/details_view.html'
    context_object_name = 'profession'