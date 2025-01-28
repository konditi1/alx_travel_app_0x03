

# ALX Travel App: Milestone 3 - API Development for Listings and Bookings

This project is part of the ALX ProDev program and focuses on developing API endpoints for managing listings and bookings in a travel application. 

## Project Objectives

- Build API views to manage `Listings` and `Bookings` using Django REST Framework.
- Implement CRUD operations for both models.
- Document all API endpoints using Swagger.
- Test the endpoints for functionality.

## Project Structure

```
alx_travel_app_0x01/
├── alx_travel_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── listings/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
└── README.md
```

## Features

1. **Listings API**:
   - Create, Read, Update, and Delete (CRUD) operations for travel listings.

2. **Bookings API**:
   - CRUD operations for managing bookings associated with listings.

3. **Swagger Integration**:
   - Automatically generated API documentation available at `/swagger/`.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx_travel_app_0x01.git
   cd alx_travel_app_0x01
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:
   - Create a `.env` file in the `alx_travel_app` directory with database credentials and other settings.

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Seed the database (optional):
   ```bash
   python manage.py seed
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the API documentation at:
   ```
   http://127.0.0.1:8000/swagger/
   ```

## Testing the API

Use a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to test the API endpoints:

- **Listings**: `/api/listings/`
- **Bookings**: `/api/bookings/`

## Other installations i made
- sudo apt-get install rabbitmq-server
- sudo systemctl enable rabbitmq-server
- sudo systemctl start rabbitmq-server

####  Install Required Libraries
- pip install celery
- pip install django-celery-results  **For tracking task results**
- pip install kombu  **Celery’s AMQP messaging library (used for RabbitMQ)**

## Configure RabbitMQ
#### Create a Virtual Host: This isolates tasks for your project.
 ``` 
   sudo rabbitmqctl add_vhost alx_vhost
```

### Add a User: Add a user for Celery to communicate with RabbitMQ.
```
   sudo rabbitmqctl add_user alx_user strongpassword
```
### Set Permissions: Grant the user permissions for the virtual host.
```
   sudo rabbitmqctl set_permissions -p alx_vhost alx_user ".*" ".*" ".*"
```
### Enable RabbitMQ Management Plugin
For easier management, enable the RabbitMQ Management UI:
```
   sudo rabbitmq-plugins enable rabbitmq_management
```