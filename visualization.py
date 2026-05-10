import pandas as pd
import matplotlib.pyplot as plt

#Data Visualization Class
class HealthcareVisual:
    def __init__(self, df):
        self.df = df

    #Gender distribution

    def gender_vis(self):
        self.df['Gender'].value_counts().plot(kind = 'bar')
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.show()

    
    #Medical Condition Distribution

    def condition_vis(self):
        self.df['Medical Condition'].value_counts().head(10).plot(kind = 'bar')
        plt.title('Top Medical Conditions')
        plt.xlabel('Condition')
        plt.ylabel('Count')
        plt.show()

    
    #Billing Distribution
    
    def billing_distribution_vis(self):
        plt.hist(self.df['Billing Amount'], bins = 18)
        plt.title('Billing Amount Distribution')
        plt.xlabel('Billing Amount')
        plt.ylabel('Frequency')
        plt.show()

    
    #Average billing by gender

    def avg_billing_by_gender_vis(self):
        self.df.groupby('Gender')['Billing Amount'].mean().plot(kind = 'bar')
        plt.title('Average Billing by Gender')
        plt.xlabel('Gender')
        plt.ylabel('Average Billing')
        plt.show()

