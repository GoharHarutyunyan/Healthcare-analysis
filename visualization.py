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
        """"Display pie chart of top 10 medical conditions"""
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

    def correlation_vis(self):
        """Display a heatmap of correlation between numeric variables"""
        import seaborn as sns

        numeric_columns = ['Age', 'Billing Amount', "Room Number"]
        corr_matrix = self.df[numeric_columns].corr()
        plt.figure(figsize=(6, 5))
        sns.heatmap(corr_matrix, annot = True, fmt = '.4f', cmap = 'coolwarm')
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show() 

    def age_group_vis(self):
        """Display pie chart of age group distribution and bar chart for average billing"""

        #create age groups
        bins = [0, 18, 36, 56, 71, float('inf')]
        labels = ['Minor(0-17)', 'Young Adult(18-35)', 'Middle Age(36-55)', 'Senior(56-70)', 'Elderly(70+)']
        self.df['Age Group'] = pd.cut(self.df['Age'], bins = bins, labels = labels, right = False)

        #pie chart - patient distribution
        counts = self.df['Age Group'].value_counts().reindex(labels)
        plt.figure(figsize=(7, 7))
        plt.pie(counts, labels = counts.index, autopct='%1.1f%%', startangle=90)
        plt.title('Patient Distribution by Agee Group')
        plt.tight_layout()
        plt.show()

        #bar chart - average billing per age group
        avg_billing = self.df.groupby('Age Group', observed = True)['Billing Amount'].mean().reindex(labels)
        plt.figure(figsize=(8, 5))
        plt.bar(avg_billing.index, avg_billing.values)
        plt.title('Average Billing Amount by Age Group')
        plt.xlabel('Age Group')
        plt.ylabel('Average Billing Amount')
        plt.tight_layout()
        plt.show()


