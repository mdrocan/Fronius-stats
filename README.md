# Fronius-stats

- Simple Python script that fetches data from a predefined Fronius inverter.
- Displays: timestamp, current production and how much has been produced during the (day, year) so far.

## Script execution

- Create a virtual environment with 'python3 -m venv test_env'
- Activate the environment with 'source test_env/bin/activate'
- Install the required package with 'pip install -r requirements.txt'
- Execute in the terminal with the following command: 'python3 fronius.py'
- After script execution the data is fetched from the inverter and trimmed as output.
- If you don't wish to keep the virtual environment then deactivate it with 'deactivate'.

## Architecture

By default the script uses a config file 'config.json', a template is [here](config.json.templete).
Currently there are two settings to be defined: URL and maximum capacity.

There's also a possibility to use a example response message in a Docker environment:

- The Dockerfile can be found from [here](web_server).
- Example message message [here](web_server/GetPowerFlowRealtimeData.fcgi).
- If you use the Docker environment the URL must be defined like your Docker environment has been
started up. For example: '<http://localhost:8080/GetPowerFlowRealtimeData.fcgi>'.

## Next steps

- Save the data to a database.
- Visualize the data.
