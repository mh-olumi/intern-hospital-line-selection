# 🏥 Intern Hospital Line Selection

A web application built with **Python Django** that allows medical interns to select hospital lines, rotations, or specialties based on availability, preferences, and rules set by administrators.

---

## 🚀 Features

- 📝 Intern registration and login
- 🏥 Browse available hospital lines/rotations
- ✅ Select and submit preferred choices
- 📊 Admin dashboard for monitoring and updating availability
- 🔒 Secure role-based access for admins and interns

---

## 🛠️ Tech Stack

- **Backend:** Python 3.x, Django 4.x
- **Frontend:** HTML5, CSS3, Bootstrap (or other framework)
- **Database:** SQLite (default) or PostgreSQL/MySQL

---

## 📦 Installation

### 1. Clone the repository

```bash
mkdir intern-hospital-line-selection
cd intern-hospital-line-selection
git clone https://github.com/mh-olumi/intern-hospital-line-selection.git
```

### 2. make .env based on .env.sample in myworld\myworld

### 3. prepare your data (you can use python folder)

### 4. backup your sqlite db into sqlite.sqlite3

```bash
sqlite3 sqlite.sqlite3 ".backup temp.db" 
move temp.db pgloader-data
```
### 5. in pgloader-data rename right file to migrate.load based on your needs

### 6. edit pgloader-data/migrate.load using your postgres db access data
```bash
docker run --rm -v "intern-hospital-line-selection/myworld/data/pgloader-data:/data" dimitri/pgloader pgloader /data/migrate.load
```
### 7. run the project
```bash
line/Scripts/activate.bat
cd myworld
pip install requiremnts.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runsever
```
