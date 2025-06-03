# Image Uploader Django Project

## Overview

This is a Django-based web application that allows users to upload images, view uploaded images in a gallery, and uses Tailwind CSS for modern styling. It also supports live browser reload during development.

---

## Features

- Image upload with form validation
- Gallery view of all uploaded images
- Success message after upload
- Tailwind CSS integration for styling
- Live browser reload with `django-browser-reload`
- Media file handling in development

---

## Project Structure

```
image_uploader/
├── manage.py
├── db.sqlite3
├── image_uploader/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── success.html
│   ├── tests.py
│   └── views.py
├── theme/
│   └── ... (Tailwind CSS app files)
├── media/
│   └── images/
├── static/
└── requirements.txt
```

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/HafizManfaz/project1.git
cd image_uploader
```

### 2. Create and Activate Virtual Environment

```sh
python -m venv django_venv
django_venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Tailwind CSS Setup

```sh
python manage.py tailwind init
python manage.py tailwind install
```

### 5. Apply Migrations

```sh
python manage.py migrate
```

### 6. Run the Development Server

```sh
python manage.py runserver
```

---

## Usage

- Visit `http://127.0.0.1:8000/` to access the image uploader.
- Upload images using the form.
- View uploaded images in the gallery below the form.
- After a successful upload, you will be redirected to a success page.

---

## Important Files

- **settings.py**: Django settings, Tailwind and media configuration.
- **urls.py**: URL routing, including media file serving in development.
- **models.py**: `Image` model with `photo` (ImageField) and `date`.
- **views.py**: Handles image upload and success page.
- **templates/myapp/**: Contains `base.html`, `home.html`, and `success.html`.
- **requirements.txt**: Python dependencies.

---

## Media & Static Files

- Uploaded images are stored in the `media/images/` directory.
- Static files are served from the `static/` directory.
- During development, media files are served automatically via Django.

---

## .gitignore

The project uses a `.gitignore` to exclude unnecessary files and folders, such as:
- Python cache files
- Virtual environments
- Node modules
- OS-specific files
- Only Django project files and essential folders are tracked

---

## Dependencies

Example `requirements.txt`:
```
Django>=5.2
django-tailwind
django-browser-reload
```
Generate your own with:
```sh
pip freeze > requirements.txt
```

---
## What I Learned

- How to set up a Django project and app structure.
- How to configure media and static files in Django.
- How to use Django models, forms, and views for file uploads.
- How to display uploaded images in a responsive grid using Tailwind CSS.
- How to integrate Tailwind CSS with Django using `django-tailwind`.
- How to use `django-browser-reload` for live reloading during development.
- How to use `.gitignore` to keep the repository clean and only track necessary project files.
- How to generate and use a `requirements.txt` for Python dependencies.
- How to organize templates and extend a base layout for consistent styling.

---

## License

This project is for educational/demo purposes.

---

## Author

Hafiz Manfaz Ali
