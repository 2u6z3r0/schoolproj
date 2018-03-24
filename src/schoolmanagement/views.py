from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from .models import School

# Create your views here.

from django.http import HttpResponse


def welcome(request):
        return HttpResponse('Hello, World!')

def school_view(request, id):
        print(request.user.get_full_name)
        print(request.user.is_staff)
        print(request.user.is_admin)
        if not request.user.is_staff:
                raise Http404
        instance = get_object_or_404(School,id=id)
        print(instance.name)
        context = {
                "title" : "school Management",
                "instance": instance,
        }
        return render(request, "school.html", context)

def school_view2(request, id):
        return render(request, "school_view2.html")
