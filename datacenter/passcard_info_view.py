from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from datacenter.functions import is_visit_long, get_format_entered_at, get_format_duration


def passcard_info_view(request, passcode):
      p = get_object_or_404(Passcard, passcode=passcode)
      this_passcard_visits = []
      v = Visit.objects.filter(passcard=p)
      for x in v:
          dictionary = dict()
          dictionary['entered_at'] = get_format_entered_at(x)
          dictionary['duration'] = get_format_duration(x)
          dictionary['is_strange'] = is_visit_long(x)
          this_passcard_visits.append(dictionary)
      context = {
        'passcard': p,
        'this_passcard_visits': this_passcard_visits
      }
      return render(request, 'passcard_info.html', context)
