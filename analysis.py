import pandas as pd
import numpy as np

df = pd.read_csv('healthcare_dataset.csv')

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
        """initialize data"""
        self.df = df

    def dataset_information(self):
        """dataset information"""
        print(f"\n \n DATASET INFORMATION \n {self.df.info()}")

    def stat_summary(self):
        """statistical information summary"""
        print('\n \n STATISTICAL DATA')
        print(self.df.describe())

    def gender_distribution(self):
        """analyze gender distribution"""
        print('\n \n GENDER DESCRIPTION')
        counts = (self.df['Gender'].value_counts())
        percentages = np.round((counts.values / counts.sum()) * 100, 2)
        for i in range(len(counts)): #demonstrates in numbers and percentages
            gender = counts.index[i]
            count = counts.values[i]
            pct = percentages[i]
            print(f"{gender}: {count} ({pct}%)")

    def common_conditions(self):
        """print the proportion and frequency of each medical condition"""
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



analysis = HealthcareAnalysis(df)
analysis.dataset_information()
analysis.stat_summary()
analysis.gender_distribution()
analysis.common_conditions()
analysis.avg_billing()
analysis.highest_billing()

