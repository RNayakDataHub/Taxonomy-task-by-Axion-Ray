# Taxonomy Tagging Task – Axion Ray

This project involves tagging unstructured Complaint, Cause, and Correction fields with standardized taxonomy terms to enable structured analysis of failure records. The goal is to automate the identification and mapping of root causes, symptom conditions/components, and fix conditions/components based on a provided taxonomy sheet.

---

## 📁 Project Summary

- **Client**: Axion Ray  
- **Objective**: Automatically tag records using a standardized taxonomy to transform free-text issue descriptions into structured data.
- **Input**:
  - A dataset containing `Complaint`, `Cause`, and `Correction` text fields
  - A taxonomy sheet with standardized terms for:
    - Root Cause
    - Symptom Condition
    - Symptom Component
    - Fix Condition
    - Fix Component

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Regular Expressions (re)
- Jupyter Notebook / Script (.py)
- Excel / CSV (for input & output)

---

## 📌 Approach

### 🔹 1. Data Preparation
- Cleaned the taxonomy sheet to remove `null` or duplicate entries
- Extracted unique values for each taxonomy field

### 🔹 2. Matching Logic
- Defined a **case-insensitive substring matching function** to scan the text fields
- Multiple matched terms per row were returned as **comma-separated values**

### 🔹 3. Field-wise Mapping

| Taxonomy Field | Source Fields Searched | Output Column(s) |
|----------------|------------------------|-------------------|
| Root Cause     | Complaint, Cause, Correction | `Root Cause` |
| Symptom Condition / Component | Mapped separately from Complaint, Cause, Correction | `Symptom Condition 1/2/3`, `Symptom Component 1/2/3` |
| Fix Condition / Component | Mapped separately from Complaint, Cause, Correction | `Fix Condition 1/2/3`, `Fix Component 1/2/3` |

---

## ✅ Outcome

- Each record in the dataset was tagged with standardized terms based on matches in the unstructured fields.
- Enabled structured analysis for:
  - High-frequency root causes
  - Common symptom/fix patterns
- Laid the groundwork for future **rule-based** or **ML-based auto-tagging systems**

---

## 🚀 Future Enhancements

- Implement fuzzy matching or NLP for improved term detection
- Train a machine learning model to predict taxonomy tags
- Integrate tagging into a real-time issue triage dashboard (e.g., Power BI or Streamlit)

---

