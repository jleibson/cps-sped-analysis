# Chicago Public Schools Special Education Spending Analysis

## Project Purpose
This project analyzes the relationship between special education (SPED) spending and student academic growth in Chicago Public Schools (CPS) for the year 2017. Our goal is to provide data-driven insights to help CPS optimize resource allocation for special education programs, potentially improving educational outcomes for students with special needs.

## Prerequisites
- Python 3.8 or higher  
- pip (Python package installer)

## Installation and Setup
1. Clone this repository: 
'git clone https://github.com/jleibson/cps-sped-analysis.git'
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

3. The script will output results to the console and generate a scatter plot visualization.

## Script Overview (cps_analysis.py)

The `cps_analysis.py` script performs the following key functions:

1. **Import Libraries**: Imports necessary libraries such as pandas, matplotlib, and numpy.
2. **Define Constants**: Sets constants for file names and keywords related to SPED.
3. **Helper Functions**: 
- `is_sped_related()`: Checks if a row in the budget data relates to special education.
- `clean_school_name()`: Cleans school names for consistent matching.
4. **Load Data**: Loads budget and SQRP data from CSV files.
5. **Process Budget Data**: Identifies SPED-related budget items and calculates total SPED spending per school.
6. **Merge Data**: Merges budget data with SQRP data based on cleaned school names.
7. **Analyze Data**: 
- Categorizes schools into high and low SPED spending groups.
- Calculates average growth percentiles for both groups.
8. **Output Results**: Prints average growth percentiles to the console.
9. **Visualize Results**: Generates scatter plots to visualize the relationship between SPED budget and student growth percentiles.

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

