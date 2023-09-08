# Fronius-stats

- Simple Python script that fetches data from a predefined Fronius inverter.
- Displays: timestamp, current production and how much has been produced during the (day, year) so far.

## Script execution

- Install the required package with 'pip install -r requirements.txt'
- Execute in the terminal with the following command: 'python3 fronius.py'
- After script execution the data is fetched from the inverter and trimmed.

## Architecture

By default it fetches the URL being used froma file called 'api.txt'.

There's also a possibility to use a example response message in a Docker environment:
- You must edit the Python source and comment/uncomment the necessary lines in the script.
- The Docker setup can be found from [here](web_server).
- Example message message [here](web_server/GetPowerFlowRealtimeData.fcgi).

## Next steps

Save data to a database.
Visualize the data.
