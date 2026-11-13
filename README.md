# MIT 8339 – Business Intelligence and Decision Support Systems (Virtual Lab)

**Customer Retention and Performance Intelligence for a Nigerian Commercial Bank**


This repository holds the supporting files for my single-PDF submission.

## Files

| File | What it is |
|---|---|
| `BankChurners_cleaned.csv` | Cleaned dataset (10,127 rows × 34 columns) produced by the notebook |
| `MIT8339_BI_Lab_Notebook.ipynb` | Python notebook with all data preparation, KPI and risk-score code, with outputs |
| `MIT8339_BI_Dashboard.html` | Interactive two-page dashboard (Plotly). Download and open in any browser; works offline |
| `build_dashboard.py` | Script that builds the dashboard from the cleaned CSV |
| `dash_template.html` | Dashboard layout, filters and chart code used by `build_dashboard.py` |

## Dataset source

Goyal, S. (2020). *Credit card customers* [Data set]. Kaggle. https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers

The raw file (`BankChurners.csv`) is not redistributed here; download it from Kaggle to re-run the notebook.

## How to reproduce

1. Download `BankChurners.csv` from the Kaggle link above and place it in the same folder as the notebook.
2. Install Python 3 and run `pip install pandas numpy scipy matplotlib plotly jupyter`.
3. Open `MIT8339_BI_Lab_Notebook.ipynb` and choose **Run All**. This writes `BankChurners_cleaned.csv`.
4. Run `python build_dashboard.py` (with `dash_template.html` in the same folder) to rebuild `MIT8339_BI_Dashboard.html`.
5. Open the dashboard in a browser and use the drop-down filters and the two page tabs.

## Key results

- Attrition rate: 16.1% (1,627 of 10,127 customers)
- High retention-risk band: 1,567 customers, 63.9% attrition, 61.6% of all attrition
