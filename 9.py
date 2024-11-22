import pandas as pd
extended_sales_data = {
    "OrderDate": ["1-6-18", "1-23-18", "2-9-18", "2-26-18", "3-15-18", "4-1-18", "4-18-18", "5-5-18", "5-22-18"],
    "Region": ["East", "Central", "Central", "Central", "West", "East", "Central", "Central", "West"],
    "Manager": ["Martha", "Hermann", "Hermann", "Timothy", "Timothy", "Martha", "Martha", "Hermann", "Douglas"],
    "SalesMan": ["Alexander", "Shelli", "Luis", "David", "Stephen", "Alexander", "Steven", "Luis", "Michael"],
    "Item": ["Television", "Home Theater", "Television", "Cell Phone", "Television", "Home Theater", "Television", "Television", "Television"],
    "Units": [95, 50, 36, 27, 56, 60, 75, 90, 32],
    "Unit_price": [1198, 500, 1198, 225, 1198, 500, 1198, 1198, 1198]
}
extended_sales_df = pd.DataFrame(extended_sales_data)
extended_sales_df['Sale_amt'] = extended_sales_df['Units'] * extended_sales_df['Unit_price']
pivot_sales_summary = extended_sales_df.pivot_table(
    values='Sale_amt', 
    index=['Region', 'Manager', 'SalesMan'], 
    aggfunc='sum'
)
print(pivot_sales_summary)
