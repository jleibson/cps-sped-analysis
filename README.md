# Chicago Public Schools Special Education Analysis

## Project Overview

This repository contains an analysis of special education data within the Chicago Public Schools (CPS) system. Our goal is to understand patterns, trends, and potential disparities in special education services across the CPS district. This analysis aims to provide insights that could inform policy decisions, resource allocation, and improvements in special education programs.

### Why This Analysis Matters

Understanding special education trends in CPS is crucial for several reasons:
1. Ensuring equitable access to services across diverse student populations
2. Identifying potential areas of over- or under-identification of special needs
3. Optimizing resource allocation for special education programs
4. Informing teacher training and professional development initiatives

## Data Source

This analysis uses publicly available data from the Chicago Public Schools. The dataset includes anonymized student information, special education classifications, and school-level data. We obtained this data through the CPS Open Data Portal.

**Note on Data Privacy:** All data used in this analysis has been anonymized to protect student privacy. No personally identifiable information is included in our analysis or results.

## Methodology

Our analysis employs a combination of descriptive statistics, inferential statistics, and machine learning techniques to uncover patterns in the CPS special education data. Here's why we chose these methods:

1. **Descriptive Statistics:** To provide a clear overview of the current state of special education in CPS, including demographics, distribution of services, and trends over time.

2. **Inferential Statistics:** To test hypotheses about relationships between variables (e.g., socioeconomic status and special education classification rates) and to generalize findings from our sample to the broader CPS population.

3. **Machine Learning:** To identify complex patterns and predictors of special education needs that might not be apparent through traditional statistical methods.

### Key Questions We're Addressing

1. Are there disparities in special education identification rates across different demographic groups?
2. How do special education services vary across different schools and neighborhoods in Chicago?
3. What factors are most predictive of a student being classified for special education services?

## Dependencies

This project requires the following Python libraries:
- pandas (1.3.0)
- numpy (1.21.0)
- scikit-learn (0.24.2)
- matplotlib (3.4.2)
- seaborn (0.11.1)

To install these dependencies, run:
`pip install -r requirements.txt`


## Usage Instructions

1. Clone this repository:
`git clone https://github.com/jleibson/cps-sped-analysis.git`

2. Navigate to the project directory:
`cd cps-sped-analysis`

3. Run the main analysis script:
`python cps_analysis.py`

This will generate a plot that will appear on the screen, and a numerical breakdown within your terminal.

## Code Structure

Our code is organized into several modules:

- `data_cleaning.py`: Handles initial data preprocessing and cleaning.
- `exploratory_analysis.py`: Conducts initial data exploration and generates descriptive statistics.
- `statistical_tests.py`: Performs inferential statistical tests to examine relationships between variables.
- `ml_models.py`: Implements machine learning models to predict special education classifications.
- `visualization.py`: Creates data visualizations to illustrate key findings.

Each module contains detailed comments explaining not just what the code does, but why certain approaches were chosen. For example, in `ml_models.py`, you'll find explanations for why we chose specific algorithms and how they help us understand the complexities of special education classification.

## Results

After analyzing the data, the following results were observed:

1. **Sample Size**:  
   - Only 3 schools were successfully matched between the budget and SQRP datasets due to data integration challenges.

2. **High SPED Spending Schools**:  
   - **Average Reading Growth Percentile**: 80.5  
   - **Average Math Growth Percentile**: 45.0  

3. **Low SPED Spending Schools**:  
   - **Average Reading Growth Percentile**: 70.0  
   - **Average Math Growth Percentile**: 53.0  

4. **Key Observations**:  
   - High SPED spending schools showed higher average reading growth compared to low SPED spending schools.  
   - Low SPED spending schools performed slightly better in math growth compared to high SPED spending schools.  

5. **Visualization**:  
   - A scatter plot was generated to visualize the relationship between SPED budget and student growth percentiles in reading and math.

     <img width="400" alt="Scatter Plot" src="https://github.com/user-attachments/assets/826736c8-8335-4974-92da-51fb814ed0b6" />

## Limitations and Future Work

While our analysis provides valuable insights, it's important to acknowledge its limitations:
- The data is observational, so we cannot infer causality from our findings.
- There may be unmeasured variables that influence special education classifications.
- Our analysis is specific to CPS and may not generalize to other school districts.

Future work could include:
- Longitudinal studies to track changes in special education trends over time
- Qualitative research to understand the experiences of students, families, and educators
- Comparative analyses with other large urban school districts

## Contributing

We welcome contributions to this project! If you have suggestions for improvements or would like to extend the analysis, please:

1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request with a clear description of your changes

Please ensure that any code contributions adhere to our coding standards and include appropriate documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback about this analysis, please contact Joseph Leibson at joseph.leibson@gmail.com




