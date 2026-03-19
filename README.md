# 🛒 E-commerce Automation Framework (Playwright + Pytest)

## 📌 Overview
This project is a scalable automation testing framework built using Python, Playwright, and Pytest.  
It follows Page Object Model (POM) design and supports end-to-end testing of an e-commerce workflow.

---

## 🚀 Features
- Page Object Model (POM)
- Pytest fixtures for setup/teardown
- Logging system
- Config management
- Parallel execution (pytest-xdist)
- HTML reporting
- Screenshot on failure
- CI/CD ready (GitHub Actions)

---

## 🧱 Project Structure
ecommerce-automation/
│
├── pages/
├── tests/
├── utils/
├── config/
├── conftest.py
├── pytest.ini
├── requirements.txt


---

## 🧪 Test Scenarios
- Login Test
- Add to Cart Test
- Remove from Cart Test
- Checkout Flow Test
- End-to-End Flow Test

---

## ⚙️ Setup Instructions

### 1. Clone Repository
git clone https://github.com/deepthapa3431/E-commerce-Automation-Framework-Playwright-Pytest-.git
cd ecommerce-automation

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt
playwright install

### 4. Run Tests
pytest -n 2 --html=report.html

---

## 🔥 Tech Stack
- Python
- Playwright
- Pytest

---

## 👨‍💻 Author
Deep Thapa