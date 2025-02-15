#  ETL  

## Architecture
The project architecture is based on a classic ETL pipeline with three main components:
- An extraction service that collects data from the Fuel Prices API
- A transformation service that cleans and normalizes data
- A loading service that stores data in PostgreSQL and streams via RabbitMQ

## 1. Context
*ETL (Extract, Transform, Load) project in Python for fuel price analysis.*

Features:
- Data extraction from API
- Data transformation and cleaning
- Storage in PostgreSQL or streaming via RabbitMQ
- Dashboard visualization

<div align="center">
  <img src="https://i.imgur.com/Yvk4T0Y.png" 
       width="500" 
       alt="dataviz"
       style="border: 2px solid #ddd; 
              border-radius: 8px; 
              box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
              margin: 20px 0">
</div>

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

```bash
# Launch services
docker-compose up
```  
```bash
# Run tests
pytest tests/test_usecases_fuel_prices.py
```

## 2. Project Structure
```
src/
├── api/         # REST API FastAPI
├── dataviz/     # Dashboard Visualization
└── etl/         # ETL Pipeline

tests/           # Unit tests
```

## 3. Technical Choices and Architecture

### Pipeline Structure
1. **Extraction** 
   - Source: Fuel Prices API
   - Format: JSON
   - Dataset: fuel-prices-d-1
   - Producer: Ministry of Economy

2. **Transformation**
   - Data normalization
   - Column cleaning
   - Data validation

3. **Loading**
   - PostgreSQL: persistent storage (ACID)
   - RabbitMQ: real-time streaming

### Available Services
| Service | URL | Access |
|---------|-----|--------|
| API | http://127.0.0.1:80/ | - |
| Documentation | http://127.0.0.1:80/docs | - |
| RabbitMQ | http://localhost:15672/ | guest/guest |

## 4. Possible Improvements

- [ ] PostgreSQL initialization script
- [ ] Cron orchestration
- [ ] Integration tests
- [ ] Monitoring and alerting
- [ ] Enhanced error handling

## 5. References

- [ETL Pattern](https://innerjoin.bit.io/making-a-simple-data-pipeline-part-1-the-etl-pattern-7ea52c0f3579)
- [FastAPI PostgreSQL](https://github.com/jod35/Build-a-fastapi-and-postgreSQL-API-with-SQLAlchemy)
- [RabbitMQ Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
- [Fuel Prices API](http://www.prix-carburants.gouv.fr/rubrique/opendata/)
