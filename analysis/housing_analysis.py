import pandas as pd

# File paths
zhvi_file = "../data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
zori_file = "../data/Metro_zori_uc_sfrcondomfr_sm_month.csv"
mortgage_file = "../data/MORTGAGE30US.csv"

# Load datasets
zhvi = pd.read_csv(zhvi_file)
zori = pd.read_csv(zori_file)
mortgage = pd.read_csv(mortgage_file)

# Preview datasets
print("ZHVI data:")
print(zhvi.head())

print("\nZORI data:")
print(zori.head())

print("\nMortgage rate data:")
print(mortgage.head())

# Check dataset sizes
print("\nDataset shapes:")
print("ZHVI:", zhvi.shape)
print("ZORI:", zori.shape)
print("Mortgage:", mortgage.shape)

# Check missing values
print("\nMissing values:")
print("ZHVI:", zhvi.isnull().sum().sum())
print("ZORI:", zori.isnull().sum().sum())
print("Mortgage:", mortgage.isnull().sum().sum())
