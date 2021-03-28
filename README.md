# Pika

![pika](readme-images/pika.jpg)

A sample django project

## Local development

1.  Create a virtual environment.
    ```bash
    python3 -m venv pika-venv
    source pika-venv/bin/activate
    ```

1.  Install packages.
    ```bash
    pip install -r requirements.txt
    ```
    
1.  Create the database.
    ```bash
    psql < create_databases.sql
    ```

1.  Run migrations.
    ```bash
    python manage.py migrate
    ```

1.  Run tests.
    ```bash
    python manage.py test
    ```

1.  Run a server.
    ```bash
    python manage.py runserver
    ```
