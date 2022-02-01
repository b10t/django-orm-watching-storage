from django.shortcuts import render
from .visit_time_functions import format_duration, get_duration, is_visit_long

from datacenter.models import Visit


def storage_information_view(request):
    """Отображает список людей, кто сейчас в хранилище."""
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            dict(
                who_entered=visit.passcard.owner_name,
                entered_at=visit.entered_at,
                duration=format_duration(get_duration(visit)),
                is_strange=is_visit_long(get_duration(visit), minutes=60)
            )
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
