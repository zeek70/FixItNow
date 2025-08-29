API TEST ENDPOINTS AND TEST INPUTS
### 1. Signup
**POST** http://127.0.0.1:8000//api/signup  

{
  "username": "testuser",
  "password": "testpass123",
  "emial": "testemail@gamil.com"
}



### 2. Login (Get JWT Token)
**POST** http://127.0.0.1:8000/api/login/

{
  "username": "testuser",
  "password": "testpass123"
}



### 3. Users
http://127.0.0.1:8000/api/users/

[
  {"id": 1, "username": "admin"},
  {"id": 2, "username": "testuser"}
]
```

---

### 4. Categories
**GET** http://127.0.0.1:8000/api/categories/


[
  {"id": 1, "name": "Plumbing"},
  {"id": 2, "name": "Electrical"}
]


### 5. Service Requests
http://127.0.0.1:8000/api/service-requests/

[
  {
    "id": 1,
    "title": "Fix broken pipe",
    "description": "Kitchen pipe leaking",
    "category": "Plumbing",
    "created_by": "testuser"
  }
]
```


{
  "title": "Install ceiling fan",
  "description": "Living room ceiling fan installation",
  "category": "Electrical"
}
```

---

### 6. Service Updates
http://127.0.0.1:8000/api/service-updates/

[
  {
    "id": 1,
    "service_request": 1,
    "status": "In Progress",
    "updated_at": "2025-08-20T12:30:00Z"
  }
]


