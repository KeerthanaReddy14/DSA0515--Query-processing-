import pandas as pd
sales_data = {
    "OrderDate": ["1-6-18", "1-23-18", "2-9-18", "2-26-18", "3-15-18", "4-1-18", "4-18-18", "5-5-18", "5-22-18"],
    "Item": ["Television", "Home Theater", "Television", "Cell Phone", "Television", "Home Theater", "Television", "Television", "Television"],
    "Units": [95, 50, 36, 27, 56, 60, 75, 90, 32],
    "Unit_price": [1198, 500, 1198, 225, 1198, 500, 1198, 1198, 1198]
}
sales_df = pd.DataFrame(sales_data)
pivot_units_sold = sales_df.pivot_table(values='Units', index='Item', aggfunc='sum')
print(pivot_units_sold)
