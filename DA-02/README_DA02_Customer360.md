# Customer 360 and Marketing Attribution Platform

**DA-02 | BigQuery + Tableau Public**

## Overview
A Customer 360 analytics prototype using the public GA4 obfuscated ecommerce sample dataset in BigQuery, supplemented with synthetic CRM-style customer profiles and synthetic advertising spend data. Tableau Public visualizes sales, customer segments, historical CLV and acquisition-channel summaries.

## Dashboard
- Monthly Revenue Trend
- Monthly Orders
- Customer Segmentation
- Customer Lifetime Value
- Marketing Channel Performance

Packaged Tableau workbook: `DA02_Customer360_Final.twbx`

## Key results
- 360,129 sessions; 270,154 unique users; 1,350,428 page views.
- Cleaned orders: 4,466 rows; 4,451 distinct order IDs.
- Monthly revenue: Nov 2020 $92,964; Dec 2020 $158,986; Jan 2021 $56,880.
- RFM: No Purchase 265,754; Recent Customers 2,717; Needs Attention 1,535; Loyal Customers 114; Champions 34.
- Historical CLV average: about $82.01 across 4,400 purchasing customers.

## Important limitations
- CRM-style customer data and ad spend are synthetic.
- Identity mapping is deterministic for available GA4 pseudo-user IDs; it is not verified cross-device identity resolution.
- Attribution is a prototype based on first-user acquisition source data, not true session-level touchpoints.
- Synthetic campaign names did not exactly match GA4 campaign names. Campaign ROI and CPA are therefore not validly measurable and must not be fabricated.
- CLV is historical, not predictive; annualized estimates may be distorted by the short observation window.
- dbt, Python pipeline, Segment integration and production CRM integration are not evidenced as completed in this workspace.

## Reproducibility
The BigQuery SQL tables and queries should be exported into a `/sql` folder before submission. Include the Tableau packaged workbook and this documentation. Add screenshots of the dashboard and BigQuery validation results.

## Suggested repository structure
```text
DA02-Customer360/
├── README.md
├── docs/
│   ├── DA02_Customer360_Project_Documentation.pdf
│   └── DA02_Customer360_Project_Documentation.docx
├── tableau/
│   └── DA02_Customer360_Final.twbx
├── sql/
│   └── (exported BigQuery SQL scripts)
└── screenshots/
    └── (dashboard and validation screenshots)
```

## Presentation outline
1. Problem and objective
2. Data sources and synthetic data disclosure
3. BigQuery architecture and data cleaning
4. RFM and historical CLV
5. Attribution and channel findings
6. Tableau dashboard
7. Limitations and recommendations
