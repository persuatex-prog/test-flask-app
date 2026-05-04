

# Technical Plan: Simple Flask Hello API

## 1. Tech Stack Recommendation
To keep this solution free, simple, and maintainable, we will use the following stack:

*   **Language:** Python 3.10+ (Stable, widely supported)
*   **Backend Framework:** Flask (Lightweight, minimal boilerplate)
*   **Frontend:** None (This is a headless API)
*   **Database:** None (Stateless endpoint, no persistence required)
*   **Server:** Flask Development Server (for local), Gunicorn (recommended for production)
*   **Cost:** $0 (All open-source tools)

## 2. Complete Folder Structure
For a project of this size, a flat structure is preferred to avoid unnecessary complexity.

```text
/hello-api
├── .env                # Environment variables (local secrets/config)
├── .gitignore          # Git ignore rules
├── requirements.txt    # Python dependencies
├── app.py              # Main application entry point
└── README.md           # Documentation
```

## 3. Database Schema
**No database is required.**
This application is stateless. It does not store user data, logs, or messages. Introducing a database here would violate the principle of simplicity.

## 4. API Endpoints
There is one public endpoint.

### `GET /hello`
Returns a greeting message in JSON format.

*   **Request:**
    ```bash
    curl http://localhost:5000/hello
    ```
*   **Response (200 OK):**
    ```json
    {
      "message": "Hello, World!"
    }
    ```
*   **Headers:**
    *   `Content-Type: application/json`

## 5. Environment Variables Needed
These should be stored in a `.env` file locally and never committed to version control.

| Variable | Description | Default |
| :--- | :--- | :--- |
| `FLASK_APP` | Entry point file | `app.py` |
| `FLASK_ENV` | Runtime environment | `development` |
| `PORT` | Port number to run on | `5000` |
| `SECRET_KEY` | Flask secret key for sessions | (Random string) |

## 6. Dependencies List
Save this in `requirements.txt`.

```text
Flask==3.0.0
python-dotenv==1.0.0
```

## 7. Key Files Content

### `app.py`
```python
import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
```

### `.env`
```text
FLASK_APP=app.py
FLASK_ENV=development
PORT=5000
SECRET_KEY=change-this-in-production
```

### `.gitignore`
```text
__pycache__/
*.py[cod]
.env
venv/
.DS_Store
```

## 8. Setup Instructions

Follow these steps to get the application running locally.

### Prerequisites
*   Python 3.10 or higher installed.
*   `pip` (Python package manager) installed.

### Step 1: Create Project Directory
```bash
mkdir hello-api
cd hello-api
```

### Step 2: Create Virtual Environment
Isolate dependencies to avoid conflicts with system packages.
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment
*   **Windows:** `venv\Scripts\activate`
*   **Mac/Linux:** `source venv/bin/activate`

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Create Files
Create the files listed in **Section 7** (`app.py`, `.env`, `.gitignore`, `requirements.txt`) with the provided content.

### Step 6: Run the Application
```bash
python app.py
```

### Step 7: Test the Endpoint
Open your browser or terminal and visit:
```
http://localhost:5000/hello
```

## 9. Architect Notes & Next Steps
*   **Production Ready:** For production, do not use `python app.py`. Use a WSGI server like **Gunicorn**: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`.
*   **Security:** Ensure `SECRET_KEY` is a strong random string in production.
*   **Scalability:** If you need to add more endpoints later, refactor `app.py` into a package structure (`/app/routes`, `/app/__init__.py`). For now, the single-file approach reduces cognitive load.