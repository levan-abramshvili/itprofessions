from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('project', views.project, name='project'),
    path('<int:pk>', views.CareerProfsDetailView.as_view(), name='professions-detail')
]