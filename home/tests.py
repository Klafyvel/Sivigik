from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

from home.models import Event

def create_event(name, pub_date):
	"""
		Create an event with the given name and the 
		specified publication date.
	"""
	return Event.objects.create(name=name, pub_date = pub_date)

class EventViewTests(TestCase):
	def test_index_view_with_no_event(self):
		"""
		If no event, there should be a message.
		"""
		response = self.client.get(reverse('home:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Pas d'évènements disponibles.")
		self.assertQuerysetEqual(response.context['event_list'], [])

	def test_index_with_a_future_event(self):
		"""
		A event published in the future should not be displayed.
		"""
		create_event(name="Future event", timezone.now() + datetime.timedelta(days=2))
		response = self.client.get(reverse('home:index'))
		self.assertContains(response, "Pas encore d'évènements disponibles.")
		self.assertQuerysetEqual(response.context['event_list'], [])

