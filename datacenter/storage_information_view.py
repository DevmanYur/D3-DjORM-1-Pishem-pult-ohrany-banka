from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.functions import is_visit_long, get_format_entered_at, get_format_duration


def storage_information_view(request):
    non_closed_visits = []
    p = Passcard.objects.all()
    for n in p:
        v = Visit.objects.filter(passcard=n, leaved_at=None)
        for x in v:
            dictionary = dict()
            dictionary['who_entered'] = x.passcard.owner_name
            dictionary['entered_at'] = get_format_entered_at(x)
            dictionary['duration'] = get_format_duration(x)
            dictionary['is_strange'] = is_visit_long(x)
            non_closed_visits.append(dictionary)

    context = {
        'non_closed_visits': non_closed_visits,  
    }
    return render(request, 'storage_information.html', context)
