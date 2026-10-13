
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# STEP 1: Create a messy weather dataset
data = {
    "Date": [
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-07", "2026-01-08", "2026-01-09",
        "2026-01-10", "2026-01-11", "2026-01-12",
        "2026-01-13", "2026-01-14", "2026-01-15",
        "2026-01-03"
    ],
    "City": [
        " lahore", "LAHORE ", "Lahore", "lahore",
        " Lahore ", "LAHORE", "lahore ", "Lahore",
        "LAHORE", " lahore", "Lahore", "lahore",
        "LAHORE ", "Lahore", " lahore", "Lahore"
    ],
    "Temperature": [
        "32C", "28C", "35C", "30C", "26C",
        "33C", "27C", "31C", "29C", "34C",
        "25C", "36C", "30C", "28C", "33C", "35C"
    ],
    "Humidity": [
        45, 60, 40, np.nan, 70,
        50, 65, 55, np.nan, 42,
        75, 38, 58, np.nan, 48, 40
    ],
    "Condition": [
        "sunny", " CLOUDY", "Sunny ", " Rainy",
        "CLOUDY ", "sunny", "Cloudy", " SUNNY",
        "rainy ", "Sunny", " Rainy", "sunny",
        "Cloudy ", " sunny", "CLOUDY", "Sunny "
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# STEP 2: Clean City and Condition columns
df["City"] = df["City"].str.strip().str.title()
df["Condition"] = df["Condition"].str.strip().str.title()

# STEP 3: Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# STEP 4: Remove C suffix from Temperature
df["Temperature"] = (
    df["Temperature"]
    .str.replace("C", "", regex=False)
)

df["Temperature"] = pd.to_numeric(
    df["Temperature"], errors="coerce"
)

# STEP 5: Remove duplicate rows
df = df.drop_duplicates().copy()

print("\nRows after dropping duplicates:", len(df))

# STEP 6: Fill missing humidity with median
median_humidity = df["Humidity"].median()

df["Humidity"] = df["Humidity"].fillna(median_humidity)

print("Missing Humidity filled with median:", median_humidity)

# STEP 7: One-hot encode Condition
df_encoded = pd.get_dummies(
    df, columns=["Condition"], dtype=int
)

print("\nEncoded Condition Columns:")
print(df_encoded.filter(like="Condition_").head())

# STEP 8: Print cleaned dataset
print("\nCleaned Weather Dataset:")
print(df)

# STEP 9: Calculate correlation
correlation = df["Temperature"].corr(df["Humidity"])

print(
    "\nCorrelation (Temperature, Humidity):",
    round(correlation, 3)
)

# STEP 10: Count weather conditions
condition_counts = df["Condition"].value_counts()

print("\nCondition Counts:")
print(condition_counts)

# STEP 11: Sort data by date
df = df.sort_values("Date")

# STEP 12: Create 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Plot 1: Line plot
axes[0, 0].plot(
    df["Date"],
    df["Temperature"],
    marker="o",
    color="steelblue"
)

axes[0, 0].set_title("Temperature Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Temperature (C)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Scatter plot
axes[0, 1].scatter(
    df["Temperature"],
    df["Humidity"],
    color="darkorange",
    s=60
)

axes[0, 1].set_title("Temperature vs Humidity")
axes[0, 1].set_xlabel("Temperature (C)")
axes[0, 1].set_ylabel("Humidity (%)")
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Pie chart
axes[1, 0].pie(
    condition_counts.values,
    labels=condition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[1, 0].set_title("Weather Condition Distribution")

# Plot 4: Histogram
axes[1, 1].hist(
    df["Temperature"],
    bins=5,
    color="seagreen",
    edgecolor="white"
)

axes[1, 1].set_title("Temperature Distribution")
axes[1, 1].set_xlabel("Temperature (C)")
axes[1, 1].set_ylabel("Number of Days")

# STEP 13: Save dashboard
fig.suptitle("Weather Overview", fontsize=16)

plt.tight_layout()
plt.savefig("weather_dashboard.png", dpi=300)

print("\nSaved weather_dashboard.png")
plt.show()
