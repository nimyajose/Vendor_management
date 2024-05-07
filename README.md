# vendor_management_system
This is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, purchase order tracking, and vendor performance evaluation.

Setup Instructions
Clone the repository to your local machine:
git clone https://github.com/your-username/vendor-management-system.git

Navigate to the project directory:
cd vendor-management-system

Create a virtual environment:
python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS and Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

The project should now be running locally on http://127.0.0.1:8000/.

API Endpoints

Purchase Orders
List Purchase Orders: GET /api/purchase_orders/
Retrieve Purchase Order: GET /api/purchase_orders/<pk>/
Create Purchase Order: POST /api/purchase_orders/create/
Update Purchase Order: PUT /api/purchase_orders/<pk>/
Delete Purchase Order: DELETE /api/purchase_orders/<pk>/
Acknowledge Purchase Order: POST /api/purchase_orders/<pk>/acknowledge/

Vendors
List Vendors: GET /api/vendors/
Retrieve Vendor: GET /api/vendors/<pk>/
Create Vendor: POST /api/vendors/create/
Update Vendor: PUT /api/vendors/<pk>/
Delete Vendor: DELETE /api/vendors/<pk>/
Vendor Performance Metrics: GET /api/vendors/<pk>/performance/

Usage
Use the provided API endpoints to interact with the Vendor Management System.
Make HTTP requests using tools like cURL, Postman, or your preferred programming language's HTTP library.
Refer to the API documentation above for details on each endpoint.
