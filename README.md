# Fronius-stats

[![MegaLinter](https://github.com/mdrocan/Fronius-stats/workflows/Linting/badge.svg?branch=main)](https://github.com/mdrocan/Fronius-stats/actions?query=workflow%3ALinting+branch%3Amain)

- Simple Python script that fetches data from a predefined Fronius inverter and visualizes the production.
- Displays: timestamp, current production and how much has been produced during the (day, year and total production) so far.

## Configure environment

- Use the [docker_compose.yml](docker_compose.yml) to start and setup your InfluxDB and Grafana environments.
- Launch the environment with, for example, `docker compose -f docker_compose.yml up -d`

### Setup InfluxDB

- Create a user with password, and a bucket to be used for saving the solar panel data.
- Create two APIs: 1) one for the Python script 2) one for Grafana. The script could have both read and write access rights, Grafana needs reading rights.

### Setup Grafana

- Create a data source connection to InfluxDB.
- Choose Flux as the query language.
- Setup the http-connection: `http://influxdb:8086`.
- Setup to InfuxDB Details section: organization, Token and Default Bucket.
- Save and Test.
- You should have now a working connection to your InfluxDB and can start making visualizations.

### Configuration settings

- By default the script uses a config file 'config.json', a template is [here](config.json.template).
- Update config.json file with the relevant information from InfluxDB setup, ie. token, org and bucket.

## Script execution

- Create a virtual environment

```code
python3 -m venv test_env
```

- Activate the environment

```code
source test_env/bin/activate
```

- Install the required packages

```code
pip install -r requirements.txt
```

- Setup the infrastructure, like defined in Chapter "Configure environment". Currently the setup uses Grafana and InfluxDB, which are running in separate Docker environments.

- Run in terminal the following command

```code
python3 fronius.py
```

- You should see something like this in the terminal:

```code
Time: 09:07:45
Currently producing: 75 W
Setup utilization: 2 %
```

or

```code
Time: 19:22:36
Not producing.
```

- You can also output the terminal output to a log file, for example:

```code
python3 fronius.py > fronius.log
```

and get to the log file something like this:

```code
Time: 19:20:00
Not producing.
```

- After script execution the data is fetched from the inverter and processed. In the terminal you will see a trimmed output and if everything is setup correctly you can find the same information from InfluxDB.

- If you don't wish to keep the virtual environment then deactivate it with the following command:

```code
deactivate
```

## Architecture

By default the script uses a config file 'config.json', a template is [here](config.json.template).

Currently there are two configurations you need to define in the Fronius part: URL and maximum capacity.
For the InfluxDB part you need to define: token, bucket and organization.

There's also a possibility to use a example response message in a Docker environment:

- The Dockerfile can be found from [here](web_server).
- Example message message [here](web_server/GetPowerFlowRealtimeData.fcgi).
- If you use the Docker environment the URL must be defined like your Docker environment has been
  started up. For example: `http://localhost:8080/GetPowerFlowRealtimeData.fcgi`.

## Development

Development activities happen in development branches.
Once the feature/fix/something is ready the change(s) are merged into main branch.

## Next steps

- Improve the documentation
- Use created sample visualizations in premade config
- Create more sample configs
- Further improvements to the the script by using also other Fronius API endpoints
