# Library Management App

A Library management app where users can register and borrow books from a catalogue. The admin can manage users, add or remove books, and view books borrowed by users, along with the return dates.

## Prerequisites

To run the app, ensure you have the following installed:

- **Python** (version 3.0 or higher)
- **Docker**

## Setup Instructions

After installing the prerequisites, follow these steps to get the app running:

### Step 1: Build and Start the Server

Run the following commands to build the Docker container and start the server:

```bash
docker-compose build
docker-compose up
```

### Step 2: Run Migrations

To run the necessary database migrations, use the following command:

```bash
docker-compose run web python manage.py migrate
```


### Step 3: Create a Superuser
To create a superuser (admin account), run:

```bash
docker-compose run web python manage.py createsuperuser
```


## Admin Endpoints

Once the app is running, you can access the admin interface using the following:

- **Admin URL:** http://localhost:8000/admin/
- Enter your superuser username and password to log in.
- The admin panel is GUI-based and easy to navigate.

## Admin Endpoints

The following frontend endpoints are available for users:

- **Register a new user:**: http://localhost:8000/create
- **View all users:** http://localhost:8000/users
- **View all books:** http://localhost:8000/books
- **View a book by ID:** http://localhost:8000/book/{book_id}
- **Filter books by publisher:** http://localhost:8000/books/publisher/{publisher_name}
- **Filter books by category:** http://localhost:8000/books/category/{category_name}
- **Borrow a book by ID:** http://localhost:8000/books/borrow/{book_id}

