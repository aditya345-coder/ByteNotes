# ByteNotes

## 📌 Project Description
ByteNotes is a full-stack note-taking application built using **React** for the frontend and **Django** for the backend. It allows users to create, categorize, and manage notes under different categories such as Personal, Business, etc.

## 🚀 Demo
_Add a link or GIF showing the demo of your application._

---

## 📂 Folder Structure
```
|   .gitignore
|   LICENSE
|   README.md
|   requirements.txt
|   
+---bytenotes (Backend Root)
|   |   db.sqlite3  # Database file
|   |   manage.py   # Django project management file
|   |   
|   +---bytenotes (Django Project Settings)
|   |       asgi.py      # ASGI configuration
|   |       settings.py  # Django project settings
|   |       urls.py      # URL configuration
|   |       wsgi.py      # WSGI configuration
|   |       __init__.py  # Python package marker
|   |       
|   \---noteapp (Main App for Notes)
|       |   admin.py       # Django admin configuration
|       |   apps.py        # App configuration
|       |   models.py      # Database models
|       |   serializers.py # Data serialization for APIs
|       |   tests.py       # Test cases for the application
|       |   urls.py        # App-level URL configuration
|       |   views.py       # Business logic and API views
|       |   __init__.py    # Python package marker
|       |   
|       \---migrations     # Database migrations folder
|
\---frontend (React Frontend)
    |   .gitignore
    |   eslint.config.js  # ESLint configuration
    |   index.html        # Main HTML file
    |   package-lock.json # NPM dependency lock file
    |   package.json      # Project metadata and dependencies
    |   README.md         # Frontend-specific README
    |   vite.config.js    # Vite configuration for React
    |   
    +---public           # Public assets folder
    |       vite.svg     # Vite logo
    |       
    \---src (Source Files)
        |   App.jsx        # Main React component
        |   index.css      # Global styles
        |   main.jsx       # React root file
        |   
        +---assets        # Static assets (icons, images, etc.)
        |       react.svg
        |       
        +---components    # Reusable UI components
        |       Filter.jsx
        |       FormatDate.js
        |       Loader.jsx
        |       Modal.css
        |       Modal.jsx
        |       NavBar.jsx
        |       NoteCard.jsx
        |       NoteCardContainer.jsx
        |       
        +---layouts       # Layout components
        |       MainLayouts.jsx
        |       
        \---pages         # Main pages
                AddNote.css
                AddNote.jsx
                EditNote.jsx
                HomePage.jsx
                NoteDetail.css
                NoteDetail.jsx
```

---

## ⚙️ Installation & Setup

### 🖥️ Backend (Django)
1. Clone the repository:
   ```sh
   https://github.com/aditya345-coder/ByteNotes.git
   cd ByteNotes
   ```
2. Create a virtual environment:
   ```sh
   python -m virtualenv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```sh
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the backend server:
   ```sh
   python manage.py runserver
   ```

### 🌐 Frontend (React)
1. Navigate to the frontend folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend server:
   ```sh
   npm run dev
   ```

---

## 🛠️ Tech Stack
- **Frontend:** React, Vite, CSS, Bootstrap
- **Backend:** Django, Django REST Framework
- **Database:** SQLite 

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


