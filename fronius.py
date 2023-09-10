"""
Importing data from the Fronius device.
"""
import json  # pylint: disable=import-error
import time  # pylint: disable=import-error
import requests  # pylint: disable=import-error
from requests.exceptions import HTTPError  # pylint: disable=import-error

with open("config.json", "r", encoding="utf8") as config_file:
    config = json.load(config_file)

URL = config["fronius"]["url"]
MAX_C = config["fronius"]["max_capacity"]
converted_MAX_C = int(MAX_C)

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


def check_values():
    """
    Actual logic of getting the JSON file with data and analyzing parts of it.
    """
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        jsondata = response.json()

        print("Time:", current_time)
        print("Response timestamp:", jsondata["Head"]["Timestamp"])

        currently = jsondata["Body"]["Data"]["Site"]["P_PV"]
        if currently == "None":
            currently = "0"
            print("Currently producing:", currently, "W")
            print("Setup utilization:", "0%")
        else:
            print("Currently producing:", currently, "W")
            percentage = currently / converted_MAX_C * 100
            print("Setup utilization:", round(percentage), "%")

        today = jsondata["Body"]["Data"]["Site"]["E_Day"]
        print("Today:", today, "Wh")

        year = jsondata["Body"]["Data"]["Site"]["E_Year"]
        print("Year:", year, "Wh")

        total_produce = jsondata["Body"]["Data"]["Site"]["E_Total"]  # noqa: E501
        print("Total:", total_produce, "Wh")

        data = {
            "currently": currently,
            "percentage": percentage,
            "today": today,
            "year": year,
            "total_produce": total_produce,
        }

        with open("data.json", "w", encoding="utf8") as outfile:
            json.dump(data, outfile, indent=4)

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:  # pylint: disable=broad-except
        print(f"Other error occurred: {err}")


if __name__ == "__main__":
    check_values()
