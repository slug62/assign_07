from django.shortcuts import render
from django.views import generic
from .models import Area


class IndexView(generic.ListView):
    template_name = 'measurements/index.html'
    context_object_name = 'area_objects'

    def get_queryset(self):
        return Area.objects.all()

