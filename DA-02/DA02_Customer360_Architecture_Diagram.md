# DA-02 Customer 360 – Architecture Diagram

## 1. End-to-End Data Flow

```mermaid
flowchart TD
    A["GA4 Public Ecommerce Sample Data"] --> B["Google BigQuery"]
    B --> C["SQL Data Preparation and Cleaning"]
    C --> D["Sessions Dataset"]
    C --> E["Cleaned Orders Dataset"]

    F["Synthetic CRM Customer Profiles"] --> H["Customer Identity Mapping"]
    D --> H
    E --> H

    H --> I["Customer 360 Dataset"]

    I --> J["RFM Customer Segmentation"]
    I --> K["Historical Customer Lifetime Value"]
    D --> L["Acquisition Channel Attribution Prototype"]
    E --> L

    M["Synthetic Advertising Spend"] --> N["Campaign Performance Analysis"]
    L --> N

    I --> O["CSV Exports"]
    J --> O
    K --> O
    L --> O
    N --> O

    O --> P["Tableau Dashboards"]
    O --> Q["Python CSV Validation"]

    B --> R["dbt Transformation Project"]
    R --> S["stg_sessions View"]
    R --> T["stg_orders View"]
    R --> U["customer_360_dbt Table"]
```

## 2. Technology Architecture

| Layer | Technology | Purpose |
|---|---|---|
| Data Source | GA4 Sample Dataset | Ecommerce events |
| Data Warehouse | Google BigQuery | Data storage and querying |
| Transformation | SQL | Cleaning and preparation |
| Transformation Framework | dbt Core | Modular models and tests |
| Analytics | SQL | RFM, CLV and attribution |
| Visualization | Tableau | Interactive dashboards |
| Validation | Python | CSV validation |
| Version Control | GitHub | Project management |

## 3. dbt Model Flow

```mermaid
flowchart TD
    A["BigQuery customer360 Dataset"] --> B["stg_sessions"]
    A --> C["stg_orders"]
    A --> D["customer_360"]
    B --> E["dbt Data Tests"]
    C --> E
    D --> F["customer_360_dbt"]
```

## 4. Important Limitations

- CRM profiles and advertising spend are synthetic.
- Identity mapping is deterministic and does not demonstrate verified cross-device identity resolution.
- Attribution uses first-user acquisition information as a proxy, not full session-level journeys.
- Campaign ROI and CPA cannot be reliably calculated because campaign names do not exactly match.
- The dbt Customer 360 model references an existing BigQuery table rather than rebuilding the entire pipeline.

## 5. Project Outcome

The architecture demonstrates how GA4 sample data, BigQuery, SQL, dbt, Tableau and Python work together in a Customer 360 analytics prototype.