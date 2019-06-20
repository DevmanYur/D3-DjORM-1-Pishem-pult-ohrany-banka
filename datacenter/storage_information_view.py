from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь

    non_closed_visits = [
        {
            "who_entered": "Richard Shaw",
            "entered_at": "11-04-2018 25:34",
            "duration": "25:03",
        }
    ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
