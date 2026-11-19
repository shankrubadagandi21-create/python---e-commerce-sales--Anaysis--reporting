# calulate monthly sales:
# How many revenue did we generate each month?
# Extract the month from the order date

completed_sales["sales_month"] = (
    completed_sales["order_date"].dt.to_period("M")
)
monthly_sales =(
    completed_sales.groupby("sales_month")["revenue"].sum()
)
monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(10,5)
)
pit.title("Monthly Revnue Trend")
pit.xlabel("Month")
pit.ylabel("Rvenue")
pit.xticks(rotation= 45)
pit.tight_layout()
pit.show()
