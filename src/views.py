from django.shortcuts import render
from django.http import HttpResponse
from src.models import ClassList, Offerings, Days

# Create your views here.

def add_class(request):

    _crn = request.GET.get('crn', '')
    _name = request.GET.get('name', '')
    _title = request.GET.get('title', '')

    if _crn != '' and _name != '' and _title != '':  
        q = ClassList(crn=_crn, name=_name, title=_title)
        q.save()
        return HttpResponse(f'Success: crn={_crn}, name={_name}, title={_title}')     
    else:
        return HttpResponse(f'Failure: crn={_crn}, name={_name}, title={_title}')     


    

def print_class(request):

    _crn = request.GET.get('crn', '')

    html = '<p1> %s </p1>' % ClassList.objects.get(crn=_crn)

    return HttpResponse(html) 

def print_all_classes(request):

    response = ''

    classes = ClassList.objects.all()

    for _class in classes:
        response += f'[{_class.crn}]: name={_class.name}, title={_class.title}</br>'

    return HttpResponse(response)

def add_offering(request):

    _crn = request.GET.get('crn', '')

    _class = ClassList.objects.get(crn=_crn)

    offering = Offerings(crn=_class)

    offering.save()

    return HttpResponse(f'[{offering.id}]: crn={offering.crn}')


def print_days(request):

    response = ''

    _days = Days.objects.all()

    for __day in _days:
        response += f'[{__day.id}]: name={__day.abbrev}, text={__day.text}</br>'

    return HttpResponse(response)
    
