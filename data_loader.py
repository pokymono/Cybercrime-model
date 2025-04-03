import pandas as pd
import warnings
import os
import numpy as np
warnings.simplefilter('ignore')

def load_dataset(file_path):
    """Load a single dataset with error handling"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {str(e)}")
        return None

def analyze_dataset(df, year):
    """Analyze a single dataset"""
    if df is None:
        return
    
    print(f"\n{'='*50}")
    print(f"Analysis for Year {year}")
    print(f"{'='*50}")
    
    print(f"\nShape: {df.shape}")
    print("\nData Types:")
    print(df.dtypes)
    
    print("\nMissing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    
    print("\nBasic Statistics:")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(df[numeric_cols].describe())
    
    return df

def load_all_datasets():
    """Load and analyze all datasets"""
    years = ['2016', '2018', '2019', '2020', '2021']
    datasets = {}
    
    for year in years:
        file_path = f'DATASET_{year}.csv'
        if os.path.exists(file_path):
            df = load_dataset(file_path)
            datasets[year] = analyze_dataset(df, year)
        else:
            print(f"Warning: File DATASET_{year}.csv not found")
    
    return datasets

if __name__ == "__main__":
    print("Loading and analyzing all datasets...")
    datasets = load_all_datasets()
    
    # Compare datasets
    if datasets:
        print("\nComparison across years:")
        for year, df in datasets.items():
            if df is not None:
                print(f"\nYear {year}:")
                print(f"Number of rows: {df.shape[0]}")
                print(f"Number of columns: {df.shape[1]}")
                
        # Check for common columns
        all_columns = set()
        for df in datasets.values():
            if df is not None:
                all_columns.update(df.columns)
                
        print("\nTotal unique columns across all datasets:", len(all_columns))
