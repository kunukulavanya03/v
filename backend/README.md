## Getting Started

### Prerequisites

* Python 3.9+
* FastAPI
* SQLAlchemy
* PostgreSQL

### Installing

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Create a new file named `.env` and add the following variables:
    DATABASE_URL=sqlite:///app.db
    SECRET_KEY=dev-secret-key-change-in-production
4. Run the application using `uvicorn app.main:app --host 0.0.0.0 --port 8000`