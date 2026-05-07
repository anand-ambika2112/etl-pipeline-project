# 📊 Bank Transactions ETL Pipeline

## 🔷 Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and SQL to process raw banking transaction data and generate meaningful business insights.

---

## 🔷 Features
- Extracts raw transaction data from CSV
- Cleans and standardizes messy real-world data
- Handles missing values and inconsistent formats
- Loads processed data into SQLite database
- Generates analytical reports

---

## 🔷 Tech Stack
- Python (Pandas)
- SQL (SQLite)
- File Handling (CSV, JSON)
- VS Code

---

## 🔷 Project Structure

etl_pipeline_project/
│
├── data/
├── src/
├── output/
├── README.md



---

## 🔷 Outputs
- Cleaned dataset (`result_processed.json`)
- Category-wise spending report
- Monthly spending trends
- Transaction summary (credit vs debit)

---

## 🔷 Key Insights
- Identified highest spending categories
- Analyzed monthly expense trends
- Classified transactions into debit/credit
- Categorized transactions (UPI, cash, transfer, salary)

---

## 🔷 How to Run

```bash
cd src
python main.py
