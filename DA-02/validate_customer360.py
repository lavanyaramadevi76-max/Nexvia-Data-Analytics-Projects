"""
DA-02 Customer 360 - CSV data quality checks
Run: python validate_customer360.py
Place this script in the same folder as the five exported CSV files.
Uses only Python's standard library.
"""

import csv
from pathlib import Path

FILES = {
    "monthly_sales_summary.csv": ["order_date", "total_orders", "total_revenue"],
    "customer_segment_summary.csv": ["segment"],
    "clv_summary.csv": ["clv_segment"],
    "channel_dashboard.csv": ["source", "medium"],
    "campaign_performance.csv": [],
}

def inspect_csv(filename, required_columns):
    path = Path(filename)
    if not path.exists():
        return {"file": filename, "status": "MISSING", "rows": 0, "details": "File not found"}

    try:
        with path.open("r", newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []
            missing = [col for col in required_columns if col not in headers]
            rows = list(reader)

        if missing:
            return {
                "file": filename, "status": "CHECK", "rows": len(rows),
                "details": "Missing expected columns: " + ", ".join(missing)
            }

        return {
            "file": filename, "status": "PASS", "rows": len(rows),
            "details": "Columns present: " + ", ".join(headers)
        }
    except Exception as exc:
        return {"file": filename, "status": "ERROR", "rows": 0, "details": str(exc)}

def main():
    print("DA-02 CUSTOMER 360 - DATA QUALITY REPORT")
    print("=" * 55)
    results = [inspect_csv(name, columns) for name, columns in FILES.items()]

    for result in results:
        print(f"\n{result['status']}: {result['file']}")
        print(f"Rows: {result['rows']}")
        print(result["details"])

    passed = sum(r["status"] == "PASS" for r in results)
    print("\n" + "=" * 55)
    print(f"Files passing basic checks: {passed}/{len(results)}")
    print("Note: These checks verify file presence and expected headers only.")
    print("They do not validate business logic, campaign matching, or attribution accuracy.")

if __name__ == "__main__":
    main()
