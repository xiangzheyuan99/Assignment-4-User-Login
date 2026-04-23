# Assignment-4-User-Login

# MongoDB Login App (FastAPI + Beanie)

## Project Overview

This project implements a simple user authentication system using **FastAPI** and **MongoDB (Atlas)**.
It demonstrates how to persist data using MongoDB instead of in-memory storage and implements basic user login functionality.

<img width="1123" height="632" alt="interface" src="https://github.com/user-attachments/assets/2a16c664-4113-4ea7-b236-8004ff8c127a" />


<img width="1216" height="527" alt="Database" src="https://github.com/user-attachments/assets/1efb0ab8-8b94-4026-92c0-eb288d3954dc" />


## Technologies Used

* Python
* FastAPI
* MongoDB Atlas
* Beanie (ODM)
* PyMongo (AsyncMongoClient)
* Uvicorn

## Project Structure
```
project/
├── main.py
├── database/
│   └── connection.py
├── models/
│   └── user.py
├── routes/
│   └── users.py
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions


### 1. Configure environment variables

Create a `.env` file in the root directory:

```env
MONGODB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/login_app_db?retryWrites=true&w=majority
SECRET_KEY=your_secret_key
```

---

### 2. Run the application

```bash
python -m uvicorn main:app --reload
```

---

### 3. Open API docs

Go to:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Features

### User Authentication APIs

#### 1. Sign Up

```
POST /user/signup
```

* Creates a new user
* Stores user data in MongoDB
* Prevents duplicate username/email

---

#### 2. Sign In

```
POST /user/signin
```

* Validates username and password
* Returns user info if successful

---

#### 3. Sign Out

```
POST /user/signout
```

* Returns a success message

---

#### 4. Dashboard

```
GET /dashboard
```

* Simple test route

---

## 🗄️ Database

* Database: `login_app_db`
* Collection: `users`

Each user document contains:

```json
{
  "_id": "...",
  "email": "...",
  "username": "...",
  "password": "..."
}
```
