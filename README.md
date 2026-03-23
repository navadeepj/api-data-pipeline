# API Data Pipeline

## 📌 Overview
This project demonstrates a basic ETL (Extract, Transform, Load) data pipeline using Python.

The pipeline fetches data from a public API, processes and cleans the data, and stores it in a structured SQL database.

---

## ⚙️ Tech Stack
- Python
- REST API
- JSON
- SQLite
- ETL Concepts

---

## 🔄 Pipeline Steps

### 1. Extract
- Fetch data from a public API using `requests`

### 2. Transform
- Clean and structure JSON data
- Select relevant fields (id, title, body)

### 3. Load
- Store processed data into SQLite database
- Create table schema and insert records

---

## 🧠 Key Features
- API data extraction
- JSON data handling
- Data cleaning and transformation
- Database integration using SQLite
- Basic schema design

---

## ▶️ How to Run

```bash
pip install requests
python pipeline.py
