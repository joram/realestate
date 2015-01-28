#!/usr/bin/python
from __future__ import print_function
import os, json, time
import sys

from geopy import geocoders

g = geocoders.GoogleV3()
logfile = open("locations.csv", "w")

def get_files(folder):
    filenames = []
    for f in os.listdir(folder):
        f = os.path.join(folder, f)
        if os.path.isfile(f) and f.endswith(".json"):
            filenames.append(f)
        else:
            if os.path.isdir(f):
                filenames.extend(get_files(f))
    return filenames

already_found = []
base_dir = "/home/john/code/realestate/data"
json_files = get_files(base_dir)
for f in json_files:
    data = json.loads(open(f, 'r').read())
    if "Address" in data:
        location = data.get("Address")
        if location not in already_found:
            places = g.geocode("%s Victoria BC Canada" % location, exactly_one=False)
            place, (lat, lng) = places[0]
            logfile.write("%s, %.5f, %.5f\n" % (place.replace(",",""), lat, lng))
            logfile.flush()
            already_found.append(location)
            time.sleep(1)
            print('*', end="")
        else:
            print('.', end="")
    else:
        print('x', end="")
    sys.stdout.flush()