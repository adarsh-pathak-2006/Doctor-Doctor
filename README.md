# Doctor-Doctor 🩺

**Doctor-Doctor** is an intelligent, AI-powered medical consultation platform built with **Django**. By leveraging the power of **Google Gemini 2.5 Flash**, it provides rapid, structured medical analysis and drug prescription recommendations based on patient inputs.

---

## 🌟 Key Features

- **Intelligent AI Analysis**: Context-aware evaluations of current medical symptoms and prior medical history using Google's Gemini GenAI SDK.
- **Automated Prescriptions**: Generates structured, readable prescriptions complete with dosage instructions.
- **Secure Authentication**: Built-in Django authentication ensuring patient data and medical records remain private and secure.
- **History Tracking**: Keeps a secure log of all past prescriptions and analyses on the user's dashboard.

---

## 🔄 How It Works (Project Flow)

1. **Authentication**: Patients/Users register or log in securely through the platform.
2. **Consultation Initiation**: Users navigate to the OPD (Outpatient Department) Dashboard and fill out a consultation form.
3. **Data Collection**: The system securely captures:
   - Patient Age
   - Current Condition / Symptoms
   - Prior Medical History
4. **AI Processing**: The backend constructs a highly detailed prompt and securely transmits it to the **Gemini 2.5 Flash** AI model.
5. **Structured Output**: The AI acts as an expert medical professional, returning a strict JSON response containing a detailed condition analysis and a recommended prescription.
6. **Persistence**: The AI's JSON output is parsed, saved securely to the SQLite database, and presented to the user on an individual consultation page.

---

## 🛠️ Tech Stack

- **Backend Framework**: Django (Python)
- **AI Integration**: Google GenAI SDK (`gemini-2.5-flash`)
- **Database**: SQLite3
- **Environment Management**: `python-dotenv`

---

## 🚀 Getting Started

Follow these instructions to set up the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/adarsh-pathak-2006/Doctor-Doctor.git
cd Doctor-Doctor/config
```

### 2. Set up the Environment Variables
Copy the `.env.example` file to create your own `.env` file:
```bash
cp .env.example .env
```
Open `.env` and add your **Google Gemini API Key**:
```env
GEMINI_API_KEY="your_actual_api_key_here"
```

### 3. Install Dependencies
Make sure you have python installed, and install the required packages (e.g., `django`, `google-genai`, `python-dotenv`):
```bash
pip install django google-genai python-dotenv
```

### 4. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```
Navigate to `http://127.0.0.1:8000/` in your browser to start using the platform!

---
*Disclaimer: Doctor-Doctor is an AI-powered assistant intended for educational and demonstrative purposes. It should not be used as a replacement for professional medical advice, diagnosis, or treatment.*
