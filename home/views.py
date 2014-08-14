#This file is part of Sivigik.
#
#Foobar is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Foobar is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from django.views import generic

from home.models import get_latest_events, get_good_sites, get_events_by_category, get_category_by_name, get_beta_events, Category, get_pinned_events

def home(request):
    """Displays the home page."""
    pinned = get_pinned_events()
    event_list = get_latest_events()
    good_sites_list = get_good_sites()

    return render(request, 'home/home_base.html', {'event_list'     :event_list,
                                                   'good_sites_list':good_sites_list,
                                                   'pinned':pinned})
def category(request, category_name):
    """Display the asked category"""
    if category_name == 'beta':
        event_list = get_beta_events()
        category = Category(name='B&ecirc;ta', displayed_name='B&ecirc;ta', comment='Articles en b&ecirc;ta')
    else:
        category = get_category_by_name(category_name)
        event_list = get_events_by_category(category)

    return render(request, 'home/home_base.html', {'event_list' :event_list,
                                                   'category':category})

