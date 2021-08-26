from django.shortcuts import render
from .logic.logic_measurements import *
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement(request, id):
    try:
        measurement = get_one_measurement(id)
        measurement_ans = serializers.serialize('json', [measurement])
        return HttpResponse(measurement_ans, content_type='application/json')
    except Exception as e:
        return HttpResponse('<html><body>Measurement pk=%s not found</body></html>' % id)

def delete_measurement(request, id):
    try:
        measurement = delete_one_measurement(id)
        return HttpResponse('<html><body>Measurement pk=%s deleted</body></html>' % id)
    except Exception as e:
        return HttpResponse('<html><body>Measurement pk=%s not found</body></html>' % id)


def update_measurement(request, id, value, unit, place):
    value = float(value)
    try:
        measurement = update_one_measurement(id, value, unit, place)
        measurement_ans = serializers.serialize('json', [measurement])
        return HttpResponse(measurement_ans, content_type='application/json')
    except Exception as e:
        return HttpResponse('<html><body>Measurement pk=%s not found</body></html>' % id)
