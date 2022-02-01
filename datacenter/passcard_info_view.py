from django.shortcuts import render
from .visit_time_functions import format_duration, get_duration, is_visit_long

from datacenter.models import Passcard, Visit


def passcard_info_view(request, passcode):
    """Отображает данные по визитам."""
    this_passcard_visits = []
    passcard = Passcard.objects.get(passcode=passcode)

    for passcard_visit in Visit.objects.filter(passcard=passcard):
        this_passcard_visits.append(
            dict(
                entered_at=passcard_visit.entered_at,
                duration=format_duration(get_duration(passcard_visit)),
                is_strange=is_visit_long(get_duration(passcard_visit),
                                         minutes=60)
            )
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
