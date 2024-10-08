# Globant: Code Challenge  

Implement an ETL process that extracts data from a free fake [API](https://jsonplaceholder.typicode.com/), transforms it, and automatically loads it into BigQuery using Airflow. Utilize Agile methodologies, testing and version control tools.

# Table of Contents
- [Installation](#Installation)
- [Usage](#usage)
- [Features](#Features)
- [Troubleshoot](#Troubleshoot)
- [Contact](#Contact)
  

# Installation

Install all requiriments in a Python environment  using `pip`

# Usage

Create a folder named `DAGs` in the  **Airflow** directory containing the file `etl_dag.py` and its dependencies.

### Initialize Airflow Database:

```bash
airflow db init
```


### Start the Airflow Webserver:

```bash
airflow webserver --port 8080
```


Open a browser and go to localhost:8080 to access the Airflow UI.

### Start Airflow Scheduler:


![alt text](https://github.com/cristianBMJ/process_ETL/blob/main/Images/scheduler.png)

### Metrics

![alt text](https://github.com/cristianBMJ/process_ETL/blob/main/Images/metrics.png)



# Features

# Troubleshoots

# Contact

Cristian MB cristianj3006@gmail.com
    
