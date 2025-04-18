# SHL Assessment Recommender System

This project is a web-based SHL assessment recommender tool that suggests appropriate assessments based on job descriptions or queries. It includes a **Flask backend API** and an **HTML/JS frontend interface**.

---
🌐 Live URLs

- 🔗 **Frontend**: [https://your-frontend-url.com](https://your-frontend-url.com)
- 🔗 **Backend (API)**: [https://your-backend-url.com](https://your-backend-url.com)

> Replace the above URLs with your actual deployed URLs once available.

---

## 📁 Project Structure

shl.com/ ├── backend/ │ ├── app.py │ └── requirements.txt ├── frontend/ │ ├── index.html │ ├── styles.css │ └── script.js └── README.md

yaml
Copy
Edit

---


```bash
git clone https://github.com/samarthdadar/shl.com.git
cd shl.com
2. Run the Backend (Flask API)
bash
Copy
Edit
cd backend
python -m venv venv         # Create virtual environment (optional)
source venv/bin/activate    # Activate venv (for Windows: venv\Scripts\activate)
pip install -r requirements.txt
python app.py
Backend will be running at: http://localhost:10000

3. Run the Frontend
You can open frontend/index.html directly in a browser OR use a static server like:

bash
Copy
Edit
cd frontend
python -m http.server 5500
Then open http://localhost:5500 in your browser.

📦 Technologies Used
Frontend: HTML, CSS, JavaScript

Backend: Python Flask

🛠 Future Improvements
Add SHL assessment database integration

Enhance UI/UX

Implement keyword matching or ML-based recommendation

👨‍💻 Author
Samarth Dadar – GitHub

yaml
Copy
Edit

---

Let me know if you want this added directly to your GitHub repo or want to customize it further!
