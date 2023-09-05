import django
import datetime


def is_visit_long(value):
    minutes = 60
    sec_limit = minutes*60
    entered_at_local = django.utils.timezone.localtime(value.entered_at)
    if value.leaved_at :
        leaved_at_local =  django.utils.timezone.localtime(value.leaved_at)
        delta = leaved_at_local - entered_at_local
        total_seconds = delta.total_seconds()
        return (total_seconds > sec_limit)
    else:
        now_local = django.utils.timezone.localtime()
        delta = now_local - entered_at_local
        total_seconds = delta.total_seconds()        
        return (total_seconds > sec_limit)


def get_format_entered_at(value):
    local_time = django.utils.timezone.localtime(value.entered_at)
    vol_datetime = datetime.datetime(local_time.year, local_time.month, local_time.day, local_time.hour, local_time.minute, local_time.second)
    vol_format = vol_datetime.strftime("%d-%m-%Y %H:%M") 
    return vol_format


def get_format_duration(value):
    entered_at_local = django.utils.timezone.localtime(value.entered_at)
    if value.leaved_at :
        leaved_at_local =  django.utils.timezone.localtime(value.leaved_at)
        return get_hour_min(entered_at_local, leaved_at_local)
    else:
        now_local = django.utils.timezone.localtime()
        return get_hour_min(entered_at_local, now_local)


def get_hour_min(time_old,time_new):
    delta = time_new - time_old
    total_seconds = delta.total_seconds()
    hour = int(total_seconds // 3600)
    min = int((total_seconds % 3600) // 60)
    hour_min = "%02d:%02d" % (hour, min)
    return hour_min