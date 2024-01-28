# FastAPI_Redis_word_counter
Python developer test task.

## Assignment
Application:

provides an endpoint of a file load

calculates the number of occurrences of the letter "X" in lines of text

saves the result in a database (Redis)

provides an endpoint to get the result from the database in the form of [{"datetime": "15.11.2023 15:00:25.001", "title": "Very fun book", "x_avg_count_in_line": 0.012}, {"datetime": "18.01.2023 12:00:25.001", "title": "Other very fun book", "x_avg_count_in_line": 0.032} ]

where x_avg_count_in_line is the average of the number of occurrences for each of the loaded texts

## Run application
0. Install Poetry:
   ```
   pip install poetry
   ```
1.  Go to the ./app working directory and run ```poetry install```
2.  Launch the application using the command
   ```poetry run uvicorn app:create_app --host 0.0.0.0 --port 8000```
## Endpoints for interacting with the API
- /api/v1/files
- /api/v1/load
