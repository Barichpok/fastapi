# fastapi
Test project for learning FastAPI

# To get started
* Open the terminal and navigate to the root directory of the project.

* Check that the .env file has POSTGRES_HOST=postgres_container set.

* Run `make start` to launch it in Docker:
  * http://127.0.0.1:5050/ - pgAdmin 4
  * http://127.0.0.1:8000/ - live server
  * http://127.0.0.1:8000/docs - automatic interactive API documentation (provided by Swagger UI)
  * http://127.0.0.1:8000/redoc - alternative automatic documentation (provided by ReDoc)

Alternatively, if you prefer to run it locally, execute the following commands:
  * In the .env file, change POSTGRES_HOST=postgres_container to POSTGRES_HOST=127.0.0.1
  * Run `start-dev` to launch Docker without the "fastapi_app" application.
  * Apply the latest database schema changes to our database.

    `alembic upgrade head`

  * Let's create a virtual environment:

    `python3 -m venv fastapi_venv`

  * Activate the virtual environment by running the command:

    `source fastapi_venv/bin/activate`

  * Install the dependencies from the requirements.txt file:

    `pip install -r requirements.txt`

  * Run `make server` to start the live server.