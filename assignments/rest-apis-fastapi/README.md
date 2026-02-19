# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework that handles basic CRUD operations for a resource, such as managing a list of items. Skills practiced: API design, HTTP methods, data models, asynchronous programming.

## 📝 Tasks

### 🛠️ Implement REST API Endpoints

#### Description
Create a FastAPI application with endpoints to perform CRUD operations on a simple resource (e.g., items with id, name, description).

#### Requirements
Completed program should:

- Have a GET endpoint to retrieve all items
- Have a GET endpoint to retrieve a single item by ID
- Have a POST endpoint to create a new item
- Have a PUT endpoint to update an existing item
- Have a DELETE endpoint to remove an item
- Use Pydantic models for request/response validation
- Handle errors appropriately (e.g., 404 for not found)
- Run the server and test the endpoints