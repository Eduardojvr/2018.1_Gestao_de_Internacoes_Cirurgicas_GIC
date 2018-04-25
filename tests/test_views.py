from __future__ import unicode_literals

import datetime
import json
import pytz

from django.http import Http404
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from schedule.models import Calendar, CalendarRelation, Event, Rule
from schedule.serializer import EventSerializer
from schedule.models.calendars import Calendar
from schedule.models.events import Event, Occurrence
from schedule.models.rules import Rule


class TestViewAPI(TestCase):
    def setUp(self):
        calendar = Calendar(name = 'Test Calendar')
        calendar.save()
        self.event_attr = {
            'id':1,
            'title': 'victor',
            'start': datetime.datetime(2013, 1, 5, 8, 0, tzinfo=pytz.utc),
            'end': datetime.datetime(2013, 1, 5, 9, 0, tzinfo=pytz.utc),
            'status': None,
            'calendar': calendar
        }

        self.serializer_data = {
            'id':0,
            'title':'joão',
            'start': datetime.datetime(2013, 1, 5, 8, 0, tzinfo=pytz.utc),
            'end': datetime.datetime(2013, 1, 5, 9, 0, tzinfo=pytz.utc),
            'status':None,
            'calendar': calendar
        }
        self.event = Event.objects.create(**self.event_attr)
        self.serializer = EventSerializer(instance=self.event)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(['title', 'updated_on', 'hospital', 'calendar', 'created_on', 'rule', 'end', 'color_event', 'registration', 'status', 'description', 'end_recurring_period', 'CPF', 'start', 'creator', 'id']),set(data.keys()))

    # def test_fields_content(self):
    #     data = self.serializer.data
    #     self.assertEqual(data['title'],self.event_attr['title'])