import pandas as pd
df = pd.read_excel("XLms.xlsx", engine="openpyxl")
print(df.head)
df = pd.read_excel("XLms.xlsx", sheet_name="Sheet1", engine="openpyxl")
import pandas as pd  # Import pandas library

# Load the Excel file
df = pd.read_excel("XLms.xlsx", engine="openpyxl")  # Replace "XLms.xlsx" with your file name

# Display the first few rows
print(df.head())