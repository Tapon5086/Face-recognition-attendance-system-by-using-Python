

```markdown
# 👥 Face Recognition Attendance System Using Python

This project automates attendance tracking by detecting and recognizing faces in real time using Python. It eliminates manual attendance errors and accelerates the attendance process. The system securely stores attendance records, making it an efficient and user-friendly solution for schools, offices, and other organizations.

---

## 🚀 Features

- Real-time face detection and recognition
- Automated attendance marking with timestamp
- Secure storage of attendance records in CSV format
- User-friendly web interface for attendance display (`index.html`, `profiles.html`)
- Supports multiple users with accurate recognition
- Lightweight and easy to deploy

---

## 🛠️ Technology Stack

- Python (OpenCV, face_recognition libraries)
- Flask (for web interface and backend API)
- CSV for attendance record storage
- HTML for front-end interface

---

## 📁 Repository Structure

├── app.py                   # Flask app to serve web interface and API
├── main.py                  # Core face recognition and attendance logic
├── attendance.csv           # Attendance records storage
├── 2024-05-25.csv           # Sample attendance data (by date)
├── index.html               # Main webpage for attendance status
├── profiles.html            # Profiles or detailed attendance page
├── README.md                # Project documentation

````

---

## 🔧 Getting Started

### Prerequisites

- Python 3.7 or above
- Required Python libraries (see below)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Tapon5086/Face-recognition-attendance-system-by-using-Python.git
   cd Face-recognition-attendance-system-by-using-Python
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main face recognition attendance script:

   ```bash
   python main.py
   ```

4. (Optional) Run the Flask web app to view attendance dashboard:

   ```bash
   python app.py
   ```

5. Open your browser and go to:

   ```
   http://localhost:5000/
   ```

---

## ⚙️ How It Works

* The system captures video from a webcam
* It detects and encodes faces using the `face_recognition` library
* Compares live faces with stored encodings of known users
* Automatically logs attendance with current date and time to CSV
* The Flask app displays attendance records on a web interface

---

## 🤝 Contribution

Feel free to fork, improve, and submit pull requests!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Tapon Paul**
[GitHub](https://github.com/Tapon5086) • [LinkedIn](https://linkedin.com/in/taponpaul)

```
