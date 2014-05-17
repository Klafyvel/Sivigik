from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from django.views import generic

from home.models import get_latest_events, get_good_sites, get_events_by_category, get_category_by_name

def home(request):
    """Displays the home page."""
    event_list = get_latest_events()
    good_sites_list = get_good_sites()

    return render(request, 'home/home_base.html', {'event_list'     :event_list,
                                                   'good_sites_list':good_sites_list})
def category(request, category_name):
    """Display the asked category"""
    category = get_category_by_name(category_name)
    event_list = get_events_by_category(category)

    return render(request, 'home/home_base.html', {'event_list' :event_list,
                                                   'category':category})

