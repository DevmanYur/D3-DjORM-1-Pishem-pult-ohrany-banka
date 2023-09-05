import django
import datetime


def is_visit_long(v):
    minutes = 60
    sec_limit = minutes*60
    entered_at_local = django.utils.timezone.localtime(v.entered_at)
    if v.leaved_at != None:
        leaved_at_local =  django.utils.timezone.localtime(v.leaved_at)
        delta = leaved_at_local - entered_at_local
        total_seconds = delta.total_seconds()
        return (total_seconds > sec_limit)
    else:
        now_local = django.utils.timezone.localtime()
        delta = now_local - entered_at_local
        total_seconds = delta.total_seconds()        
        return (total_seconds > sec_limit)


def get_format_entered_at(x):
    v = django.utils.timezone.localtime(x.entered_at)
    vol_datetime = datetime.datetime(v.year, v.month, v.day, v.hour, v.minute, v.second)
    vol_format = vol_datetime.strftime("%d-%m-%Y %H:%M") 
    return vol_format


def get_format_duration(x):
    entered_at_local = django.utils.timezone.localtime(x.entered_at)
    if x.leaved_at != None:
        leaved_at_local =  django.utils.timezone.localtime(x.leaved_at)
        return get_hour_min(entered_at_local, leaved_at_local)
    else:
        now_local = django.utils.timezone.localtime()
        return get_hour_min(entered_at_local, now_local)


def get_hour_min(t1,t2):
    delta = t2 - t1
    total_seconds = delta.total_seconds()
    hour = int(total_seconds // 3600)
    min = int((total_seconds % 3600) // 60)
    hour_min = "%02d:%02d" % (hour, min)
    return hour_min