# FastAPI_Redis_word_counter
Python developer test task.

## Assignment
Application:

provides an endpoint of a file load

calculates the number of occurrences of the letter "X" in lines of text

saves the result in a database (Redis)

provides an endpoint to get the result from the database in the form of [{"datetime": "15.11.2023 15:00:25.001", "title": "Very fun book", "x_avg_count_in_line": 0.012}, {"datetime": "18.01.2023 12:00:25.001", "title": "Other very fun book", "x_avg_count_in_line": 0.032} ]

where x_avg_count_in_line is the average of the number of occurrences for each of the loaded texts

## Requirements
- Docker
  - [docker-compose](https://docs.docker.com/compose/install/)

## Run application
1. Build a docker container:
   ```docker-compose build```
2. Run the assembled docker container:
   ```docker-compose up -d```
3. Navigate to the http://localhost:8000/docs and execute test API call.

## Run application without Docker
**Requirements/dependencies**
- Python >= 3.10
   - poetry
- Redis instance
> The Redis service can be started with docker-compose -f docker-compose-services.yml up

**Install dependencies**
Execute the following command: ```poetry install```

**Run FastAPI app and Celery worker app**
1. Start the FastAPI web application with ```poetry run hypercorn app:create_app --reload```.
2. Navigate to the http://localhost:8000/docs and execute test API call.
