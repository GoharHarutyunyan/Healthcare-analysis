import numpy as np
import pandas as pd

# Data Cleaning Class

class DataCleaning:
    """Handles
    - duplicate row removal
    - missing value handling
    - data type correction(str to int, float)
    - name normalization
    - invalid value improvement(negative billings)
    """
    def __init__(self, df):
        """initialize data"""
        self.df = df

    def remove_duplicates(self): 
        """remove fully duplicate rows from dataset"""
        before_removing = self.df.shape[0] #row count before cleaning
        self.df = self.df.drop_duplicates()
        after_removing = self.df.shape[0] #row count after cleaning

        #demonstate how many rows were removed
        print(f'{before_removing - after_removing} duplicate rows were removed') 

    def handle_missing_values(self):
        """handle missing or invalid values in the dataset"""

        # changes missing values with median 
        median_billing = np.median(self.df["Billing Amount"].dropna().values)
        self.df['Billing Amount'] = self.df['Billing Amount'].fillna(median_billing)

        self.df = self.df.dropna() #dropes all other missing values

        neg_count = (self.df['Billing Amount'] < 0).sum()
        self.df = self.df[self.df['Billing Amount'] >= 0] #dropes negative values
        print(f'Missing values handled! Removed {neg_count} negative billing rows.')

    def fix_data_types(self):
        """fix column data types so they match their meaning"""

        # change string date columns into date format 
        for col in ("Date of Admission", "Discharge Date"):
            self.df[col] = pd.to_datetime(self.df[col], dayfirst=True) #converts string into datetime object for easier access, checks the format dd.mm.yyyy

        # ensures billing is numeric
        self.df["Billing Amount"] = pd.to_numeric(self.df["Billing Amount"])

        # normalise messy name capitalization 
        self.df["Name"] = self.df["Name"].str.title()

        # make sure age and room numbers are stored as whole numbers
        for col in ("Age", "Room Number"):
            self.df[col] = self.df[col].astype(np.int64)

        print("Data types corrected. Dates converted, billing numeric and names normalized.")

    def get_cleaned_data(self):
        """return the fully cleaned DataFrame"""
        return self.df
