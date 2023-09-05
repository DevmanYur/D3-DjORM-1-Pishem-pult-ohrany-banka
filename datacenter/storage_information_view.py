from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.functions import is_visit_long, get_format_entered_at, get_format_duration


def storage_information_view(request):
    non_closed_visits = []
    passcard = Passcard.objects.all()
    for passcard_value in passcard:
        visit = Visit.objects.filter(passcard=passcard_value, leaved_at=None)
        for visit_value in visit:
            dictionary = dict()
            dictionary['who_entered'] = visit_value.passcard.owner_name
            dictionary['entered_at'] = get_format_entered_at(visit_value)
            dictionary['duration'] = get_format_duration(visit_value)
            dictionary['is_strange'] = is_visit_long(visit_value)
            non_closed_visits.append(dictionary)

    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
