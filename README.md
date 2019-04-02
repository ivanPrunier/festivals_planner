# Festivals planner API

## Installation
`git clone git@github.com:ivanPrunier/festivals_planner_api.git`

`cd festivals_planner_api`

`docker-compose up --build`

The API is now accessible on `GET` [http://127.0.0.1:8005/api](http://127.0.0.1:8005/api)

You can then run `docker-compose exec api ./manage.py load_festivals` to scrap some festivals and populate your database.

The api docs can be found at [http://127.0.0.1:8005/docs](http://127.0.0.1:8005/docs)
