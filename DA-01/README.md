# DA-01: Enterprise Business Intelligence Suite

## Project Overview
This project uses Microsoft Power BI and SQL Server to analyze business performance across Sales, Finance, Human Resources (HR), and Procurement.

The project includes interactive dashboards, data preparation, data modelling, DAX calculations, Row-Level Security (RLS), and a local SQL Server automation demonstration for data cleaning and validation.

## Dashboards
- **Sales Performance:** Sales, cost, profit, profit margin, and sales trends.
- **Financial Performance:** Sales, profit, and comparisons by country and segment.
- **HR Analytics:** Employee counts, attrition, and department-level analysis.
- **Procurement Performance:** Purchase values, ordered and received quantities, and supplier performance.

The report also includes four drill-through detail pages for exploring the underlying records.

## Tools and Technologies
- Microsoft Power BI Desktop
- Power Query for data preparation and cleaning
- DAX for calculations and measures
- SQL Server 2025 Developer Edition
- SQL Server Management Studio (SSMS)
- SQL Server Agent for scheduled job execution
- T-SQL stored procedures for data cleaning and validation
- GitHub for project documentation and version control

## Interactive Features
- KPI cards and charts
- Interactive slicers
- Drill-through detail pages
- Row-Level Security configured and tested for the North America sales region

## SQL Server Data Cleaning and Automation

A local SQL Server automation workflow was added to demonstrate data cleaning, validation, execution logging, and scheduled processing.

### Implemented Components
- Created the `DA01_Business_Intelligence` database.
- Created a cleaned Financial Sample table: `dbo.Financial_Sample_Clean`.
- Created stored procedures for data cleaning and validation.
- Used `TRY_CONVERT` to safely convert Profit values into a numeric currency data type.
- Trimmed text values during the cleaning process.
- Created an `ETL_Run_Log` table to record execution details and status.
- Configured the SQL Server Agent job `DA01_Automated_ETL_Job`.
- Configured a daily schedule at 9:00 AM.

### Execution Result
The job was manually executed successfully. The latest recorded execution showed:
- Status: Success
- Records processed in the cleaned Financial Sample table: 700
- Error message: None

**Note:** The 700 records refer to the Financial Sample cleaned table, not all project datasets. The daily schedule is configured; a future scheduled execution still needs to be verified.

## Project Files
The repository includes:
- Power BI report (`DA-01_Business_Intelligence.pbix`)
- Project Documentation PDF (`DA-01_Project_Documentation.pdf`)
- User Guide PDF (`DA-01_User_Guide.pdf`)
- Project Reflection (`DA-01_Project_Reflection.docx`)
- Final Presentation (`DA-01_Final_Presentation.mp4`)

## How to Open
1. Install Microsoft Power BI Desktop.
2. Download the `.pbix` report from this repository.
3. Open the file in Power BI Desktop.
4. Use the report tabs, slicers, charts, and drill-through pages to explore the dashboards.

## Project Demo Videos

- **10-minute Power BI walkthrough:** [Watch the demo](https://drive.google.com/file/d/1LaQLJkyJ78Am_72jkfgpKUG3INpdD5YR/view?usp=sharing)
- **Short presentation video:** [Watch the short presentation](https://drive.google.com/file/d/14vnj29YNg-gZ-ahtPVEwNCYNC5Mc2VTn/view?usp=sharing)

### Final Presentation (Narrated)
[Watch the 10-Slide Final Presentation](https://drive.google.com/file/d/1pkm9wsznrfG7ou6CCyrh1nWAT7qmWkY2/view?usp=sharing)

## Project Notes and Scope
This project was developed as part of a Data Analytics internship project.

The SQL Server automation described above is a local SQL Server demonstration. Azure Data Factory integration and Power BI Service publishing or scheduled refresh have not yet been completed.

Dashboard results should be reviewed using the supplied Power BI report and data.

---

# DA_01_Business_Intelligence

Power BI dashboards and SQL Server data cleaning and validation for Sales, Finance, HR, and Procurement analytics.
