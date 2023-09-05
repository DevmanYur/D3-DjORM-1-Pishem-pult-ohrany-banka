from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.functions import is_visit_long, get_format_entered_at, get_format_duration

def storage_information_view(request):
    non_closed_visits = []

    visit = Visit.objects.filter(leaved_at=None)
    for visit_value in visit:
            dictionary = {
            'who_entered': visit_value.passcard.owner_name,
            'entered_at': get_format_entered_at(visit_value),
            'duration': get_format_duration(visit_value),
            'is_strange': is_visit_long(visit_value)
            }
            non_closed_visits.append(dictionary)

    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
