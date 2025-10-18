## Bookstore Backend

### Installation
```
pip install -r requirements.txt
```
### Set Up Database
```
python manage.py migrate
```
### then run server :
```
python manage.py runserver
```




## 🔑 Authentication

### **Register** 

* **URL:** `/api/auth/register/`
* **Метод:** `POST`
* **Headers:** `Content-Type: application/json`
* **Body:**

```json
{
  "username": "user1",
  "first_name": "Polina",
  "last_name": "Pavlenko",
  "email": "user1@example.com",
  "password1": "Password123",
  "password2": "Password123",
  "role": "customer"  
}
```

* **Response 201:**

```json
{
  "user": {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "first_name": "Polina",
    "last_name": "Pavlenko",
    "role": "customer"
  }
}
```

* **Response 400 :**

```json
{
  "password1": ["This field is required."],
  "password2": ["This field is required."]
}
```

---

### **Login** 

* **URL:** `/api/auth/login/`
* **Метод:** `POST`
* **Headers:** `Content-Type: application/json`
* **Body:**

```json
{
  "username": "user1",
  "password": "Password123"
}
```

* **Response 200 :**

```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "first_name": "Polina",
    "last_name": "Pavlenko",
    "role": "customer"
  },
  "tokens": {
    "access": "jwt-access-token",
    "refresh": "jwt-refresh-token"
  }
}
```

* **Response 401 :**

```json
{
  "error": "Invalid credentials"
}
```

---

### **Logout**

* **URL:** `/api/auth/logout/`
* **Method:** `POST`
* **Headers:** `Authorization: Bearer <access_token>`
* **Body:**

```json
{
  "refresh": "jwt-refresh-token"
}
```

* **Response 200:**

```json
{"message": "Logout successful"}
```

---

## 📖 Books

### **Get books list**

* **URL:** `/books/`
* **Метод:** `GET`
* **Headers:** `Authorization: Bearer <access_token>`
* **Response 200:**

```json
{
  "books": [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
  ]
}
```

**Body for removing:**

```json
{
  "remove": true,
  "product": 1
}
```

---

## ⚙️ Headers

* **Authorization:** `Bearer <access_token>` for secured endpoints
* **Content-Type:** `application/json` for POST/PUT.

---

## How to run tests:

* **Install dependencies(first time only):

```
pip install pytest pytest-django
```

* ** Run all tests
```
pytest
```
