from django.shortcuts import render_to_response
from django.conf import settings

def locations():
    filepath = '%s/locations.csv' % settings.ROOT_PATH
    f = open(filepath, 'r')
    locations = []
    for line in f.readlines():
        try:
            print line
            s = line.split(',')
            print s
            (name, lat, lng) = s
            locations.append({'name': name, 'lat': lat, 'lng':lng})
        except Exception as e:
            print e
            pass
    return locations

def map(request):

    context = {
        'locations': locations()
    }
    print context
    return render_to_response('map.html', context)
