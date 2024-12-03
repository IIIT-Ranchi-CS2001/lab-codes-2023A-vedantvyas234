import pandas as pd;
ds=pd.read_csv("AQI_Data.csv");
print("The first 5 rows are :- ")
print(ds.head(5));#display the first 5 rows
print("The last 6 columns are :- ")
print(ds.tail(6));#display the lat 6 rows
print("Statiscal Summary of all the numerical columns are :- ")
print(ds.describe());#outputs the statiscal paramaters of the column data
import numpy as np

# Extracting unique cities
cities = ds['City'].unique()

# Calculating mean values for AQI, PM2.5, and PM10 using NumPy
mean_values_numpy = {
    city: {
        "AQI": np.mean(ds.loc[ds['City'] == city, 'AQI']),
        "PM2.5": np.mean(ds.loc[ds['City'] == city, 'PM2.5']),
        "PM10": np.mean(ds.loc[ds['City'] == city, 'PM10'])
    }
    for city in cities
}

# Printing the results
for city, values in mean_values_numpy.items():
    print(f"{city}: AQI = {values['AQI']:.2f}, PM2.5 = {values['PM2.5']:.2f}, PM10 = {values['PM10']:.2f}")

# Load the dataset
file_path = "AQI_Data.csv"
ds = pd.read_csv(file_path)

# Calculate the average AQI and maximum PM10 level for each city
grouped_data = ds.groupby('City')[['AQI', 'PM10']].agg({
    'AQI': 'mean',
    'PM10': 'max'
})

# Rename the columns for clarity
grouped_data.columns = ['Average_AQI', 'Maximum_PM10']

# Save the results to a new CSV file
grouped_data.to_csv("Citywise_AQI.csv")

print("Data grouped by city and saved to 'Citywise_AQI.csv'")
