import urllib2
import json
import os

wunderground_key = os.environ.get("wunderground_key")

# f = urllib2.urlopen('http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/CA/San_Francisco.json')
# json_string = f.read()

# # turn the string into an object
# parsed_json = json.loads(json_string)

# location = parsed_json['location']['city']

# temp_f = parsed_json['current_observation']['temp_f']
# precip = parsed_json['current_observation']['precip_today_in']

# print "Current temperature in %s is: %s. Rain in inches: %s" % (location, temp_f, precip)

# f.close()


def get_weather():
    f = urllib2.urlopen('http://api.wunderground.com/api/' + wunderground_key + '/geolookup/conditions/q/CA/San_Francisco.json')
    json_string = f.read()

    # turn the string into an object
    parsed_json = json.loads(json_string)

    location = parsed_json['location']['city']

    temp_f = parsed_json['current_observation']['temp_f']
    precip = parsed_json['current_observation']['precip_today_in']

    msg = "Current temperature in %s is: %s. Rain in inches: %s" % (location, temp_f, precip)

    f.close()
    return msg

print get_weather()
