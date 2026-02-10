## How to Run This Project

Follow these steps to run the application on your local machine.

### Step 1: Clone the Repository

Open terminal or command prompt and run:


git clone https://github.com/YOUR-USERNAME/intelligent-todo-manager.git
cd intelligent-todo-manager

---

### Step 2: Install Backend Dependencies

Move into the backend folder:


cd backend


Install required Python packages:


pip install fastapi uvicorn sqlalchemy


---

### Step 3: Start the Backend Server

Run the FastAPI server:


python -m uvicorn main:app --reload


The backend will start at:


http://127.0.0.1:8000


Keep this terminal open.

---

### Step 4: Open the Frontend

Open a new window and navigate to the project folder.

Open this file in your browser:


frontend/index.html


You can double-click the file to open it.

---

### Step 5: Use the Application

* Add tasks
* Mark tasks as completed
* Delete tasks
* View daily productivity summary
