# fastapi
Test project for learning FastAPI

# To get started
* Open the terminal and navigate to the root directory of the project.

* Run the following command:

`python3 -m venv fastapi_venv`

* Activate the virtual environment by running the command:

`source fastapi_venv/bin/activate`

* Install the dependencies from the requirements.txt file:

`pip install -r requirements.txt`

* Run the live server:
    * `uvicorn main:my_api --reload`
      * http://127.0.0.1:8000/
      * http://127.0.0.1:8000/docs - automatic interactive API documentation (provided by Swagger UI)
      * http://127.0.0.1:8000/redoc - alternative automatic documentation (provided by ReDoc)
