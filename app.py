from flask import Flask, render_template
import csv

app = Flask(__name__)

# Function to read CSV and return data
def read_attendance():
    filename = "attendance.csv"
    attendance_data = []
    try:
        with open(filename, mode='r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                attendance_data.append(row)
    except FileNotFoundError:
        pass

    return attendance_data

# Function to read attendance and group by student
def read_attendance_by_student():
    filename = "attendance.csv"
    attendance_by_student = {}
    try:
        with open(filename, mode='r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                name, date, time = row
                if name not in attendance_by_student:
                    attendance_by_student[name] = []
                attendance_by_student[name].append((date, time))
    except FileNotFoundError:
        pass

    return attendance_by_student

@app.route('/')
def index():
    attendance_data = read_attendance()
    return render_template('index.html', attendance_data=attendance_data)

@app.route('/profiles')
def profiles():
    attendance_by_student = read_attendance_by_student()
    return render_template('profiles.html', attendance_by_student=attendance_by_student)

if __name__ == '__main__':
    app.run(debug=True)
