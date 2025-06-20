# RestaurantApi & UserApi

This repository contains two Django REST API projects:

- **RestaurantApi**: Manages restaurant listings, allowing users to like restaurants and menu items, or save menu items.
- **UserApi**: Handles user authentication, profile management, and password operations using JWT.

## RestaurantApi Endpoints

- `GET /restaurants/` — List all restaurants  
- `POST /restaurants/<id>/like/` — Like a restaurant  
- `POST /menu_items/<id>/like/` — Like a menu item  
- `POST /menu_items/<id>/save/` — Save a menu item  

## UserApi Endpoints

- `POST /register/` — Register a new user  
- `POST /login/` — Obtain JWT access and refresh tokens  
- `POST /refresh/` — Refresh JWT token  
- `GET /profile/` — Retrieve user profile (authenticated)  
- `POST /password_reset/` — Request password reset  
- `POST /password_reset/<uidb64>/<token>/` — Confirm password reset  
- `POST /change-password/` — Change user password  

## Setup Instructions

1. Clone the repository:  
   `git clone <repository-url>`  
2. Create and activate a virtual environment:  
   `python -m venv venv`  
   `source venv/bin/activate` (Windows: `venv\Scripts\activate`)  
3. Install dependencies:  
   `pip install -r requirements.txt`  
4. Run database migrations:  
   `python manage.py migrate`  
5. Start the development server:  
   `python manage.py runserver`  

## Notes

- Built with Django REST Framework and uses `djangorestframework-simplejwt` for JWT authentication.  
- Admin interface available at `/admin/`.  
- Uses SQLite as the default database (configurable).  

## Contributing

Feel free to fork, modify, and submit pull requests to enhance these APIs.

## License

This project is licensed under the MIT License.
