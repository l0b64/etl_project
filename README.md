#  ETL  

## Architecture
![architecture](https://i.imgur.com/Kn2j3IC.jpg)

## 1. Context
*This is an ETL (Extract, Transform, Load) project written in Python.*

It allows data extraction from a source, processing, and finally persisting it in a database or sending it to a streaming flow.


### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Run the command
   ```
   docker-compose up
   ```

2. Run the tests

   ```
   pytest .\tests\test_usecases_fuel_prices.py
   ```  


##  2. Choix technique et architecture

In this project, we implement a data pipeline that is divided into three parts:
1. **Extraction** : We retrieve data by making a call to a Web API.

**Dataset**   
*prix-des-carburants-j-1*  
**Themes** : Transport, Travel  
**Keywords** : Fuel, Price, Car, Mobility, Service station 
**License** : Open License v1.0  
**Language** : French  
**Producer** : Ministry of Economy, Industry, and Digital

The dataset is retrieved in JSON format.

2. **Transformation** : We load the data into memory to normalize and clean it.

For the fuel price dataset, we flatten the data, keep only the columns with useful information, and change the column names.

3. **Loading** : This step involves persisting the data in a PostgreSQL database (batch mode) or sending a message containing the normalized data to a RabbitMQ queue (streaming).

To persist the data, we chose a PostgreSQL relational database because it is suitable for our use case and has interesting properties (ACID).

For each data addition (job execution) in a table, we drop the table if it already exists and insert the new data.

Starting from this step, we can retrieve the normalized data on the PostgreSQL database via a FastAPI API available at
```
http://127.0.0.1:80/
```   
The documentation is available at
```   
http://127.0.0.1:80/docs  
```   
We can also connect to the RabbitMQ interface to visualize the messages with   
`login=guest`  
`pwd=guest`  
```     
http://localhost:15672/
```   


## 3. Possible improvements

- Add a script to create a schema and a database when launching the PostgreSQL container
- Orchestrate job execution with a cron
- Add more tests and integration tests

## 4. References

* https://innerjoin.bit.io/making-a-simple-data-pipeline-part-1-the-etl-pattern-7ea52c0f3579

* https://github.com/jod35/Build-a-fastapi-and-postgreSQL-API-with-SQLAlchemy

* https://www.rabbitmq.com/tutorials/tutorial-one-python.html

* http://www.prix-carburants.gouv.fr/rubrique/opendata/
