# Finance Tracking API

A robust, clean, and maintainable backend system for managing and analyzing personal financial records. Built with Python and FastAPI, this project demonstrates structured application design, data validation, and business logic implementation.

## 🚀 Tech Stack
* **Framework:** FastAPI
* **Database:** SQLite (Chosen for zero-setup local evaluation)
* **ORM:** SQLAlchemy
* **Validation:** Pydantic

## ✨ Core Features
* **Financial Records Management:** Full CRUD operations for income and expense transactions.
* **Summary & Analytics:** Database-level aggregations calculating total income, total expenses, current balance, and dynamic category-wise breakdowns.
* **Data Validation:** Strict input validation ensuring positive amounts and correct transaction types.
* **Error Handling:** Graceful HTTP exceptions for unauthorized access, missing records, or invalid inputs.

## 🌟 Optional Enhancements Included
To make the application more robust and production-like, the following optional features from the assignment requirements have been implemented:
1. **Interactive API Documentation:** Automatically generated Swagger UI (`/docs`) and ReDoc (`/redoc`).
2. **Advanced Filtering:** Users can filter their transaction records by `transaction_type` (income/expense) and `category`.
3. **Pagination:** Implemented `skip` and `limit` parameters on list endpoints to handle large datasets efficiently.
4. **Role-Based Access Control (RBAC):** A simplified header-based authentication system implementing `Viewer`, `Analyst`, and `Admin` roles.

## 📁 Project Structure
```text
finance_backend/
├── app/
│   ├── main.py             # Application entry point
│   ├── database.py         # SQLite & SQLAlchemy engine setup
│   ├── models.py           # Database schema definition
│   ├── schemas.py          # Pydantic models for validation
│   ├── crud.py             # Reusable database interaction logic
│   ├── auth.py             # RBAC header dependencies
│   └── routers/            
│       ├── transactions.py # API endpoints for records
│       └── analytics.py    # API endpoints for financial summaries
├── requirements.txt        # Project dependencies
└── README.md

🛠️ Setup & Installation
1. Clone or extract the project directory and open your terminal inside the root folder.

2. Create and activate a virtual environment:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies:

Bash
pip install -r requirements.txt
4. Start the development server:

Bash
uvicorn app.main:app --reload
(The SQLite database finance.db will be created automatically upon starting the server).

🧪 How to Test the API
Instead of manual cURL commands, you can use the built-in interactive UI.

Open your browser and navigate to: http://127.0.0.1:8000/docs

Important - Authentication Headers: To test the endpoints, you must provide the following headers in the Swagger UI input form:

x-user-id: Any integer (e.g., 1) to simulate a logged-in user.

x-user-role: Must be one of viewer, analyst, or admin.

Role Permissions:

Admin: Can Create (POST), Read (GET), and Delete (DELETE) transactions, and view analytics.

Analyst: Can Read (GET) transactions and view analytics (GET).

Viewer: Can only Read (GET) transactions.
