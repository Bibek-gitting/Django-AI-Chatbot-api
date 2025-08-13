# ​ Django AI Chatbot API

A RESTful AI chatbot API built with Django and Django REST Framework. Users can register, log in with token-based authentication, send messages to the AI (OpenRouter GPT-5 Nano), receive responses, and track token usage.

---

## ​ Features

- **User signup & login** using token authentication
- **Chat endpoint**: send a message to the AI and receive a response
- **Token deduction**: 100 tokens are charged per chat request
- No frontend – designed as a backend-only API

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
