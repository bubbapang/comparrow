import pandas as pd

df = pd.DataFrame(columns=["idea"])  # or create a new DataFrame if the csv does not exist

# Read the output.txt file
with open("output.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

# Append new ideas into DataFrame
for line in lines:
    new_row_data = line.strip()  # Remove newline character
    df.loc[len(df)] = [new_row_data]  # Append new row using df.loc

# Save DataFrame to CSV file
df.to_csv("data/list1.csv", index=False)
