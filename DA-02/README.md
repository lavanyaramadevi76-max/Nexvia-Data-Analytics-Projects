# DA-02: Customer 360 and Marketing Attribution Platform

## 1. Project Overview

DA-02 is a Customer 360 and Marketing Attribution analytics project built using Google BigQuery, SQL, dbt Core, Tableau, and Python.

The project uses the Google Analytics 4 public ecommerce sample dataset to analyze customer activity, orders, customer value, segmentation, and marketing attribution.

## 2. Technologies Used

- Google BigQuery – Cloud data warehouse
- SQL – Data preparation and analytics
- dbt Core – Data transformation, model management, and testing
- Tableau – Dashboard development and visualization
- Python – CSV validation
- GitHub – Project version control and documentation

## 3. Data Architecture

The project processes ecommerce data in BigQuery and prepares analytical datasets for customer and marketing analysis.

Main processing areas:

- GA4 ecommerce sample data
- Customer and identity mapping tables
- Session and order preparation
- Customer 360 analytics
- RFM customer segmentation
- Historical Customer Lifetime Value (CLV)
- Marketing attribution analysis
- Tableau dashboard and Python validation

See `DA02_Customer360_Architecture_Diagram.md` for the architecture diagram.

## 4. dbt Implementation

The dbt project connects to the existing BigQuery `customer360` dataset.

### Implemented dbt models

| Model | Source table | Materialization |
|---|---|---|
| stg_sessions | sessions | View |
| stg_orders | orders_clean | View |
| customer_360_dbt | customer_360 | Table |

### dbt activities completed

- Configured dbt Core and BigQuery connection.
- Configured source definitions.
- Created staging and mart models.
- Executed dbt models successfully.
- Added data quality tests.
- Executed dbt tests successfully.
- Generated dbt documentation
- Verified model dependencies using the dbt lineage graph.

### Verified model row counts

| Model | Rows |
|---|---:|
| stg_sessions | 360,129 |
| stg_orders | 4,466 |
| customer_360_dbt | 270,154 |

### Data quality

Three configured `not_null` tests passed for:
- stg_sessions.user_pseudo_id
- stg_orders.order_id
- stg_orders.customer_id

## 5. Customer Analytics

The project includes:

- Customer 360 analysis
- RFM segmentation
- Historical Customer Lifetime Value analysis
- Customer purchase and revenue analysis
- Marketing channel attribution

## 6. Marketing Attribution

The attribution prototype compares first-touch, last-touch, linear, and time-dec
