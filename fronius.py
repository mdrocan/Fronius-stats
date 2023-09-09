"""
Importing data from the Fronius device.
"""
import json  # pylint: disable=import-error
import requests  # pylint: disable=import-error
from requests.exceptions import HTTPError  # pylint: disable=import-error
from numerize import numerize  # pylint: disable=import-error

with open("config.json", "r", encoding="utf8") as config_file:
    config = json.load(config_file)

URL = config["fronius"]["url"]
MAX_C = config["fronius"]["max_capacity"]


def check_values():
    """
    Actual logic of getting the JSON file with data and analyzing parts of it.
    """
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        jsondata = response.json()

        print("Timestamp:", jsondata["Head"]["Timestamp"])

        currently = jsondata["Body"]["Data"]["Site"]["P_PV"]
        if currently is None:
            currently = 0
            print("Currently:", currently, "W")
            print("From max capacity:", "0%")
        else:
            percentage = currently / MAX_C * 100
            print("From max capacity:", round(percentage, 1), "%")

        today = numerize.numerize(jsondata["Body"]["Data"]["Site"]["E_Day"], 2)
        print("Today:", today, "Wh")

        year = numerize.numerize(jsondata["Body"]["Data"]["Site"]["E_Year"], 2)
        print("Year:", year, "Wh")

        total_produce = numerize.numerize(
            jsondata["Body"]["Data"]["Site"]["E_Total"], 2
        )  # noqa: E501
        print("Total:", total_produce, "Wh")

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:  # pylint: disable=broad-except
        print(f"Other error occurred: {err}")


if __name__ == "__main__":
    check_values()
