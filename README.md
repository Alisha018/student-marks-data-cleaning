# Student Marks Data Cleaning (Python + Pandas)

This project focuses on cleaning and standardizing a messy student dataset using Python.  
It fixes issues like inconsistent formatting, missing values, invalid numbers, and incorrect text fields.

## 🧹 What This Project Does
- Removed leading/trailing spaces from student names  
- Normalized names to Title Case  
- Standardized gender values (m/M/male → Male, f/F/female → Female)  
- Converted non-numeric marks (like "Ninety") into numeric  
- Removed out-of-range marks (< 0 or > 100)  
- Filled missing marks using median imputation  
- Exported a clean, analysis-ready CSV file

## 📂 Files in This Project
- `students_raw.csv` — raw messy data  
- `data_cleaning.py` — cleaning script  
- `students_cleaned.csv` — cleaned output  
- `README.md` — project documentation  

## ▶️ How to Run
```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy
python3 data_cleaning.py

