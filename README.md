# 📌 Flask User Management REST API

A simple REST API built with **Flask** to manage user data in memory.  
Supports **CRUD** operations and is perfect for learning basic API development fundamentals.

---

## 🚀 Features
- **POST `/users`** → Create a new user
- **GET `/users`** → Retrieve all users
- **PUT `/users/<id>`** → Update an existing user
- **DELETE `/users/<id>`** → Remove a user

---

## 🛠 Tech Stack
- Python 3
- Flask
- Postman or curl for testing

---

## 📌 Sample API Output
```bash
Request Body
{
  "name": "John Doe",
  "email": "john@example.com"
}
Response
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
Response
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
]
Request Body
{
  "name": "Johnny Doe"
}
Response
{
  "id": 1,
  "name": "Johnny Doe",
  "email": "john@example.com"
}
Response
{
  "message": "User deleted successfully"
}

