# Simple Customer Order Service

This project is a simple implementation of a service using Python, designed to manage customers and their orders. It features a REST API to handle data operations, utilizes PostgreSQL for data storage, and implements OpenID Connect for authentication and authorization. Notifications are sent to customers via SMS using the Africa’s Talking SMS gateway whenever an order is placed.

## System Requirements
Python 3.8 or newer
PostgreSQL
Docker and Docker Compose (optional for containerization)
An Africa’s Talking account for SMS notifications

## Getting Started
### Clone the Repository

git clone https://github.com/yourusername/simple-customer-order-service.git
cd simple-customer-order-service

### Set Up the Environment
Set up a Python virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate
Install the required dependencies:


pip install -r requirements.txt

### Configure the Application
Create a .env file in the root directory and update it with the necessary configurations:


DATABASE_URL=postgresql://username:password@localhost:5432/customerdb
AFRICASTALKING_API_KEY='YourAfrica'sTalkingApiKey'
AFRICASTALKING_USERNAME='YourUsername'
SMS_SENDER_ID='YourSenderId'

### Database Setup
Run the following command to create the database tables:

python manage.py migrate
### Run the Server
Start the local server using:


python manage.py runserver
### API Usage
#### Endpoints

POST /api/customers/ - Create a new customer.
Request Body:
json
Copy code
{
  "name": "John Doe",
  "code": "CUST001"
}
POST /api/orders/ - Create a new order.
Request Body:
json
Copy code
{
  "customer_id": 1,
  "item": "Laptop",
  "amount": 1500,
  "time": "2024-04-29T12:00:00Z"
}
#### Authentication
The API uses OpenID Connect for authentication. Ensure to send a valid token in the Authorization header:

plaintext
Copy code
Authorization: Bearer YourAccessToken

#### Testing
To run tests and check coverage:

bash
Copy code
pytest --cov=app

#### Continuous Integration and Deployment
CI/CD is handled using GitHub Actions. Upon pushing code to the repository, GitHub Actions will automatically run the tests and, if successful, deploy the code to the configured PaaS/IaaS/FaaS.

#### Further Documentation
For more details, refer to the individual files and code comments within the project repository.