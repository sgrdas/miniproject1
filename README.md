# AI Career Hub — Flask

## Quickstart

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/

## Admin Panel

The app includes a simple admin panel at `/admin` with minimal CRUD for `courses`, `jobs`, and `internships`.

- Default admin password: `admin123` (set `ADMIN_PASSWORD` env var to override)
- Default session secret: `FLASK_SECRET` env var may be set, otherwise a dev key is used

## Structure

```
ai_career_hub/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── jobs.html
    ├── courses.html
    ├── internships.html
    ├── resume-analyzer.html
    ├── resume-builder.html
    ├── career-predictor.html
    └── r.html
```


# AI Career Hub - Logo Enhancement Summary

## ✅ **Comprehensive Logo System Implemented**

### What's Been Added:

#### 1. **Extended Logo Database (150+ Companies)**
The `get_company_logo()` function now includes logos for:

**Tech Giants:**
- Google, Microsoft, Apple, Amazon, Meta, OpenAI, IBM, Adobe, NVIDIA, Intel, Oracle, Cisco, GitHub

**Cloud Providers:**
- AWS, Google Cloud, Microsoft Azure, Alibaba Cloud

**Software & Services:**
- Salesforce, Slack, Zoom, Atlassian, JetBrains, VMware, Citrix, SAP

**Financial Services:**
- JPMorgan, Goldman Sachs, Morgan Stanley, Bank of America, Citi, Wells Fargo
- Coinbase, Square, Stripe, PayPal

**Management Consulting:**
- Deloitte, EY, PwC, KPMG, Accenture, Infosys, TCS

**Automotive:**
- Tesla, Toyota, Honda, BMW, Mercedes-Benz, Audi, Porsche, Ferrari, Lamborghini
- Nissan, Ford, GM, Volkswagen, Hyundai, Kia, Jaguar
- Electric: BYD, Rivian, Lucid, XPeng, NIO

**Consumer & Retail:**
- Amazon, Walmart, Target, Best Buy, Home Depot, Costco

**Entertainment & Media:**
- Netflix, Disney, Warner Bros, Universal, HBO, Spotify, Apple Music

**E-commerce & Logistics:**
- Alibaba, Shopify, eBay, Etsy, Airbnb, Uber, DoorDash

**Telecommunications:**
- AT&T, Verizon, Comcast, Spectrum, T-Mobile

**Aerospace & Defense:**
- Boeing, Airbus, Lockheed Martin, SpaceX

**Industrial & Manufacturing:**
- Siemens, Bosch, GE, Caterpillar, 3M, Honeywell

**And many more...**

#### 2. **Smart Logo Fallback System**
- **Exact Match:** If company name exists in database → use its logo
- **Partial Match:** If company name contains or is contained in database entry → use matched logo
- **Case-Insensitive:** Works with any capitalization variant
- **Fallback:** Unknown companies get a professional placeholder image from placeholder.com

#### 3. **Logo Display on Internship Cards**
Each internship card now displays:
- ✅ Company logo (70px × 70px, professionally styled)
- ✅ Company name
- ✅ Job role
- ✅ Stipend information
- ✅ Apply Now button

#### 4. **Dynamic Company Dropdown**
The internships page company filter shows:
- ✅ All 225 unique companies from the dataset
- ✅ Alphabetically sorted
- ✅ Dynamically generated from actual data
- ✅ Professional filtering experience

### Features:
- ✅ Professional company logos from Wikimedia Commons
- ✅ Responsive image sizing with CSS
- ✅ Proper alt text for accessibility
- ✅ Intelligent fallback for unmapped companies
- ✅ No broken image links

### How It Works:

```python
# Get logo for any company
logo_url = get_company_logo("Google")  # Returns Google's official logo
logo_url = get_company_logo("google")  # Returns professional placeholder
```

### Visit Your Website:
- 🔗 **Internships:** http://127.0.0.1:5000/internships
- 🔗 **Jobs:** http://127.0.0.1:5000/jobs
- 🔗 **Home:** http://127.0.0.1:5000/

