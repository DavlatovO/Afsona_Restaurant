from django.shortcuts import render
from . import models


def index(request):
    team_members = models.TeamMember.objects.all()
    menu_item = models.MenuItem.objects.all()
    about_us = models.AboutUs.objects.last()
    delay = 0.1
    context = {
        'member':team_members,
        'item':menu_item,
        'about_us':about_us,
        
    }

    

    return render(request, 'index.html', context)