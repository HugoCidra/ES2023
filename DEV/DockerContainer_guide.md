## Requirements

* Install the [Docker App](https://www.docker.com/products/docker-desktop/)
   * If you do not want to use the Docker App, you will need [Docker Compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)

---
## Setup

Clone the repository: (if you have not done it yet)
``` bash
git clone git@gitlab.com:dei-uc/es2023/pl1.git
```

    
The files related to the containers setup are:
* [docker-compose.yml](./docker-compose.yml)
* [Dockerfile](./backend/Dockerfile)

---
## RUN
In order to run the application, you need to run the following command inside the DEV folder:\
```bash
docker compose up
```

This will start the containers and the application will be available at http://localhost:3000 (frontend) and http://localhost:5000 (backend)

To stop the containers, press Ctrl+C and then run the following command:
```bash
docker compose down
```


## More INFO
* This is the bare minimum to run the application.
* If you want to know more:
    - Check Filipe Rodrigues [repository](https://github.com/Curvu/project-setup) on how to set up the project using Docker:


