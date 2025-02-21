# Chicago Public Schools Special Education Spending Analysis

## Project Purpose
This project analyzes the relationship between special education (SPED) spending and student academic growth in Chicago Public Schools (CPS) for the year 2017. Our goal is to provide data-driven insights to help CPS optimize resource allocation for special education programs, potentially improving educational outcomes for students with special needs.

## Prerequisites
- Python 3.8 or higher  
- pip (Python package installer)

## Installation and Setup
1. Clone this repository: 
'git clone https://github.com/yourusername/cps-sped-analysis.git'
'cd cps-sped-analysis'

2. Create a virtual environment (optional but recommended):  
'python -m venv venv'
'source venv/bin/activate' 

3. Install required packages:  
'pip install pandas matplotlib numpy'


## Data Sources
Ensure you have the following files in your project directory:  
- `Budget17.csv`: Contains school budget data for FY2017.  
- `SQRP17.csv`: Contains School Quality Rating Policy data for 2017.

## Usage
1. Place `Budget17.csv` and `SQRP17.csv` in the same directory as `cps_analysis.py`.  
2. Run the analysis script: 'python cps_analysis.py'
3. The script will output results to the console and generate a scatter plot visualization.

## Script Breakdown (cps_analysis.py)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Define constants
YEAR = 2017
BUDGET_FILE = f'Budget{YEAR}.csv'
SQRP_FILE = f'SQRP{YEAR}.csv'
SPED_KEYWORDS = ['Special Education', 'Diverse Learners', 'IEP']

Define helper functions
def is_sped_related(row, keywords):
return any(keyword.lower() in str(value).lower() for value in row for keyword in keywords)

def clean_school_name(name):
return str(name).lower().replace(' ', '').replace('.', '')

Load and process budget data
budget_df = pd.read_csv(BUDGET_FILE, skiprows=1, low_memory=False)
budget_df = budget_df.fillna(0)
budget_column = '0.6' # Column containing FY17 budget amount

Calculate SPED budget per school
sped_budget = budget_df[budget_df.apply(lambda row: is_sped_related(row, SPED_KEYWORDS), axis=1)]
school_sped_budget = sped_budget.groupby(sped_budget.columns)[budget_column].sum().reset_index()
school_sped_budget.columns = ['School Name', 'SPED Budget']
school_sped_budget['Clean School Name'] = school_sped_budget['School Name'].apply(clean_school_name)

Load and process SQRP data
sqrp_df = pd.read_csv(SQRP_FILE, low_memory=False)
sqrp_data = sqrp_df[['School Name', 'National School Growth Percentile - Reading', 'National School Growth Percentile - Math']]
sqrp_data['Clean School Name'] = sqrp_data['School Name'].apply(clean_school_name)

Merge budget and SQRP data
merged_data = pd.merge(school_sped_budget, sqrp_data, on='Clean School Name', how='inner')

Analyze data
spending_threshold = merged_data['SPED Budget'].quantile(0.75)
high_spending = merged_data[merged_data['SPED Budget'] >= spending_threshold]
low_spending = merged_data[merged_data['SPED Budget'] < spending_threshold]

avg_growth_high = high_spending[['National School Growth Percentile - Reading', 'National School Growth Percentile - Math']].mean()
avg_growth_low = low_spending[['National School Growth Percentile - Reading', 'National School Growth Percentile - Math']].mean()

Output results
print("Average Growth Percentiles - High Spending Schools:")
print(avg_growth_high)
print("\nAverage Growth Percentiles - Low Spending Schools:")
print(avg_growth_low)

Visualize results
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['SPED Budget'], merged_data['National School Growth Percentile - Reading'], label='Reading Growth')
plt.scatter(merged_data['SPED Budget'], merged_data['National School Growth Percentile - Math'], label='Math Growth')
plt.xlabel('Special Education Budget')
plt.ylabel('National School Growth Percentile')
plt.title('SPED Budget vs. Student Growth')
plt.legend()
plt.grid(True)
plt.show()


## Results Interpretation
The script outputs average growth percentiles for high and low spending schools. A scatter plot is generated to visualize the relationship between SPED budget and student growth percentiles.

## Challenges and Limitations
- Data integration issues due to inconsistent school naming conventions.  
- Small sample size after merging datasets (only three schools matched).  
- Limited to one year of data, preventing trend analysis.

## Future Improvements
1. Implement fuzzy matching techniques to improve school name alignment across datasets.  
2. Incorporate additional identifiers like school IDs or zip codes to enhance merging accuracy.  
3. Expand the analysis to include multiple years of data for trend identification.  
4. Include additional variables such as school size, demographics, and overall budgets to provide a more comprehensive analysis of resource allocation impacts.

## Contributing
We welcome contributions to improve this analysis! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.






