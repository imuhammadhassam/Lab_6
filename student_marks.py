
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a messy dataset
data = {
    "Name": [" ali", "SARA ", "bilal", " Ayesha",
             "HAMZA", "zain ", "Noor", " usman "],
    "Marks": ["72", "85", "absent", "64",
              "90", "78", "81", "69"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Clean student names
df["Name"] = df["Name"].str.strip().str.title()

# Step 3: Convert marks into numbers
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Step 4: Replace absent with the mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset:")
print(df)

# Step 5: Create bar chart
plt.figure(figsize=(9, 5))
plt.bar(df["Name"], df["Marks"], color="steelblue")

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()

# Step 6: Save the graph
plt.savefig("marks_bar.png")

print("\nSaved marks_bar.png")
plt.show()
