import pandas as pd
import numpy as np

#Data Analysis Class
class HealthcareAnalysis:
    """Performs analysis on a cleaned healthcare Dataframe.

    Analysis techniques covered:
    - Descriptive statistics (mean, median, std, percentiles via NumPy)
    - Grouping and aggregation (billing by gender, condition, insurance)
    - Correlation analysis (Age vs Billing Amount)
    - Frequency distributions (medical conditions, test results)
    - Derived features (length of stay, age groups)
    """
    
    def __init__(self, df):
        """Initialize data"""
        self.df = df

    def dataset_information(self):
        """Dataset information"""
        print(f"\n \n DATASET INFORMATION \n {self.df.info()}")

    def stat_summary(self):
        """Statistical information summary"""
        print('\n \n STATISTICAL DATA')
        print(self.df.describe())

    def gender_distribution(self):
        """Analyze gender distribution"""
        print('\n \n GENDER DESCRIPTION')
        counts = (self.df['Gender'].value_counts())
        percentages = np.round((counts.values / counts.sum()) * 100, 2)
        for i in range(len(counts)): #demonstrates in numbers and percentages
            gender = counts.index[i]
            count = counts.values[i]
            pct = percentages[i]
            print(f"{gender}: {count} ({pct}%)")

    def common_conditions(self):
        """Print the proportion and frequency of each medical condition"""
        print("\n \n MEDICAL CONDITION FREQUENCY")
        counts = self.df['Medical Condition'].value_counts()
        for condition, count in counts.items(): ##demonstrates in numbers and percentages
            pct = np.round(count / len(self.df) * 100, 2)
            print(f"{condition}: {count} ({pct}%)")

    def avg_billing(self):
        """Average Billing Amount"""
        print('\n \n BILLING AMOUNT ANALYSIS')
        print(self.df['Billing Amount'].mean())

    def highest_billing(self):
        """Top 10 highest bills"""
        highest_bills = self.df.sort_values( by = 'Billing Amount', ascending = False)
        print(highest_bills.head(10))

    def correlation_analysis(self):
        """Compute and print correlation between numeric variables"""
        print("\n \n CORRELATION ANALYSIS")

        numeric_cols = ["Age", "Billing Amount", "Room Number"]
        corr_matrix = self.df[numeric_cols].corr()
        print(corr_matrix.round(4).to_string())

        # numpy verification of age and billing amount
        r = np.corrcoef(
            self.df["Age"].values,
            self.df["Billing Amount"].values
        )[0,1]
        print(f"\n Age vs Billing Amount: {r}")
        if abs(r) < 0.1:
            print("Interpretation: Very weak / no linear relationship.")
        elif abs(r) < 0.3:
            print("Interpretation: Weak linear relationship.")
        elif abs(r) < 0.5:
            print("Interpretation: Moderate linear relationship.")
        else:
            print("Interpretation: Strong linear relationship.")
        
    def age_group_analysis(self):
        """Segment patients into age groups and analyse billing per segment."""
        print("\n \n AGE GROUP ANALYSIS")
        
        # assign each patient to an age group
        age_groups = []
        for age in self.df["Age"]:
            if age < 18:
                age_groups.append('Minor (0-17)')
            elif age < 36:
                age_groups.append('Young Adult (18-35)')
            elif age < 56:
                age_groups.append('Middle Age (35-55)')
            elif age < 71:
                age_groups.append('Senior (56-70)')
            else:
                age_groups.append('Elderly (70+)')

        self.df = self.df.copy()
        self.df['Age Group'] = age_groups

        # print results for each group
        groups = ['Minor (0-17)', 'Young Adult (18-35)', 'Middle Age (35-55)', 'Senior (56-70)','Elderly (70+)']

        for group in groups:
            group_df = self.df[self.df['Age Group'] == group]
            count = len(group_df)
            avg = round(group_df['Billing Amount'].mean(),2)
            median = round(group_df['Billing Amount'].median(),2)
            print(f"{group}: {count} patients, Avg: {avg}, Median:{median}")



