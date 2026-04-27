# House Price Prediction

A machine learning model that predicts California housing prices using the California Housing Dataset. Includes a Streamlit web app for interactive predictions.

## Project Overview

This project builds a regression model to predict median house values based on various housing features like location, median income, age, and proximity to ocean. The model is deployed as an interactive Streamlit application for easy price prediction.

## Features

- **Predictive Model**: Trained machine learning model for house price estimation
- **Interactive Web App**: Streamlit-based UI for real-time predictions
- **Exploratory Data Analysis**: Comprehensive EDA notebook analyzing patterns and correlations
- **Data Preprocessing**: Handles missing values and categorical encoding
- **Geographic Analysis**: Visualizes house prices by location

## Dataset

- **Source**: California Housing Dataset
- **Samples**: 20,640 houses
- **Features**: 10 (including location, income, age, etc.)
- **Target**: Median house value

### Features:
- `longitude`, `latitude` - Geographic location
- `housing_median_age` - Age of the house
- `total_rooms`, `total_bedrooms` - Property size
- `population`, `households` - Area demographics
- `median_income` - Median income of the area
- `ocean_proximity` - Proximity to ocean (categorical)

## Installation

### Requirements
- Python 3.7+
- pandas, numpy, scikit-learn, matplotlib, seaborn, streamlit

### Setup
```bash
# Clone the repository
git clone https://github.com/patelmukund7/house-price-prediction.git
cd house-price-prediction

# Install dependencies
pip install -r requirements.txt
