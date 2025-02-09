# Task 3: COVID-19 Dashboard Development (Dash)

## 📌 Overview
This project is an **interactive COVID-19 dashboard** built using **Dash (Python)** and **Plotly**. It provides a **visual representation of COVID-19 cases worldwide**, including confirmed cases, deaths, and recoveries.

---

## 📌 Features
✔ **Global COVID-19 Cases Visualization** (Scatter Map)  
✔ **Top 10 Countries with Most Cases** (Bar Chart)  
✔ **COVID-19 Cases by WHO Region** (Pie Chart)  
✔ **Total Cases, Deaths, Recovered & Active Cases Summary**  

---

## 📌 Steps Performed

1️⃣ **Data Preprocessing**
   - Loaded the dataset: `covid-dashboard/country_wise_latest.csv`.
   - Cleaned missing values and added **Active Cases** column.

2️⃣ **Dashboard Development**
   - Created a **Scatter Geo Map** to visualize COVID-19 cases per country.
   - Added a **Bar Chart** for the top 10 most affected countries.
   - Built a **Pie Chart** to show cases distribution by WHO regions.

3️⃣ **Interactivity Features**
   - **Dynamic visualizations** update automatically.
   - **Dark theme** for better UI experience.

---

## 📌 How to Run the Dashboard

### **1️⃣ Install Required Libraries**
Make sure you have Python installed. Install dependencies using:

```bash
pip install dash pandas plotly
