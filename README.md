# Chicago Public Schools Special Education Spending Analysis

## Project Overview
This project analyzes the relationship between special education (SPED) spending and student growth percentiles in Chicago Public Schools (CPS) for the year 2017. Our goal is to uncover potential correlations between SPED budget allocation and academic performance, providing insights for resource allocation strategies.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Sources](#data-sources)
3. [Methodology](#methodology)
4. [Technical Implementation](#technical-implementation)
5. [Results](#results)
6. [Interpretation](#interpretation)
7. [Challenges Encountered](#challenges-encountered)
8. [Future Improvements](#future-improvements)
9. [Potential Applications](#potential-applications)

## Introduction
Efficient allocation of resources in special education is crucial for student success. This project seeks to understand how SPED spending impacts student growth in reading and math across CPS schools.

## Data Sources
- Budget data: `Budget17.csv`
  - Contains: School names, budget categories, and allocated amounts
  - Key column: '0.6' (represents the FY17 budget amount)
- School Quality Rating Policy (SQRP) data: `SQRP17.csv`
  - Contains: School performance metrics
  - Key columns: 'National School Growth Percentile - Reading', 'National School Growth Percentile - Math'

## Methodology
1. Identify SPED-related budget items using keywords
2. Calculate total SPED spending per school
3. Extract student growth percentiles from SQRP data
4. Merge budget and performance data based on school names
5. Categorize schools into high and low SPED spending groups
6. Compare student growth percentiles between these groups

## Technical Implementation
- Language: Python 3.8
- Key Libraries: 
  - pandas 1.2.4 for data manipulation
  - matplotlib 3.4.2 for visualization
  - numpy 1.20.2 for numerical operations

Key steps in the implementation:
1. Data loading: `pd.read_csv()` for both budget and SQRP files
2. SPED budget identification: Used lambda function with keyword matching
3. Data cleaning: Standardized school names, handled missing values
4. Data merging: `pd.merge()` on cleaned school names
5. Analysis: Calculated average growth percentiles for high and low spending schools
6. Visualization: Scatter plots of SPED budget vs. growth percentiles

## Results
- Sample size: 3 schools (after data merging)
- High-spending schools:
  - Reading growth: 80.5 percentile
  - Math growth: 45.0 percentile
- Low-spending schools:
  - Reading growth: 70.0 percentile
  - Math growth: 53.0 percentile

## Interpretation
The limited sample suggests a potential positive correlation between SPED spending and reading growth. However, the relationship with math growth is less clear. The small sample size significantly limits the reliability of these conclusions.

## Challenges Encountered
1. Data integration: Difficulty matching school names between datasets
2. Data quality: Inconsistent naming conventions and missing data
3. Sample size: Resulting in only 3 schools for final analysis

## Future Improvements
1. Enhance data matching:
   - Implement fuzzy matching algorithms (e.g., Levenshtein distance)
   - Use additional identifiers (school ID, zip code)
2. Expand data sources:
   - Include multiple years for trend analysis
   - Incorporate demographic data and other relevant factors
3. Refine analysis techniques:
   - Apply more advanced statistical methods (e.g., regression analysis)
   - Utilize machine learning for predictive modeling

## Potential Applications
1. Resource Allocation: Inform SPED budget decisions based on performance correlations
2. Performance Benchmarking: Identify high-performing schools for best practice studies
3. Predictive Modeling: Develop models to forecast the impact of budget changes on student growth
4. Policy Development: Provide data-driven insights for SPED policy formulation

By refining this approach, CPS can make more informed decisions in resource allocation, potentially improving outcomes for students with special needs.
