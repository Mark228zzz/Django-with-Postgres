# Django-with-Postgres

### Overview

This repository demonstrates how to set up and integrate a Django application with a PostgreSQL database. It includes configurations for Docker and Docker Compose to facilitate development and deployment.

<hr>

### Features

* Django Application: A sample Django project structured for scalability and maintainability.

* PostgreSQL Integration: Configuration and setup to use PostgreSQL as the database backend.

* Docker Support: Docker and Docker Compose configurations for containerized development and deployment.

* Environment Variables Management: Utilizes environment variables for configuration, enhancing security and flexibility.

<hr>

### Prerequisites

Ensure you have the following installed on your system:

* Python 3.x
* Docker
* Docker Compose

<hr>

### Setup Instructions

1. Clone the Repository:

```bash
git clone https://github.com/Mark228zzz/Django-with-Postgres.git
cd Django-with-Postgres
```

2. Environment Variables Configuration:

Create a .env file in the project root to define your environment-specific variables. For example:

```ini
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
```

Replace **your_db_name**, **your_db_user**, and **your_db_password** with your actual database credentials.

3. Build and Run with **Docker Compose**:

Ensure **Docker** and **Docker Compose** are running, then execute:

```bash
docker pull postgres
docker build -t web .
docker-compose up -d
```

This command builds the Docker images and starts the containers as defined in the docker-compose.yml file.

4. Access the Application:

The application should now be accessible at http://localhost:8000/. You can see **products** table from **PostgreSQL** database at http://localhost:8000/products/.
