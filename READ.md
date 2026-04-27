🔐 PassForge

A Modern Password Generator & Strength Analyzer built with Flask

PassForge is a sleek and efficient web application that helps users generate secure passwords and evaluate password strength in real-time. Designed with simplicity and usability in mind, it combines functionality with a clean dark-themed UI.

🚀 Features
🔑 Custom Password Generator
Choose password length
Include/exclude:
Uppercase letters
Lowercase letters
Numbers
Special characters
📊 Real-Time Strength Checker
Instant feedback as user types
Visual strength indicator (Weak / Medium / Strong)
Color-based strength feedback (🔴 🟠 🟢)
🎨 Modern UI
Dark theme
Minimal and user-friendly design
Smooth interaction experience
🛠️ Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Logic: Custom password generation & strength evaluation algorithms
## 📦 Installation & Setup

```bash
1️⃣ Clone the Repository
git clone https://github.com/YOURNAME/PswdGenerator.git

2️⃣ Navigate to the Project Directory
cd PswdGenerator

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Open in Browser

After running, you will see:

Running on http://127.0.0.1:5000

Open this link in your browser.

⚠️ Important: Keep the terminal running while using the application.
```
## 📂 Project Structure

```bash
PswdGenerator/
│── app.py              # Main Flask application
│── main.py             # Core logic (if applicable)
│── templates/          # HTML files
│── static/             # CSS, JS, assets
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```
💡 How It Works
The backend (Flask) handles password generation and strength logic.
The frontend sends user input (length, options, password).
The system evaluates:
Length
Character variety
Complexity
Returns a strength score + visual feedback instantly.
🌟 Future Improvements
🔐 Password history & save feature
📋 Copy-to-clipboard button
🔎 Advanced strength analysis (entropy-based)
🌐 Deploy online (Render / Vercel / Railway)
👤 User authentication system
🤝 Contributing

Contributions are welcome!
If you have ideas to improve PassForge, feel free to fork the repo and submit a pull request.

📜 License

This project is open-source and available under the MIT License.

💬 Final Note

PassForge is not just a tool—it's a step toward building secure digital habits.
Simple, fast, and effective.
