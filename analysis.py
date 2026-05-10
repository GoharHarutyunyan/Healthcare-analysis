import pandas as pd
import matplotlib.pyplot as plt

#Data Analysis Class
class HealthcareAnalysis:
    def __init__(self, df):
        self.df = df


    #dataset information
    def dataset_information(self):
        print (self.df.info())

    
    #statistical information summary
    def stat_summary(self):
        print('---statistical data---')
        print(self.df.describe())


    #Analyzing gender distribution
    def gender_distribution(self):
        print('---Gender Distribution---')
        print(self.df['Gender'].value_counts())

    
    #analyze medical conditions
    def common_conditions(self):
        print(self.df['Medical Condition'].value_counts())


    #Average Billing Amount
    def avg_billing(self):
        print('---Average Billing Amount')
        print(self.df['Billing Amount'].mean())


    #Top 10 highest bills
    def highest_billing(self):
        highest_bills = self.df.sort_values( by = 'Billing Amount', ascending = False)
        print(highest_bills.head(10))

    