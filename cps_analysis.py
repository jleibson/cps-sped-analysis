import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the years and file names
years = [2017]
budget_files = {2017: 'Budget17.csv'}
sqrp_files = {2017: 'SQRP17.csv'}

# Define keywords to identify special education programs
sped_keywords = ['Special Education', 'Diverse Learners', 'IEP']

# Function to check if a row is SPED related based on keywords
def is_sped_related(row, sped_keywords):
    return any(keyword.lower() in str(value).lower() for value in row for keyword in sped_keywords)

# Function to clean school names
def clean_school_name(name):
    try:
        return str(name).lower().replace(' ', '').replace('.', '')
    except AttributeError:
        print(f"Warning: Unable to clean school name '{name}'. Skipping.")
        return None

# Main Code
for year in years:
    print(f"\n--- Analyzing data for {year} ---")

    try:
        # Load budget data
        budget_df = pd.read_csv(budget_files[year], skiprows=1, low_memory=False)
        budget_df = budget_df.fillna(0)

        # Set budget column
        budget_column = '0.6'
        print(f"Using column '{budget_column}' for budget data")

        # Load SQRP data
        sqrp_df = pd.read_csv(sqrp_files[year], low_memory=False)
        sqrp_df = sqrp_df.fillna(0)

        # 1. Calculate Special Education Spending per School
        sped_budget = budget_df[budget_df.apply(lambda row: is_sped_related(row, sped_keywords), axis=1)].copy()

        # Group by school name and sum the budget
        school_sped_budget = sped_budget.groupby(sped_budget.columns[0])[budget_column].sum().reset_index()
        school_sped_budget.columns = ['School Name', 'SPED Budget']

        # Clean school names in budget data
        school_sped_budget['Clean School Name'] = school_sped_budget['School Name'].apply(clean_school_name)
        school_sped_budget = school_sped_budget.dropna(subset=['Clean School Name'])

        # 2. Get Student Growth Data
        sqrp_data = sqrp_df[['School Name', 'National School Growth Percentile - Reading', 'National School Growth Percentile - Math']].copy()

        # Clean school names in SQRP data
        sqrp_data['Clean School Name'] = sqrp_data['School Name'].apply(clean_school_name)
        sqrp_data = sqrp_data.dropna(subset=['Clean School Name'])

        # Convert growth percentiles to numeric, replacing 'Score' with NaN
        for col in ['National School Growth Percentile - Reading', 'National School Growth Percentile - Math']:
            sqrp_data[col] = sqrp_data[col].replace('Score', np.nan)
            sqrp_data[col] = pd.to_numeric(sqrp_data[col], errors='coerce')
            sqrp_data[col] = sqrp_data[col].replace(0, np.nan)  # Replace 0 with NaN

        # Remove rows with NaN values
        sqrp_data = sqrp_data.dropna()

        print("\nSQRP data shape after cleaning:", sqrp_data.shape)
        print("\nSample of SQRP school names:")
        print(sqrp_data['School Name'].head())
        print("\nSample of Budget school names:")
        print(school_sped_budget['School Name'].head())

        # 3. Merge Budget and Growth Data
        merged_data = pd.merge(school_sped_budget, sqrp_data, on='Clean School Name', how='inner')

        print("\nMerged data shape:", merged_data.shape)
        print("\nMerged data info:")
        print(merged_data.info())

        if merged_data.empty:
            print("\nNo matching schools found between budget and SQRP data.")
            continue

        # 4. Identify Schools with Significant SPED Spending
        spending_threshold = merged_data['SPED Budget'].quantile(0.75)
        high_spending_schools = merged_data[merged_data['SPED Budget'] >= spending_threshold]
        low_spending_schools = merged_data[merged_data['SPED Budget'] < spending_threshold]

        # 5. Compare Growth Percentiles
        avg_growth_high = high_spending_schools[['National School Growth Percentile - Reading', 'National School Growth Percentile - Math']].mean()
        avg_growth_low = low_spending_schools[['National School Growth Percentile - Reading', 'National School Growth Percentile - Math']].mean()

        # 6. Output Results
        print("\nAverage Growth Percentiles - High Spending Schools:")
        print(avg_growth_high)
        print("\nAverage Growth Percentiles - Low Spending Schools:")
        print(avg_growth_low)

        # 7. Plot Results
        plt.figure(figsize=(10, 6))
        plt.scatter(merged_data['SPED Budget'], merged_data['National School Growth Percentile - Reading'], label='Reading Growth')
        plt.scatter(merged_data['SPED Budget'], merged_data['National School Growth Percentile - Math'], label='Math Growth')
        plt.xlabel('Special Education Budget')
        plt.ylabel('National School Growth Percentile')
        plt.title('SPED Budget vs. Student Growth')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
         print(f"Error processing data for {year}: {e}")

