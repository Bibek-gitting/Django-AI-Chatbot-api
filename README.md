# ​ Django AI Chatbot API

A RESTful AI chatbot API built with Django and Django REST Framework. Users can register, log in with token-based authentication, send messages to the AI (OpenRouter GPT-5 Nano), receive responses, and track token usage.

---

**✨ Features**
------------

1. **User Registration**: Users can register with the chatbot using a unique username and password.
2. **User Login**: Users can login to the chatbot using their registered username and password.
3. **Chat Functionality**: Users can interact with the chatbot by sending messages, and the chatbot will respond with a pre-defined message.
4. **Token Balance**: Users can check their token balance, which is used to track the number of messages they can send.
5. **Admin Interface**: Administrators can view and manage user accounts, chat logs, and token balances.
6. **RESTful APIs**: The project uses RESTful APIs for communication between the client and server.
7. **Django Framework**: The project is built using Django, a high-level Python web framework.
8. **Security**: The project includes basic security features such as password hashing and token validation.

---

## ​ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Bibek-gitting/Django-AI-Chatbot-api.git
   cd Django-AI-Chatbot-api
2. **Create & activate virtual environment**
   ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS / Linux
    python -m venv venv
    source venv/bin/activate
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    
4.  **Configure environment variables**
    Create a .env file in the project root:
    ```env
    SECRET_KEY=your_django_secret_key
    OPENROUTER_API_KEY=your_openrouter_api_key
    
5. **Apply migrations**
   ```bash
    python manage.py migrate
   
6.  **Create a superuser (optional)**
    ```bash
    python manage.py createsuperuser
    
7.  **Run the development server**

    ```bash
    python manage.py runserver

---

**🧰 Tech Stack Table**
----------------------

| Frontend | Backend | Tools |
| --- | --- | --- |
| HTML/CSS/JS | Django | Python 3.9 |
| RESTful APIs | Django REST framework | SQLite |
| JavaScript |  |  |
|  |  |  |

---

**📁 Project Structure**
----------------------

```bash
chatbot/
  chatbot/
    asgi.py
    wsgi.py
    settings.py
    urls.py
    __init__.py
  api/
    urls.py
    views.py
    models.py
    serializers.py
    admin.py
    apps.py
    __init__.py
    tests.py
  requirements.txt
  manage.py
```

---

**🧪 Testing Instructions**
-------------------------

1. **Unit Tests**: Run `python manage.py test` to run the unit tests.
2. **Integration Tests**: Run `python manage.py test --integration` to run the integration tests.

**📸 Screenshots**
----------------

[Insert screenshots of the project in action]

**📦 API Reference**
---------------------

[Insert API reference documentation or a link to it]

**👤 Author**
------------

[Your Name]

**📝 License**
------------

The Chatbot project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
