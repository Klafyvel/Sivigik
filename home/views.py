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

from home.models import get_latest_events, get_good_sites, get_events_by_category, get_category_by_name, get_beta_events, Category, get_pinned_events, HomeInfo
from member.forms import CreateMemberForm

def home(request):
    """Displays the home page."""
    pinned = get_pinned_events()
    event_list = get_latest_events()
    site_infos = get_object_or_404(HomeInfo, pk=1)
    signin_form = CreateMemberForm()
    return render(request, 'home/accueil.html', {'event_list'     :event_list,
                                                   'pinned':pinned,
                                                   'current':-1,
                                                   'site_infos':site_infos,
                                                   'signin':signin_form})
def category(request, category_name):
    """Display the asked category"""
    print(request.path)
    if category_name == 'beta':
        event_list = get_beta_events()
        category = Category(name='B&ecirc;ta', displayed_name='B&ecirc;ta', comment='Articles en b&ecirc;ta')
        current=-2
    else:
        category = get_category_by_name(category_name)
        event_list = get_events_by_category(category)
        current = category.pk

    return render(request, 'home/category.html', {'event_list' :event_list,
                                                   'category':category,
                                                   'current':current})

