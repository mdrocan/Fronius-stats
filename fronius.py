"""
Importing data from the Fronius device.
"""
import requests  # pylint: disable=import-error
from requests.exceptions import HTTPError  # pylint: disable=import-error
from numerize import numerize  # pylint: disable=import-error

with open("api.txt", "r", encoding="utf8") as file:
    URL = file.read().rstrip()

# URL = "http://localhost:8080/GetPowerFlowRealtimeData.fcgi"


def check_values():
    """
    Actual logic of getting the JSON file with data and analyzing parts of it.
    """
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        jsondata = response.json()

        print("Timestamp:", jsondata["Head"]["Timestamp"])

        currently = numerize.numerize(jsondata["Body"]["Data"]["Site"]["P_PV"], 2)
        print("Currently:", currently, "Wh")

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
