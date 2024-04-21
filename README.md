
This is a simple Flask-based API for managing items with CRUD operations. The project includes an OpenAPI specification and is testable via Insomnia.

---

**Folder Structure**

mod10-pon1/
│
├── api/
│   ├── __init__.py
│   ├── app.py          # Main application file where the Flask app and routes are defined
│   └── resources/      # Directory for resource modules if using Flask-RESTful or similar
│       └── __init__.py
│
├── tests/
│   └── test_api.py     # Test scripts for the API
│
├── docs/
│   ├── openapi.yaml    # OpenAPI (Swagger) documentation
│   └── insomnia.json   # Insomnia collection for API testing
│
├── requirements.txt    # Python package dependencies
└── README.md           # Project overview and setup instructions

**Getting Started:**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

**Prerequisites:**

You will need Python installed on your system. The project is tested with Python 3.9. Make sure you have `pip` and `virtualenv` installed to handle Python packages.

**Installation:**

1. **Clone the Repository**

   Start by cloning the repository to your local machine:
   ```
   git clone https://github.com/danielquintaos/mod10-pon1
   cd mod10-pon1
   ```

2. **Set up a Python Virtual Environment (Optional but recommended)**

   To create a virtual environment, run:
   ```
   python3 -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Install all dependencies that are required for the project by running:
   ```
   pip install -r requirements.txt
   ```

**Running the API:**

1. **Start the Flask Application**

   You can start the server using:
   ```
   python api/app.py
   ```
   This will start the local development server on `http://localhost:5000/api`. The API endpoints can now be accessed through this URL.

**Testing the API:**

1. **Using Insomnia**

   Import the `insomnia.json` file located in the `docs/` directory into Insomnia to test the API endpoints.

2. **Using Swagger UI**

   If you integrate Swagger UI into your project, you can navigate to `http://localhost:5000/api/docs` (or the respective URL you configure) to view and interact with the API documentation.

**Shutting Down:**

To stop the server, use CTRL+C in your terminal. If you are using a virtual environment, deactivate it by running:
```
deactivate
```