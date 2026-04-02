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