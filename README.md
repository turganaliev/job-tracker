# My Personal Job Application Tracker 📝

A simple and secure web app I built to manage my job search. It uses Flask's session management to keep every user's data completely private.

**Check out the live demo:** [**job-tracker-nql4.onrender.com**](https://job-tracker-nql4.onrender.com)

---

![Job Tracker Screenshot](job-tracker-in-action.png)

---
## The Story Behind This Project

While deep in my own job search, I found myself juggling dozens of applications in messy spreadsheets and endless notes. I wanted a cleaner, simpler solution to see everything in one place, so I decided to build one myself. This Job Tracker is the result—a straightforward tool designed to bring a little order to the chaos of job hunting.

Building this was also a fantastic learning experience. I got to implement a full CRUD application from scratch and dive deep into Flask's secure session management to handle user data without needing a traditional database. Taking it from a local machine to a fully deployed application on Render was a challenging but rewarding process that taught me a lot about production environments.

---
## Features

* **Add & Track:** Quickly add new applications with all the key details: company, title, application status, and personal notes.
* **Clean Dashboard:** See all your applications at a glance in a simple, card-based layout.
* **Edit on the Fly:** Easily update the status or add new notes from a dedicated edit page.
* **Private & Secure:** Thanks to server-side sessions, your data is yours alone. Every visitor gets their own private tracker.

---
## Built With

I built this project using some of my favorite tools and technologies:

* **Backend:** Python 3 & Flask
* **Server:** Gunicorn
* **Hosting:** Render
* **Frontend:** HTML5 & CSS3

---
## How to Run It Locally

### Prerequisites
* Python 3.x
* pip

### Installation

1.  Clone the repo:
    ```sh
    git clone https://github.com/turganaliev/job-tracker.git
    ```
2.  Navigate into the project directory:
    ```sh
    cd job-tracker
    ```
3.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4.  Run the Flask application:
    ```sh
    python app.py
    ```
