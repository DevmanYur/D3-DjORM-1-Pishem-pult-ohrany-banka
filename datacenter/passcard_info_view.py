from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.functions import is_visit_long, get_format_entered_at, get_format_duration


def passcard_info_view(request, passcode):
      passcard = get_object_or_404(Passcard, passcode=passcode)
      this_passcard_visits = []
      visit = Visit.objects.filter(passcard=passcard)
      for visit_value in visit:
          dictionary = {
          'entered_at': get_format_entered_at(visit_value),
          'duration': get_format_duration(visit_value),
          'is_strange': is_visit_long(visit_value)
          }
          this_passcard_visits.append(dictionary)
      context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
      }
      return render(request, 'passcard_info.html', context)
