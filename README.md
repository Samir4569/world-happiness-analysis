# World Happiness Report Analysis

## Project Overview

This repository contains a comprehensive data analysis of the World Happiness Report (WHR) dataset, covering the years 2014–2024. The dataset ranks countries based on happiness metrics derived from the Gallup World Poll. This project explores the relationships between life satisfaction and factors such as GDP per capita, social support, freedom, generosity, and perceptions of corruption. Interactive visualizations and trend analyses highlight how these factors influence happiness across time.

## Objectives

- Examine how economic factors (e.g., GDP per capita) and social factors (e.g., social support, freedom) correlate with life evaluation scores.
- Analyze happiness trends from 2014–2024 to identify shifts in rankings and key drivers.
- Visualize multidimensional relationships using interactive bubble plots, stacked bar charts, and other visualizations.
- Document the data scraping and cleaning process, emphasizing its impact on data quality and analysis.

## Why This Project?

Happiness metrics provide valuable insights into global well-being and the interplay of economic and social factors. This project demonstrates skills in:

- Web scraping and data collection
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Interactive and static visualizations

It is suitable for data science portfolios, academic research, or policy-related analyses.

## Data Source and Scraping Details

- Source: Data scraped from worldhappiness.report (tables or CSV downloads from annual reports).
- Scraping Process:
    - Python libraries used: requests, BeautifulSoup, and/or selenium
    - Combined data from multiple years (2014–2024) into a single CSV file
    - Challenges: inconsistent table formats, missing data for some countries, handling non-standard characters (e.g., '−' for negative values)
 
## Data Quality

- Size: ~1100 rows (~100–150 countries per year)
- Missing Values: Represented as '-' (e.g., Healthy Life Expectancy for Lesotho, 2014)
- Limitations:
    - Rankings are relative (1 = highest), not absolute values
    - Self-reported data may include cultural biases
    - Some countries are missing in certain years
## Technologies Used

- Python: pandas, numpy, matplotlib, seaborn, plotly
- Web scraping: requests, BeautifulSoup, selenium
- Data visualization: Static and interactive plots

## Exploratory Data Analysis (EDA)

Key steps performed:

- **Inspect dataset:** Check structure, types, and summary statistics  
- **Missing values:** Identify gaps in data  
- **Trends over time:** Average Life Evaluation per year; top & bottom countries per year  
- **Correlations:** Relationships between Life Evaluation and economic/social factors  
- **Visualizations:**  
    - Scatter plots with regression lines (e.g., GDP vs Life Evaluation)  
    - Time series for country-level happiness trends  
    - Compare rank vs score to verify consistency

## Key Visualizations

- **Line chart:** Average happiness over years  
- **Boxplots:** Compare happiness across regions or years  
- **Multi-line chart:** Top 5 countries’ happiness trends over 2014–2024  
- **Heatmap:** Correlations between Life Evaluation and other numeric factors  
- **Stacked bar charts:** Contributions of Social Support, Freedom, and Generosity to happiness  
- **Bubble plots:** GDP vs Life Evaluation (bubble size = Social Support or population)  
- **Optional Interactive plots:** Using Plotly with hover info for countries
