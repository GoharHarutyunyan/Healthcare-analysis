import pandas as pd
import matplotlib.pyplot as plt

#Data Visualization Class
class HealthcareVisual:
    """Generates visalization for cleaned healthcare DataFrame.

    Visualization types used:
    - Bar chart (gender distribution, average billing by gender)
    - Pie chart (medical condition distribution)
    - Histogram (billing amount distribution)
    """

    def __init__(self, df):
        """Initialize with a healthcare DataFrame"""
        self.df = df

    def gender_vis(self):
        """Display a bar chart of gender distribution"""
        self.df['Gender'].value_counts().plot(kind = 'bar')
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.show()

    def condition_vis(self):
        """"Display pie chart of top 10 medican conditions"""
        counts = self.df['Medical Condition'].value_counts().head(10)
        plt.figure(figsize = (8, 8))
        plt.pie(counts, labels = counts.index, autopct='%1.1f%%', startangle = 90)
        plt.title('Top Medical Conditions')
        plt.tight_layout()
        plt.show()
     
    def billing_distribution_vis(self):
        """Display a histogram of billing amount distribution"""
        plt.hist(self.df['Billing Amount'], bins = 18)
        plt.title('Billing Amount Distribution')
        plt.xlabel('Billing Amount')
        plt.ylabel('Frequency')
        plt.show()

    def avg_billing_by_gender_vis(self):
        '''Display a bar chart of average billing amount by gender'''
        self.df.groupby('Gender')['Billing Amount'].mean().plot(kind = 'bar')
        plt.title('Average Billing by Gender')
        plt.xlabel('Gender')
        plt.ylabel('Average Billing')
        plt.show()


