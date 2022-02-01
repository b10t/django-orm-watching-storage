from django.utils import timezone
from django.utils.timezone import localtime


def is_visit_long(duration_visit, minutes=60):
    """Определяет, длинный или нет визит.

    Args:
        duration_visit (timedelta): Продолжительность визита
        minutes (int, optional): Лимит времени в минутах. Defaults to 60.

    Returns:
        boolean: Длинный или нет визит
    """
    return minutes <= duration_visit.seconds // 60


def get_duration(visit):
    """Расчитывает продолжительность по времени визита.

    Args:
        visit (Visit): Запись из таблицы Visit

    Returns:
        timedelta: Разница во времени
    """
    leaved_at = timezone.now()

    if leaved_at:
        leaved_at = visit.leaved_at

    return localtime(leaved_at) - localtime(visit.entered_at)


def format_duration(duration_visit):
    """Возвращает отформатированное время.

    Args:
        duration_visit (timedelta): Продолжительность по времени

    Returns:
        str: Отформатированное время
    """
    hours = duration_visit.seconds // 3600
    minutes = duration_visit.seconds % 3600 // 60
    return f'{hours}:{minutes}'
