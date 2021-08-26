from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_one_measurement(id):
    measurement = Measurement.objects.get(pk=id)
    print(measurement)
    return measurement

def delete_one_measurement(id):
    Measurement.objects.get(pk=id).delete()

def update_one_measurement(id, value, unit, place):
    measurement = Measurement.objects.get(pk=id)
    measurement.value = value
    measurement.unit = unit
    measurement.place = place
    measurement.save()
    return measurement
