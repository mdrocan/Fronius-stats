"""
Import data from the Fronius inverter and write the data into InfluxDB.
"""
import json  # pylint: disable=import-error
import time  # pylint: disable=import-error
import requests  # pylint: disable=import-error
from influxdb_client import (
    InfluxDBClient,
)  # pylint: disable=import-error
from influxdb_client.client.write_api import SYNCHRONOUS  # pylint: disable=import-error
from requests.exceptions import HTTPError  # pylint: disable=import-error


def check_values():
    """
    Actual logic of getting the JSON file with data and analyzing parts of it.
    """

    try:
        with open("config.json", "r", encoding="utf8") as config_file:
            config = json.load(config_file)

        url = config["fronius"]["url"]
        converted_max_c = int(config["fronius"]["max_capacity"])

        current_time = time.strftime("%H:%M:%S", time.localtime())
        print("Time:", current_time)

        response = requests.get(url, timeout=5)
        response.raise_for_status()
        jsondata = response.json()

        currently = jsondata["Body"]["Data"]["Site"]["P_PV"]

        if currently is None:
            print("Not producing.")
            currently = 0
            percentage = 0
        else:
            print("Currently producing:", round(currently), "W")
            percentage = round(currently / converted_max_c * 100)
            print("Setup utilization:", round(percentage), "%")

        timestamp = jsondata["Head"]["Timestamp"]
        today = round(jsondata["Body"]["Data"]["Site"]["E_Day"])
        year = round(jsondata["Body"]["Data"]["Site"]["E_Year"])
        total_produce = round(jsondata["Body"]["Data"]["Site"]["E_Total"])  # noqa: E501

        data = [
            {
                "measurement": "fronius",
                "time": timestamp,
                "fields": {
                    "currently": round(currently),
                    "percentage": round(percentage),
                    "today": round(today),
                    "year": round(year),
                    "total_produce": round(total_produce),
                },
            }
        ]

        with open("data.json", "w", encoding="utf8") as outfile:
            json.dump(data, outfile, indent=4)

        bucket = config["influxdb"]["bucket"]
        org = config["influxdb"]["org"]

        client = InfluxDBClient(
            url=config["influxdb"]["url"], token=config["influxdb"]["token"], org=org
        )

        # print(data)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=bucket, org=org, record=data)

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")


if __name__ == "__main__":
    check_values()