### What You'll See:
- Beautiful internship cards with company logos
- Professional company branding on every card
- Full company dropdown with 225+ companies
- Responsive design that works on all devices
- Accessible images with proper alt text

**All internship cards now display correct company logos with professional fallbacks!** 🎉
# 🚀 AI Career Hub

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2%2B-green.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI Career Hub** is an intelligent, full-stack career platform designed to help students, job seekers, and tech professionals navigate the rapidly evolving technology landscape. Built with Flask and SQLite, it offers personalized job and internship discovery, AI career trajectory prediction, interactive resume analysis, real-time multi-template resume building with client-side PDF export, an AI assistant chatbot, and a comprehensive administrative management dashboard.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [System Architecture](#-system-architecture)
- [Key Features](#-key-features)
  - [1. User Authentication & Profile Personalization](#1-user-authentication--profile-personalization)
  - [2. AI & Tech Jobs Portal](#2-ai--tech-jobs-portal)
  - [3. Internships Portal & Company Logo System](#3-internships-portal--company-logo-system)
  - [4. Courses Catalog & Personalized Recommendations](#4-courses-catalog--personalized-recommendations)
  - [5. AI Career Predictor](#5-ai-career-predictor)
  - [6. AI Resume Analyzer](#6-ai-resume-analyzer)
  - [7. Interactive AI Resume Builder with PDF Export](#7-interactive-ai-resume-builder-with-pdf-export)
  - [8. Conversational AI Assistant Chatbot](#8-conversational-ai-assistant-chatbot)
  - [9. User Feedback System](#9-user-feedback-system)
  - [10. Administrative Dashboard & Analytics](#10-administrative-dashboard--analytics)
- [Technology Stack](#-technology-stack)
- [Project Directory Structure](#-project-directory-structure)
- [Database Schema & Data Flow](#-database-schema--data-flow)
- [REST API Reference](#-rest-api-reference)
- [Installation & Quickstart](#-installation--quickstart)
- [Environment Variables & Configuration](#-environment-variables--configuration)
- [Default Credentials](#-default-credentials)
- [Utility Scripts](#-utility-scripts)
- [Contributing & License](#-contributing--license)

---

## 🌟 Overview

The modern tech job market moves fast, requiring job seekers to constantly upgrade skills, align their resumes with industry expectations, and track emerging roles. **AI Career Hub** unifies these critical workflows into a single cohesive platform:

1. **Discovery:** Aggregates jobs and internships across AI, Data Science, Cloud, and Software Engineering.
2. **Personalization:** Matches jobs, internships, and courses to users based on their registered skills and target locations.
3. **Guidance:** Recommends optimal career paths via the **AI Career Predictor** and grades CV readiness with the **AI Resume Analyzer**.
4. **Action:** Allows users to build industry-ready resumes with real-time formatting previews and instant PDF generation.
5. **Administration:** Empowers administrators with a full CRUD panel, real-time metrics, visual analytics, and one-click CSV export utilities.

---

## 🏛 System Architecture

The following diagram outlines the architecture, data flow, and interactions across the application:

```
+-----------------------------------------------------------------------------------+
|                                 CLIENT BROWSER                                    |
|  Bootstrap 5 | Vanilla JS | HTML5 / CSS3 | jsPDF Library | FontAwesome            |
+-----------------------------------------------------------------------------------+
        |                                        |                        |
   HTTP / HTML Requests                    REST API (JSON)         PDF Generation
        |                                        |                  (Client-Side)
        v                                        v                        v
+-----------------------------------------------------------------------------------+
|                             FLASK WEB SERVER (app.py)                             |
|                                                                                   |
|  [Authentication & Sessions]      [Core Application Routes]    [Admin Panel]      |
|  - Signup / Login / Logout        - Home (/)                   - Admin Auth Guard |
|  - Password Hashing (Werkzeug)    - Jobs (/jobs)               - CRUD Operations  |
|  - Profile Management             - Internships (/internships) - Analytics Engine |
|  - Context Processor              - Courses (/courses)         - CSV Exporter     |
|                                   - Predictor (/career-pred)                      |
|  [API & Chat Engine]              - Analyzer (/resume-anal)                       |
|  - /api/courses (CRUD)            - Builder (/resume-build)                       |
|  - /chat (NLP / Rule-based)       - Feedback (/feedback)                          |
+-----------------------------------------------------------------------------------+
        |                                                                  ^
        v                                                                  |
+------------------------------+             +-----------------------------+-------+
|    DATABASE (SQLite3: data.db)|             |     SEED DATA / CSV STORAGE (data/)   |
|                              |  Auto-Seed  |                                     |
|  - users                     |<------------|  - ai_job_market_insights.csv       |
|  - courses                   |  on startup |  - coursea_data.csv                 |
|  - jobs                      |  if empty   |  - internship.csv                   |
|  - internships               |             +-------------------------------------+
|  - feedback                  |
+------------------------------+
```

---

## 💡 Key Features

### 1. User Authentication & Profile Personalization
- **Registration (`/signup`)**: Encrypted user registration using `werkzeug.security.generate_password_hash`. Duplicate email check is enforced.
- **Login (`/login`)**: Secure session initiation verified against hashed database passwords. Also supports seamless admin elevation.
- **Profile Management (`/profile`)**: Allows users to configure their full name, target role, technical skills (comma-separated), city/location, and target job keywords.
- **Dynamic Content Adaptation**: Once logged in, the `/jobs`, `/courses`, and `/internships` routes automatically filter and prioritize listings matching the user's specific skills and city.

### 2. AI & Tech Jobs Portal (`/jobs`)
- Powered by real-world job market data (`data/ai_job_market_insights.csv`).
- Interactive client-side and server-side filtering by job title, company name, industry, and city.
- Highlighting salary estimates (USD), job growth projections, and remote-work indicators.
- Responsive company branding container with fallback imagery.

### 3. Internships Portal & Company Logo System (`/internships`)
- Curated internship postings from top tech enterprises and startups (`data/internship.csv`).
- Real-time search by role and dynamic dropdown filter populated with 225+ companies.
- Stipend figures, role descriptions, and instant "Apply Now" triggers.
- **Smart Logo Fallback System**: Integrates vector logos from Wikimedia Commons and official sources, gracefully falling back to structured placeholder badges for unmapped brands.

### 4. Courses Catalog & Personalized Recommendations (`/courses`)
- Comprehensive repository of online courses seeded from Coursera dataset (`data/coursea_data.csv`).
- Categorized into domains: *Programming*, *AI & Data*, *IT & Cloud*, and *Non-IT*.
- Filters for course pricing (Free vs. Paid) and keyword search.
- Personalized recommendation badge appears automatically when tailored to logged-in user skills.

### 5. AI Career Predictor (`/career-predictor`)
- Users enter their current technical skills and competencies (e.g., `Python, Machine Learning, SQL, Cloud`).
- The engine computes the most relevant career path (such as *Machine Learning Engineer*, *Data Scientist*, *Full Stack Developer*, *Cybersecurity Analyst*, or *Cloud Engineer*).
- Visualizes:
  - Career Match Title
  - AI Confidence percentage rating with animated progress bars
  - Curated course recommendations for upskilling
  - Actionable professional tips to land the role

### 6. AI Resume Analyzer (`/resume-analyzer`)
- Evaluates resumes (`.pdf`, `.doc`, `.docx`) uploaded by candidates.
- Generates an instant, multi-metric diagnostic report:
  - **Overall Score** (0–100%)
  - **Technical Skills** rating
  - **Communication & Impact** rating
  - **Experience Relevance** rating
  - **Formatting & Presentation** rating
  - **Certifications & Validation** rating
- Identifies the candidate's strongest job match and highlights specific areas for improvement.

### 7. Interactive AI Resume Builder with PDF Export (`/resume-builder` & `/r`)
- Live, two-pane interactive builder: form inputs on the left, instant live layout preview on the right.
- **Multiple Design Templates**:
  - **Modern**: Sleek gradient headers, clean typography, badge-styled skill tags.
  - **Classic**: Traditional black-and-white serif format ideal for corporate/finance roles.
  - **Minimal**: Clean lines, subtle borders, high information density.
  - **Professional**: Two-column layout with colored sidebar, profile photo, and segmented sections.
- Supports profile photo upload, personal contacts, executive summary, work experience, projects, education, skills, achievements, and hobbies.
- **One-Click Client-Side PDF Generation**: Uses `jsPDF` to compile and export the structured resume directly to a downloadable PDF without sending private CV data to external servers.

### 8. Conversational AI Assistant Chatbot (`/chat`)
- Floating interactive chat assistant available across public pages.
- Responds to natural language queries regarding available courses, top job locations, active internship opportunities, and website navigation.
- Backed by an asynchronous JSON endpoint (`POST /chat`).

### 9. User Feedback System (`/feedback`)
- Public feedback submission form supporting user name, email, star ratings (1–5 stars), and custom review comments.
- Supports both standard browser form submission and asynchronous JSON requests.
- Recorded directly into the SQLite database for administrative monitoring.

### 10. Administrative Dashboard & Analytics (`/admin`)
- Accessible via secure admin authentication (`/admin/login`).
- **Dashboard Overview (`/admin`)**:
  - Live metric counters for Courses, Jobs, Internships, and User Feedback.
  - Quick summary table of the latest 5 user reviews and star ratings.
- **Data Analytics API (`/admin/chart-data`)**:
  - Aggregates courses by category, top 10 job markets by city, and top 10 internship providers.
- **Complete CRUD Operations**:
  - Manage, create, edit, and delete courses (`/admin/courses`).
  - Manage, create, edit, and delete jobs (`/admin/jobs`).
  - Manage, create, edit, and delete internships (`/admin/internships`).
  - Inspect and delete user feedback submissions (`/admin/feedback`).
- **One-Click CSV Exporter (`/admin/export/<which>`)**:
  - Instantly export database tables (`courses`, `jobs`, `internships`, `feedback`) into downloadable `.csv` spreadsheets.

---

## 🛠 Technology Stack

| Layer | Technology | Description |
|---|---|---|
| **Backend Framework** | **Flask (Python 3.8+)** | Lightweight, modular WSGI web application framework |
| **Database** | **SQLite 3** | Serverless, self-contained relational database (`data.db`) |
| **Data Processing** | **Pandas & Python CSV** | Dataset ingestion, CSV parsing, and seeding |
| **Security & Auth** | **Werkzeug Security** | Secure password hashing (`pbkdf2:sha256`) & HTTP-only cookies |
| **Frontend Styling** | **Bootstrap 5.3.2** | Responsive layout, modern UI components, and grid system |
| **Icons & Typography** | **FontAwesome 6 & Google Fonts** | Poppins font family, modern SVG icons |
| **PDF Generation** | **jsPDF 2.5.1** | Client-side dynamic PDF compilation and download |
| **Architecture** | **MVC / RESTful API** | Clean separation of models, Jinja2 templates, and JSON APIs |

---

## 📁 Project Directory Structure

```
ai_career_hub/
│
├── app.py                      # Main application entry point (routes, auth, DB init, APIs)
├── requirements.txt            # Python dependencies (Flask, pandas)
├── data.db                     # SQLite database file (created automatically on startup)
├── test_data.py                # Diagnostic script to verify CSV datasets and path loading
├── LOGO_SYSTEM.md              # Technical specification of the company logo system
├── README.md                   # Complete project documentation
│
├── data/                       # Initial dataset seed files
│   ├── ai_job_market_insights.csv   # Comprehensive AI/Tech job listings dataset
│   ├── coursea_data.csv             # Coursera course catalog dataset
│   └── internship.csv               # Tech internship and stipend listings dataset
│
├── scripts/                    # Maintenance and utility automation
│   └── reset_courses.py        # Utility to purge and re-seed the courses table
│
├── static/                     # Static assets
│   └── style.css               # Custom global CSS styles and admin theme rules
│
└── templates/                  # Jinja2 HTML templates
    ├── index.html              # Homepage with hero section, feature cards, and chatbot
    ├── jobs.html               # Tech jobs listing page with filters
    ├── internships.html        # Tech internships listing page with logo system
    ├── courses.html            # Course catalog with search and wishlist
    ├── career-predictor.html   # AI Career Predictor tool
    ├── resume-analyzer.html    # AI Resume Analyzer tool
    ├── resume-builder.html     # Interactive AI Resume Builder with PDF export
    ├── r.html                  # Advanced alternative resume builder layout
    ├── login.html              # User login page
    ├── signup.html             # User registration page
    ├── profile.html            # User profile and skills configuration
    ├── feedback.html           # Public user feedback form
    │
    └── admin/                  # Administrative management templates
        ├── index.html          # Admin dashboard with metric cards and recent reviews
        ├── login.html          # Admin authentication page
        ├── list.html           # Generic reusable tabular CRUD listing
        ├── form_course.html    # Form to add / edit courses
        ├── form_job.html       # Form to add / edit jobs
        ├── form_intern.html    # Form to add / edit internships
        ├── feedback_list.html  # User feedback table with delete action
        ├── feedback_detail.html# Detailed view for individual feedback item
        └── about.html          # Admin platform information
```

---

## 🗄 Database Schema & Data Flow

When `app.py` runs, it executes `init_db()` which checks and creates the following tables if they do not exist, automatically seeding them with CSV data if empty:

### 1. `users` Table
Stores registered member accounts and personalization preferences.
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    role TEXT,
    skills TEXT,
    city TEXT,
    desired TEXT,
    password TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. `courses` Table
Stores learning courses and training programs.
```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    price TEXT,
    link TEXT,
    image_url TEXT
);
```

### 3. `jobs` Table
Stores AI and tech career opportunities.
```sql
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    city TEXT,
    salary TEXT,
    description TEXT,
    logo_url TEXT,
    apply_url TEXT
);
```

### 4. `internships` Table
Stores student and early-career internship roles.
```sql
CREATE TABLE internships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    role TEXT,
    stipend TEXT,
    logo_url TEXT
);
```

### 5. `feedback` Table
Stores user reviews, star ratings, and contact messages.
```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    message TEXT,
    rating INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🔌 REST API Reference

The application exposes both RESTful endpoints and internal utility APIs:

### 1. Courses API

#### Get All Courses
```http
GET /api/courses
```
**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Machine Learning Specialization",
    "category": "AI & Data",
    "price": "Free",
    "link": "https://coursera.org/...",
    "image_url": "https://..."
  }
]
```

#### Add a Course
```http
POST /api/courses
Content-Type: application/json

{
  "title": "Full Stack Web Development",
  "category": "Programming",
  "price": "Paid",
  "link": "https://example.com/course",
  "image_url": "https://example.com/image.jpg"
}
```
**Response (201 Created):**
```json
{ "message": "Course added" }
```

#### Update a Course
```http
PUT /api/courses/<int:id>
Content-Type: application/json

{
  "title": "Updated Course Title",
  "category": "Cloud Computing",
  "price": "Free",
  "link": "https://example.com/course",
  "image_url": "https://example.com/image.jpg"
}
```
**Response (200 OK):**
```json
{ "message": "Course updated" }
```

#### Delete a Course
```http
DELETE /api/courses/<int:id>
```
**Response (200 OK):**
```json
{ "message": "Course deleted" }
```

---

### 2. Chatbot API

```http
POST /chat
Content-Type: application/json

{
  "message": "Can you recommend courses in machine learning?"
}
```
**Response (200 OK):**
```json
{
  "reply": "Top course categories: AI & Data, Programming. Browse all courses at /courses"
}
```

---

### 3. Admin Analytics API

```http
GET /admin/chart-data
Cookie: admin=1
```
**Response (200 OK):**
```json
{
  "courses": {
    "labels": ["Programming", "AI & Data", "IT & Cloud"],
    "counts": [120, 85, 42]
  },
  "jobs": {
    "labels": ["Bangalore", "San Francisco", "New York"],
    "counts": [54, 39, 28]
  },
  "internships": {
    "labels": ["Google", "Amazon", "Microsoft"],
    "counts": [12, 10, 8]
  }
}
```

---

### 4. Admin CSV Export Endpoint

```http
GET /admin/export/<courses|jobs|internships|feedback>
Cookie: admin=1
```
**Response (200 OK):**
Downloads a dynamically formatted `.csv` attachment.

---

## ⚙️ Installation & Quickstart

### Prerequisites
- **Python 3.8 or higher**
- **pip** package manager
- **Git** (optional, for cloning)

### Step 1: Clone or Navigate to the Repository
```bash
cd "C:\Users\ravid\Downloads\mini_project-main (1)\mini_project-main\ai_career_hub"
```

### Step 2: (Recommended) Create a Virtual Environment
```bash
# On Windows PowerShell / CMD:
python -m venv venv
.\venv\Scripts\activate

# On macOS / Linux:
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Open in Your Browser
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

> [!NOTE]
> On the very first launch, the application automatically initializes the SQLite database (`data.db`) and seeds initial records from the files in `data/`.

---

## 🔐 Environment Variables & Configuration

You can customize the application's runtime settings using environment variables:

| Variable | Description | Default Value |
|---|---|---|
| `FLASK_SECRET` | Session encryption secret key | `"devkey123"` |
| `ADMIN_USER` | Admin username | `"ravi092"` |
| `ADMIN_EMAIL` | Admin login email | `"admin@localhost"` |
| `ADMIN_PASSWORD` | Admin login password | `"ravi@123"` |

### Setting Environment Variables in Windows PowerShell:
```powershell
$env:ADMIN_USER = "myadmin"
$env:ADMIN_PASSWORD = "SuperSecurePassword99!"
$env:FLASK_SECRET = "custom_secret_key_string"
python app.py
```

### Setting Environment Variables in Linux / macOS:
```bash
export ADMIN_USER="myadmin"
export ADMIN_PASSWORD="SuperSecurePassword99!"
export FLASK_SECRET="custom_secret_key_string"
python3 app.py
```

---

## 🔑 Default Credentials

### 1. Administrative Access
- **Admin Panel URL:** [http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin) or [http://127.0.0.1:5000/admin/login](http://127.0.0.1:5000/admin/login)
- **Username / Identifier:** `ravi092` *(or `admin@localhost`)*
- **Password:** `ravi@123`

### 2. User Access
- New users can register instantly at [http://127.0.0.1:5000/signup](http://127.0.0.1:5000/signup).
- After signing up, log in at [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login) and visit `/profile` to configure your skills for personalized recommendations.

---

## 🛠 Utility Scripts

### 1. Dataset Verification Script (`test_data.py`)
Verifies that the CSV dataset files exist in `data/` and tests data ingestion functions:
```bash
python test_data.py
```

### 2. Courses Table Reset Script (`scripts/reset_courses.py`)
Clears the `courses` table in `data.db` and injects 40 fresh categorized dummy records:
```bash
python scripts/reset_courses.py
```

---

## 🚀 Future Roadmap & Enhancements

- [ ] **Advanced AI/LLM Integration:** Connect the chatbot and resume analyzer directly to OpenAI / Google Gemini API for contextual feedback.
- [ ] **Direct Application Tracking:** Add a "Saved Jobs" and "Application Tracker" kanban board for candidates.
- [ ] **PDF Parsing with OCR:** Enable server-side text extraction from uploaded PDF resumes using `pypdf` or `pdfplumber`.
- [ ] **Email Alerts:** Automated email notifications for newly posted jobs matching user skill sets.
- [ ] **OAuth2 Social Login:** Google and GitHub one-click authentication.

---

## 📄 License & Attribution

This project was developed as an academic and professional mini-project for AI career preparation and education.  
Distributed under the **MIT License**. Free for educational and commercial use.

