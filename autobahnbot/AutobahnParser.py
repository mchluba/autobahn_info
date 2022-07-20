import requests
import json

class AutobahnParser():
    def __init__(self):
        self.api_uri = "https://verkehr.autobahn.de/o/autobahn/"

    def get_warnings(self, autobahn, ort1, ort2):
        module = "/services/warning"
        api_module_uri = self.api_uri + autobahn + module
        warnings = json.loads(requests.get(url=api_module_uri).text)["warning"]
        warning_list = []
        for element in warnings:
            warning_string = " ".join(element["description"])
            if ort1 in warning_string and ort2 in warning_string:
                warning_dict = {
                    "external_id" : element["identifier"],
                    "highway" : autobahn,
                    "location_lat" : element["coordinate"]["lat"],
                    "location_long" : element["coordinate"]["long"],
                    "timestamp" : element["startTimestamp"],
                    "isblocked" : element["isBlocked"],
                    "description" : " ".join(element["description"]),
                    "routea" : element["subtitle"].split(" ")[0],
                    "routeb" : element["subtitle"].split(" ")[2]
                }
                warning_list.append(warning_dict)
        return warning_list
