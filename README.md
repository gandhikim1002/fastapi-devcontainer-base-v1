
### directory structure
* project-name
  * app
    * src
      * domain
      * internal
      * routers
    * resources
    * test


### step command
* make directory
* add main.py
``` python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```

* code .
* >dev containers: add dev container configuration files
* add configuration to workspace
* python3 & postgreSQL
* 3.11-bullseye(default)
* modify Dockerfile
``` 
# ENV PYTHONUNBUFFERED 1
```
* pip install --upgrade pip

* pip install uvicorn
* pip install fastapi
* pip install sqlmodel
* pip install psycopg2
* pip install PyJWT
* pip install pydantic[email]
* requirements.txt.1
* 

