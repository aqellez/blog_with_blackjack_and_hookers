Example of blog with articles on django 2.1.2

Included: searching, comments, syntax highlighting (CKEditor), forms for creating/editing articles,
user authentication system with login, logout, register forms.

How to:

1. Pull or clone this repo
2. Create virtual environment with virtualenv or python's command: \n
    "python(3) -m venv myenv"
3. Activate virtual environment: \n
    a) Win: "venv\Scripts\activate" \n
    b) Linux: "source venv/bin/activate"
4. Go to project root folder.
5. Run migrations: \n
    a) python(3) manage.py makemigrations \n
    b) python(3) manage.py migrate
6. Run server:
    "python(3) manage.py runserver (port)"
