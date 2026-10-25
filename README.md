# Retail Sales Analysis and Visualization

**Portfolio:** Muhammad Awais  
**Stack:** Python, pandas, matplotlib

## Project overview
This project explores **500 synthetic retail transactions** across four product categories. It calculates revenue, identifies the most frequently purchased products, and visualizes monthly sales trends. All prices are illustrative Pakistani rupees (PKR), not actual store transactions.

## Questions
- How does revenue vary by month?
- Which category generates the most revenue?
- Which products sell the most units?
- What is the average order value?

## Run locally
Use Python 3.10+ and open a terminal in the project folder:

```bash
python -m pip install -r requirements.txt
python -m src.analysis
python -m unittest discover -s tests -v
```

## Repository structure
- `data/retail_sales.csv`: example dataset
- `src/analysis.py`: validation, grouping, summaries and plots
- `outputs/`: CSV reports, JSON summary and three PNG charts
- `tests/`: automated smoke test
- `PROJECT_GUIDE.md`: explanation and suggested improvements

## Results
The supplied dataset produces **500 orders**, **PKR 4,067,056 total revenue**, **1,570 units sold**, and **PKR 8,134.11 average order value**. The highest-revenue category is **Electronics**, and the top product by units is **Headphones**. These are synthetic-data findings, not real-world business claims.

The exact computed summary is stored in [`outputs/summary.json`](outputs/summary.json). Monthly, category, and product aggregations are saved as CSV files.

![Monthly revenue](outputs/monthly_revenue.png)
![Category revenue](outputs/category_revenue.png)
![Top products](outputs/top_products.png)

## Interpretation
Revenue is calculated as `quantity × unit_price_pkr`. This is a descriptive analysis only; synthetic trends do not establish real business performance. No refunds, discounts, taxes, or costs are included, so revenue is **not profit**.

## Next steps
Add returns and discounts, compare quarterly trends, and use a real dataset with a clear license and source.

## About this portfolio project
This repository documents a learning-oriented analysis project maintained for the portfolio of **Muhammad Awais**. The included dataset is simulated; results are illustrative. See `PROJECT_GUIDE.md` for reproduction and extension ideas.
