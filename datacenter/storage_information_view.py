from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit


def get_duration(entered_at):
    """Возвращает продолжительность времени.

    Args:
        entered_at (datetime): Дата и время входа

    Returns:
        str: Отформатированное время
    """
    return format_duration(localtime(timezone.now()) - localtime(entered_at))


def format_duration(difference_time):
    """Возвращает отформатированное время.

    Args:
        difference_time (timedelta): Разница во времени

    Returns:
        str: Отформатированное время
    """
    hours = difference_time.seconds // 3600
    minutes = difference_time.seconds % 3600 // 60
    return f'{hours}:{minutes}'


def is_visit_long(visit, minutes=60):
    # TODO пишите код здесь
    return False


def storage_information_view(request):
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(dict(who_entered=visit.passcard.owner_name,
                                      entered_at=visit.entered_at,
                                      duration=get_duration(visit.entered_at))
                                 )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
