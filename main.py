import pandas as pd
import matplotlib.pyplot as plt

# main.py

from cleaning import DataCleaning
from analysis import HealthcareAnalysis
from visualization import HealthcareVisual
import pandas as pd


def main():

    # Load dataset
    df = pd.read_csv('healthcare_dataset.csv')

    print(df.head())


    #Clean Data

    clean = DataCleaning(df)
    clean.remove_duplicates()
    clean.handle_missing_values()
    clean.fix_data_types()
    df = clean.get_cleaned_data()


    #Analysis

    analysis = HealthcareAnalysis(df)
    analysis.dataset_information()
    analysis.stat_summary()
    analysis.gender_distribution()
    analysis.common_conditions()
    analysis.avg_billing()
    analysis.highest_billing()


    #Visualization


    viz = HealthcareVisual(df)
    viz.gender_vis()
    viz.condition_vis()
    viz.billing_distribution_vis()
    viz.avg_billing_by_gender_vis()


if __name__ == "__main__":
    main()