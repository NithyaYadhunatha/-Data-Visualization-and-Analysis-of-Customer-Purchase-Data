# -Data-Visualization-and-Analysis-of-Customer-Purchase-Data


## 🚀 Overview
This project is designed to **clean, analyze, and visualize customer purchase data** using Python. The goal is to automate data preprocessing and generate meaningful insights through statistical analysis and visualizations.

## 📂 Project Structure
```
├── data/                     # Folder for raw and cleaned datasets
│   ├── sample_customer_data.csv
├── output/                   # Folder for storing generated visualizations
├── src/                      # Source code
│   ├── data_cleaner.py        # Data cleaning and visualization script
├── README.md                  # Project documentation
└── requirements.txt            # Required Python libraries
```

## 🔹 Features
✅ **Data Cleaning**
- Handles missing values, fills income data with the median, and filters invalid data.
- Removes duplicate records for accurate analysis.

✅ **Data Analysis & Reporting**
- Computes descriptive statistics for customer demographics and purchases.
- Generates an automated report with dataset insights.

✅ **Data Visualization**
- **Histograms** – Distribution of purchase amounts.
- **Box Plots** – Purchase amount variations by category.
- **Scatter Plots** – Relationship between age, income, and purchases.
- **Pie Charts** – Customer category distribution.

## 📊 Example Visualizations
Sample output visualizations include:
- **Purchase Distribution Histogram** 📈
- **Purchase by Category Box Plot** 📦
- **Age vs Purchase Scatter Plot** 🎯
- **Category-wise Pie Chart** 🥧

## 🛠️ Installation & Usage
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Script
```bash
python src/data_cleaner.py
```

## 📂 Dataset Requirements
The dataset should contain numeric fields like `age`, `income`, and `purchase_amount`, along with at least one categorical column (e.g., `customer_category`).

## 📌 Technologies Used
- **Python** 🐍
- **Pandas** 📊
- **Matplotlib & Seaborn** 🎨

## 💡 Applications
This project is useful for:
✔ Business Intelligence
✔ Customer Behavior Analysis
✔ Sales Data Exploration

## 🏆 Future Enhancements
- Implement **interactive dashboards** using Plotly or Streamlit.
- Extend the project for **real-time data analysis** with live customer data.

