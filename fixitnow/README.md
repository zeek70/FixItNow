FixItNow - Domestic Services Marketplace API
   
About FixItNow
FixItNow is a comprehensive domestic services marketplace API that connects homeowners with skilled service providers. Similar to Fiverr but specifically designed for home services, it addresses the common challenges of finding reliable, fairly-priced domestic work including unpredictable pricing, unreliable providers, and lack of quality assurance.
Problems Solved
•	Transparent Pricing - Competitive marketplace pricing
•	Quality Assurance - Verified service providers and progress tracking
•	 Reliability - Structured booking and communication system
•	 Real-time Updates - Live job progress tracking
•	 Easy Discovery - Categorized services for quick finding
 
 Technology Stack
•	Backend Framework: Django 5.2.4
•	API Framework: Django REST Framework 3.16.0
•	Authentication: JWT (djangorestframework-simplejwt)
•	Database: SQLite (Development) / PostgreSQL (Production Ready)
•	Documentation: Swagger/OpenAPI
•	Python Version: 3.12+
 
Quick Start
Prerequisites
•	Python 3.12+
•	pip package manager
•	Git
Installation
1.	Clone the repository
2.	git clone https://github.com/yourusername/fixitnow.git
3.	cd fixitnow
4.	Create virtual environment
5.	python -m venv env
6.	source env/bin/activate  # On Windows: env\Scripts\activate
7.	Install dependencies
8.	pip install django djangorestframework djangorestframework-simplejwt
9.	Database setup
10.	python manage.py makemigrations
11.	python manage.py migrate
12.	python manage.py createsuperuser
13.	Run development server
14.	python manage.py runserver
15.	Access the application
o	Web Interface: http://127.0.0.1:8000/
o	API Documentation: http://127.0.0.1:8000/api/
 
API Documentation
Base URL
http://127.0.0.1:8000/
Authentication Endpoints
Method	Endpoint	Description	Authentication
POST	/accounts/api/signup/	Register new user	None
POST	/accounts/api/login/	User login	None
POST	/accounts/api/logout/	User logout	None
POST	/api/token/	Get JWT tokens	None
POST	/api/token/refresh/	Refresh JWT token	None
Sample Requests
User Registration:
curl -X POST http://127.0.0.1:8000/accounts/api/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepass123"
  }'
User Login:
curl -X POST http://127.0.0.1:8000/accounts/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepass123"
  }'
Core API Endpoints
Method	Endpoint	Description	Authentication
GET	/api/users/	List all users	Optional
POST	/api/users/	Create new user	Optional
GET	/api/users/{id}/	Get user details	Optional
PUT	/api/users/{id}/	Update user	Optional
DELETE	/api/users/{id}/	Delete user	Optional
Service Categories
Method	Endpoint	Description	Authentication
GET	/api/categories/	List all categories	Optional
POST	/api/categories/	Create new category	Optional
GET	/api/categories/{id}/	Get category details	Optional
PUT	/api/categories/{id}/	Update category	Optional
DELETE	/api/categories/{id}/	Delete category	Optional
Sample Request
curl -X POST http://127.0.0.1:8000/api/categories/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Emergency Plumbing",
    "description": "24/7 emergency plumbing services"
  }'
Service Requests
Method	Endpoint	Description	Authentication
GET	/api/service-requests/	List all service requests	Optional
POST	/api/service-requests/	Create new service request	Optional
GET	/api/service-requests/{id}/	Get service request details	Optional
PUT	/api/service-requests/{id}/	Update service request	Optional
DELETE	/api/service-requests/{id}/	Delete service request	Optional
POST	/service-requests/create/	Alternative create endpoint	Optional
Available Categories
•	plumbing - Plumbing services
•	gardening - Gardening and landscaping
•	electrical - Electrical installations and repairs
•	cleaning - House and office cleaning
•	painting - Interior and exterior painting
•	other - Miscellaneous services
Sample Request
curl -X POST http://127.0.0.1:8000/api/service-requests/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Kitchen Sink Leak Repair",
    "description": "Urgent repair needed for leaking kitchen sink causing water damage",
    "category": "plumbing",
    "status": "pending"
  }'
Service Updates
Method	Endpoint	Description	Authentication
GET	/api/service-updates/	List all service updates	Optional
POST	/api/service-updates/	Create new service update	Optional
GET	/api/service-updates/{id}/	Get service update details	Optional
PUT	/api/service-updates/{id}/	Update service update	Optional
DELETE	/api/service-updates/{id}/	Delete service update	Optional
Sample Request
curl -X POST http://127.0.0.1:8000/api/service-updates/ \
  -H "Content-Type: application/json" \
  -d '{
    "servicerequest": 1,
    "description": "Technician assigned: Mike Johnson. Scheduled for tomorrow 10 AM."
  }'
About Section
Method	Endpoint	Description	Authentication
GET	/api/about/	Get platform information	Optional
POST	/api/about/	Create about content	Optional
GET	/api/about/{id}/	Get specific about content	Optional
PUT	/api/about/{id}/	Update about content	Optional
DELETE	/api/about/{id}/	Delete about content	Optional
  Testing the API
Using cURL
Complete Test Flow:
# 1. Register user
curl -X POST http://127.0.0.1:8000/accounts/api/signup/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123"}'

# 2. Create category
curl -X POST http://127.0.0.1:8000/api/categories/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Plumbing", "description": "Professional plumbing services"}'

# 3. Create service request
curl -X POST http://127.0.0.1:8000/api/service-requests/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Bathroom Repair", "description": "Fix leaking tap", "category": "plumbing", "status": "pending"}'

# 4. List all service requests
curl -X GET http://127.0.0.1:8000/api/service-requests/

# 5. Create service update
curl -X POST http://127.0.0.1:8000/api/service-updates/ \
  -H "Content-Type: application/json" \
  -d '{"servicerequest": 1, "description": "Technician on the way"}'
Using Postman
1.	Import the provided collection
2.	Set base URL: http://127.0.0.1:8000
3.	Test endpoints in the recommended order above
 
📁 Project Structure
FixItNow/
├── fixitnow/                 # Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                     # Main app
│   ├── models.py            # ServiceRequest, Category, About models
│   ├── serializers.py       # DRF serializers
│   ├── api_views.py         # API endpoints
│   ├── views.py             # Traditional Django views
│   ├── urls.py              # Core app URLs
│   └── api_urls.py          # API router URLs
├── accounts/                 # Authentication app
│   ├── views.py             # Auth views
│   └── urls.py              # Auth URLs
├── templates/               # HTML templates
├── manage.py
└── requirements.txt
 
API Response Examples
Successful Service Request Creation
{
  "id": 1,
  "title": "Kitchen Sink Leak Repair",
  "description": "Urgent repair needed for leaking kitchen sink",
  "category": "plumbing",
  "status": "pending"
}
Error Response
{
  "title": ["This field is required."],
  "description": ["This field is required."]
}
 
 Key Features
•	Multi-Category Support: Plumbing, electrical, cleaning, gardening, painting, and more
•	Real-time Updates: Track service progress with timestamped updates
•	User Management: Complete user registration and profile system
•	RESTful Design: Clean, predictable API endpoints following REST principles
•	Flexible Architecture: Both traditional web views and modern API endpoints
•	Scalable Structure: Modular app design for easy feature expansion
 
Deployment
The application is production-ready and can be deployed to:
•	Heroku - Simple git-based deployment
•	DigitalOcean - VPS deployment with nginx
•	AWS EC2 - Cloud deployment
•	Railway - Modern deployment platform
 

