# Rapport ETL 


## 1. Contexte
*Ce projet est un ETL écrit en python*

Il permet d'extraire des données d'une source, de traiter les données et enfin de persister en base ou les envoyer vers un flux en streaming


### Prérequis
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Lancer la commande
   ```
   docker-compose up
   ```

2. Lancer les tests

   ```
   pytest .\tests\test_usecases_fuel_prices.py
   ```  


##  2. Choix technique et architecture

Dans ce projet, on met en place un pipeline de données qui se décompose en trois parties :
1. **L'extraction** : on obtient des données par appel à une API Web  
   
**Jeux de données**  
*prix-des-carburants-j-1*  
**Thèmes** : Transports, Déplacements  
**Mots clés** : Carburant, Prix, Voiture, Mobilité, Station service  
**Licence** : Licence Ouverte v1.0  
**Langue** : Français  
**Producteur** : Ministère de l'Economie, de l'Industrie et du Numérique

Le jeu de données est récupérée au format JSON

2. **La transformation** : on charge en mémoire les données pour les normaliser et les nettoyer.

Pour le jeu de données prix des carburants, on va mettre à plat les données, garder seulement les colonnes avec de l'information utile et changer le nom des colonnes.

3. **Le chargement** : cette étape consiste à persister les données dans une base de données postgreSQL (mode batch) ou envoyer un message contenant les données normalisées dans une queue RabbitMQ (streaming)

Afin de persister les données, j'ai choisi une base de données relationnelle posgtresSQL, car elle est adaptée à mon cas d'usage et possède des propriétés intéressantes (ACID).  

À chaque ajout de données (exécution du job) dans une table, on drop la table si elle déjà existante et on insert les nouvelles données.

À partir de cette étape, on peut récupérer les données normalisées sur la base de données posgtreSQL via une API (FastAPI) disponible sur
```
http://127.0.0.1:80/
```   
La documentation est disponible sur 
```   
http://127.0.0.1:80/docs  
```   
On peut aussi se connecter sur l'interface RabbitMQ pour visualiser les messages envoyés avec  
login=guest  
pwd=guest
```     
http://localhost:15672/
```   


## 3. Améliorations possibles

- Rajouter un script pour créer un schéma et une base de données au lancement du conteneur postgreSQL
- Orchestrer avec un cron le lancement du job
- Faire plus de tests et ajouter des tests d'intégrations

## 4. Références

* https://innerjoin.bit.io/making-a-simple-data-pipeline-part-1-the-etl-pattern-7ea52c0f3579

* https://github.com/jod35/Build-a-fastapi-and-postgreSQL-API-with-SQLAlchemy

* https://www.rabbitmq.com/tutorials/tutorial-one-python.html

* http://www.prix-carburants.gouv.fr/rubrique/opendata/