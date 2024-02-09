from django.shortcuts import render
from .models import *


def index_page(request):
    skills = Skills.objects.all()
    languages = Languages.objects.all()
    experience = Exp.objects.all()
    education = Education.objects.all()
    context = {'skills': skills,
               'languages': languages,
               'experience': experience,
               'education': education
               }

    return render(request, 'index.html', context=context)
