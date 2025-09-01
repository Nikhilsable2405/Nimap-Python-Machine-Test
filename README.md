# 📝 Machine Test - Django Project (Clients & Projects Management)

A **Django REST Framework** project for managing **Clients** and their **Projects** with user authentication.  

---

## 🚀 Features
- 🔐 User authentication (Login required)  
- 👥 CRUD for Clients  
- 📂 CRUD for Projects linked to Clients  
- 🎯 Role-based access: Users can only view their own projects  


---

## ⚙️ Installation

1. **Clone this repository or download the files**
   
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # For Linux/Mac
   source venv/bin/activate
   
   # For Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---


## 🔑 Login to Admin Panel

👉 http://127.0.0.1:8000/admin/

Login using the superuser credentials you created.

---


## 📌 API Endpoints
**Clients API**

- GET /clients/

- POST /clients/

**Projects API (linked to client)**

- POST /clients/<client_id>/projects/

- GET /projects/

---

## 🛠️ Tech Stack

- 🐍 Python 3.x  
- 🌐 Django 5.x  
- ⚡ Django REST Framework (DRF)  
- 🗄️ PostgreSQL (Database)  


---

## 👨‍💻 Author
- **Nikhil Sable**  
- GitHub: [Nikhilsable2405](https://github.com/Nikhilsable2405)
