<div align="center">

# 🩺 Doctor-Doctor 

**Next-Generation AI Medical Assistant & Consultation Platform**

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Gemini API](https://img.shields.io/badge/Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*An intelligent, highly-responsive platform that bridges the gap between patient symptoms and AI-driven medical insights. Experience the future of automated, structured medical prescriptions.*

[Explore Features](#-features) • [Installation](#-quick-start) • [Tech Stack](#-tech-stack) • [Demo](#)

</div>

---

## ⚡ Elevating the Medical Experience
**Doctor-Doctor** isn't just a consultation form—it's a complete, premium ecosystem. Powered by **Google Gemini 2.5 Flash**, the platform dynamically analyzes patient symptoms alongside their medical history, acting as a highly experienced digital medical professional to deliver instant, structured, and reliable insights.

With an aesthetic, glassmorphic UI and buttery-smooth micro-animations, the user experience is designed to feel as premium as the technology powering it.

---

## ✨ Features That Shine

- 🧠 **Instant AI Diagnostics**: Context-aware evaluations of medical symptoms leveraging state-of-the-art Generative AI.
- 💊 **Automated Rx Generation**: Outputs beautifully formatted, print-ready medical prescriptions complete with detailed dosage instructions.
- 🎨 **Premium UI/UX**: A breathtaking frontend built with glassmorphism, modern typography (Google Fonts *Outfit* & *Inter*), and slick CSS micro-interactions.
- 🔐 **Bulletproof Security**: Built-in Django authentication ensuring patient data, medical records, and AI prompts remain completely private and secure.
- 📚 **Consultation History**: A dynamic, grid-based dashboard that keeps a secure, interactive log of all your past medical analyses.
- 🖨️ **Print-Ready Digital Pads**: View individual prescriptions on a beautifully designed digital "Rx pad", perfectly optimized for physical printing.

---

## 🚀 Quick Start

Get your AI medical assistant running locally in under 2 minutes.

### 1. Clone the Repository
```bash
git clone https://github.com/adarsh-pathak-2006/Doctor-Doctor.git
cd Doctor-Doctor/config
```

### 2. Environment Setup
Create your local environment variables file:
```bash
cp .env.example .env
```
Open the newly created `.env` file and insert your **Google Gemini API Key**:
```env
GEMINI_API_KEY="your_actual_api_key_here"
```

### 3. Install Dependencies
Ensure Python is installed, then run:
```bash
pip install -r requirements.txt
```

### 4. Database & Static Files
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
```

### 5. Launch 
```bash
python manage.py runserver
```
🔥 **You're live!** Navigate to `http://127.0.0.1:8000/` to experience Doctor-Doctor.

---

## 🛠 Tech Stack

| Layer | Technology | Description |
| --- | --- | --- |
| **Backend** | Django 5.x | High-level Python web framework |
| **AI Engine** | Google GenAI SDK | `gemini-2.5-flash` for ultra-fast medical analysis |
| **Frontend** | HTML5 / CSS3 / Vanilla JS | Custom-built, lightweight, premium UI architecture |
| **Database** | SQLite3 | Default secure relational database |
| **Deployment** | Gunicorn & Whitenoise | Production-ready server and static file serving |

---

<div align="center">

*Disclaimer: Doctor-Doctor is an AI-powered assistant intended for educational and demonstrative purposes. It should not be used as a replacement for professional medical advice, diagnosis, or treatment.*

**Crafted with ❤️ for the future of healthcare.**

</div>
