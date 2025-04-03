import pandas as pd

# Load the Excel file
df = pd.read_excel("DATASET.xlsx")

# Convert to CSV
df.to_csv("DATASET.csv", index=False)
