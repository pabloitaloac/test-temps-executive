# Django Order Management API

A Django REST API for managing articles and orders, allowing CRUD operations on articles and orders. The API ensures proper validation and tax calculations for each order.

## Features

- Create, retrieve, update, and delete articles.
- Create, retrieve, update, and delete orders.
- Automatically calculate total price with and without tax for each order.
- Enforce quantity limits (min 1, max 999) on articles in an order.

## Tech Stack

- **Django** - Python web framework.
- **Django Rest Framework** - Toolkit for building Web APIs in Django.
- **MySQL** - Relational database used for data storage.
- **Docker** - Containerization of the application.

## Prerequisites

Make sure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To set up the app and run it using Docker, follow these steps:

### 1. Clone the Repository

git clone https://github.com/pabloitaloac/test-temps-executive.git
cd test-temps-executive


### 2. Build and Run the Application with Docker

docker-compose up --build


### 3. Access the Application

- The API will be accessible at http://localhost:8000/swagger/

## API Usage

### Endpoints

#### 1. Create a New Article

POST /articles/

Request Body:

{
  "reference": "ART001",
  "name": "Article 1",
  "description": "Description of article",
  "price_before_tax": 100.00,
  "tax_rate": 0.15
}

#### 2. Retrieve an Article

GET /articles/{id}/

#### 3. Update an Article

PUT /articles/{id}/

Request Body:

{
  "reference": "ART001",
  "name": "Updated Article",
  "description": "Updated description",
  "price_before_tax": 120.00,
  "tax_rate": 0.22
}

#### 4. Delete an Article

DELETE /articles/{id}/

#### 5. Create a New Order

POST /orders/

Request Body:

{
  "articles": [
    {
      "article_reference": "ART001",
      "quantity": 10
    },
    {
      "article_reference": "ART002",
      "quantity": 5
    }
  ]
}

#### 6. Retrieve an Order

GET /orders/{id}/

#### 7. Update an Order

PUT /orders/{id}/

Request Body:

{
  "articles": [
    {
      "article_reference": "ART001",
      "quantity": 5
    }
  ]
}


#### 8. Delete an Order

DELETE /orders/{id}/
