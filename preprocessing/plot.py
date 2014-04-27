
# import numpy as np
import matplotlib.pyplot as plt
import config
import reqs
from flask import jsonify, redirect, url_for
import json


class Sensors:
    ACCEL = "accelerometer"
    GPS = "gps"


def plot_accelerometer(session_key, exec_id):
    fig = plt.figure("Accelerometer")
    ax = fig.add_subplot(111)
    ax.set_xlabel("Time")
    ax.set_ylabel("Force")

    xs = list()
    ys_x = list()
    ys_y = list()
    ys_z = list()

    try:
        s_data = reqs.get_sensor_data(session_key, exec_id)
    except:
        return None

    for s_event in s_data:
        if s_event["sensorType"] == Sensors.ACCEL:
            xs.append(s_event["timestamp"] / 100.0)
            ys_x.append(s_event["data"]["x"])
            ys_y.append(s_event["data"]["y"])
            ys_z.append(s_event["data"]["z"])

    ax.plot(xs, ys_x, "r+-")
    ax.plot(xs, ys_y, "b+-")
    ax.plot(xs, ys_z, "g+-")

    ax.legend(("X", "Y", "Z"))

    filename = config.IMG_FOLDER + session_key \
        + "_" + str(exec_id) + "_" + Sensors.ACCEL
    plt.savefig(filename)
    return filename + ".png"


@config.app.route(
    "/plots/<session_key>/<exec_id>/<sensor_type>",
    methods=["GET"]
)
def get_plot(session_key, exec_id, sensor_type):
    if sensor_type == Sensors.ACCEL:
        filename = plot_accelerometer(session_key, exec_id)
        if filename:
            return redirect("/" + filename)
        else:
            return jsonify(error="Bad parameters dude")


@config.app.route("/gps/<session_key>/<exec_id>", methods=["GET"])
def get_gps(session_key, exec_id):
    s_data = reqs.get_sensor_data(session_key, exec_id)
    gps_list = list()
    for s_event in s_data:
        if s_event["sensorType"] == Sensors.GPS:
            gps_dict = dict()
            gps_dict["latitude"] = s_event["data"]["latitude"]
            gps_dict["longitude"] = s_event["data"]["longitude"]
            gps_list.append(gps_dict)
    return json.dumps(gps_list)
