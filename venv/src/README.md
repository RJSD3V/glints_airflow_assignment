# Data Pipeline Project for Glints Interview Process.

The root folder needs to be ``` src```

If you just run the command 
```commandline
docker-compose up --build
```
The docker containers specified in the docker compose file will
start getting initialised as services based on the config specified.

In this case in some instances if the configurations clash the services might not run as exected,
but there has been an attempt made to configure the services perfectly. 

There are three services currently currently configured :-
- **postgres_x** : The input database X
- **postgres_y** : The output database Y (In a separate container)
- **webserver**  : The airflow webserver that can be used to connect the input X and output Y databases. 

Docker containers will be spun up for these mentioned services
and the first container (X) is programmed to create the input database and 
tables inside init files :
 - **init.sh** shell script : runs the psql command and grants rights to glints database.
 - **create_tables.sql** : sql script that creates the tables and inserts sample records


Inside the airflow server, the dag is located inside the dags folder. there is one dag that is created
with the following functions that support it: 

 - get_data() : gets data from running X docker container
 - push_data() : pushes data into running Y docker container
 - sentinel functions:
   - first_function_execute: Notify start of DAG
   - last_function_execute : Notify End of DAG
  
        



Note: This project has been prepared considering I have very little experience
with docker and airflow. 

