# Fronius-stats

Simple Python script that fetches data from a predefined Fronius inverter.
Displays: timestamp, current production and how much has been produced during the (day, year) so far.

## Script execution
Execute in the terminal with the following command: 'python3 fronius.py'
After script execution the data is fetched from the inverter and trimmed.

## Architecture
By default it fetches the URL being used froma file called 'api.txt'.

There's also a possibility to use a example response message in a Docker environment.
In order to use the Docker web service you must edit the python source and comment/uncomment the necessary lines.
The Docker setup can be found from web_server-directory.


## Next steps

Save data to a database.
Visualize the data.