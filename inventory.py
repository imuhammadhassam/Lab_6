
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a messy product inventory dataset
data = {
    "Product": [
        "Cola", "Chips", "Milk", "Biscuits", "Juice",
        "Cheese", "Water", "Chocolate", "Yogurt", "Coffee"
    ],
    "Category": [
        "beverages ", "SNACKS", " Dairy", "Snacks",
        "beverages", "DAIRY ", "Beverages",
        " snacks ", "dairy", "BEVERAGES"
    ],
    "Price": [
        "Rs. 1,250", "Rs. 90", "Rs. 450", "Rs. 120",
        "Rs. 1,800", "Rs. 750", "Rs. 100",
        "Rs. 300", "Rs. 200", "Rs. 950"
    ],
    "Stock": [40, 120, 60, 100, 35, 25, 200, 80, 55, 45]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Clean category names
df["Category"] = df["Category"].str.strip().str.title()

# Step 3: Convert Price to numeric values
df["Price"] = (
    df["Price"]
    .str.replace("Rs. ", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# Step 4: Label encode Category
df["Category_Code"] = df["Category"].astype("category").cat.codes

print("\nCleaned and Encoded Dataset:")
print(df)

# Step 5: Calculate values for visualization
avg_price = df.groupby("Category")["Price"].mean()
total_stock = df.groupby("Category")["Stock"].sum()

print("\nAverage Price by Category:")
print(avg_price)

print("\nTotal Stock by Category:")
print(total_stock)

# Step 6: Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot
axes[0].bar(
    avg_price.index,
    avg_price.values,
    color=["steelblue", "orange", "seagreen"]
)
axes[0].set_title("Average Price by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Average Price (Rs.)")

# Pie chart
axes[1].pie(
    total_stock.values,
    labels=total_stock.index,
    autopct="%1.1f%%",
    startangle=90
)
axes[1].set_title("Stock Share by Category")

# Step 7: Save and display plots
plt.tight_layout()
plt.savefig("inventory_plots.png", dpi=300)

print("\nSaved inventory_plots.png")
plt.show()
