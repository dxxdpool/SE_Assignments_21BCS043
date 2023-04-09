import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define API endpoint and parameters
# url = 'https://api.data.gov.in/resource/979de2b8-dba4-4c91-827f-d33824a5e824'
# params = {'api-key': '579b464db66ec23bdd0000017de3bb26b00b41cf61f619570e2f0b04', 'format': 'json', 'offset': 0,
#           'limit': 1000}

# Make API request and convert response to pandas dataframe
# response = requests.get(url, params=params)
# data = response.json()

# Assuming we receive input as given below from the above api...
data = {
  "success": True,
  "records": [
    {
      "month": "2022-01",
      "energy_consumed": "3000"
    },
    {
      "month": "2022-02",
      "energy_consumed": "3500"
    },
    {
      "month": "2022-03",
      "energy_consumed": "4000"
    },
    {
      "month": "2022-04",
      "energy_consumed": "3800"
    },
    {
      "month": "2022-05",
      "energy_consumed": "4200"
    }
  ]
}

if 'records' in data:
    df = pd.DataFrame(data['records'])
    df.rename(columns={'energy_consumed_actual': 'energy_consumed'}, inplace=True)
    df['energy_consumed'] = pd.to_numeric(df['energy_consumed'])

    # Convert date column to datetime format and set as index
    df['month'] = pd.to_datetime(df['month'], format='%Y-%m')
    df.set_index('month', inplace=True)

    # Calculate monthly energy consumption
    monthly_energy = df['energy_consumed'].resample('M').sum()

    # Calculate mean and median monthly energy consumption
    mean_monthly = monthly_energy.mean()
    median_monthly = monthly_energy.median()

    print(f"Mean monthly energy consumption: {mean_monthly} kWh")
    print(f"Median monthly energy consumption: {median_monthly} kWh")

    # Plot monthly energy consumption
    plt.plot(monthly_energy.index, monthly_energy)
    plt.xlabel('Month')
    plt.ylabel('Energy consumption (kWh)')
    plt.title('Monthly Energy Consumption')
    plt.show()

else:
    print('No records found in the response.')
