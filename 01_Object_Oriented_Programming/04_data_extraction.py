"""
Topic: Data Extraction
Description: Demonstrates reading different file formats using the pandas library.
Author: Suryansh
"""

import pandas as pd

# ============================================
# Data Extractor Class
# ============================================

class DataExtractor:

    # Constructor
    def __init__(self, file_path: str):
        self.file_path = file_path

    # Method to read a CSV/Text file
    def fetch_text(self, separator: str):

        df = pd.read_csv(self.file_path, sep=separator)

        print(df.head())   # Displays the first 5 rows

    # Method to read a JSON file
    def fetch_json(self):

        df = pd.read_json(self.file_path)

        print(df.head())

    # Method to read a Parquet file
    def fetch_parquet(self):

        df = pd.read_parquet(self.file_path)

        print(df.head())


# ============================================
# Creating Object
# ============================================

# Pass the file path while creating the object
obj = DataExtractor("your_file_path_here")

# Reading a CSV/Text file
obj.fetch_text(",")      # Pass the separator (e.g. ',' or '\t')

# Reading a JSON file
# obj.fetch_json()

# Reading a Parquet file
# obj.fetch_parquet()