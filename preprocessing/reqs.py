
import urllib2
import json
import config


def get_sensor_data(session_key, exec_id):
    route = str(exec_id) + "?session_key=" + session_key
    res = urllib2.urlopen(config.API_SENSORS_URL + route)
    res_string = res.read()
    res_dict = json.loads(res_string)
    data_dict = json.loads(res_dict["data"])
    return data_dict["data"]
