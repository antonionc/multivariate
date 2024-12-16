import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse

def generate_cpu_usage_data(file_path):
    # Generate hourly timestamps for one full month
    start_date = datetime(2024, 11, 1)
    end_date = datetime(2024, 12, 1)
    timestamps = pd.date_range(start_date, end_date, freq='H')[:-1]

    # Simulate CPU usage data
    np.random.seed(0)
    cpu_usage = np.random.normal(loc=10, scale=2, size=len(timestamps))

    # Create DataFrame
    df = pd.DataFrame({'time': timestamps, 'cpu_usage': cpu_usage})

    # Save to CSV
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Kubernetes CPU usage data.')
    parser.add_argument('file_path', type=str, help='The path to the CSV file to be generated.')
    args = parser.parse_args()
    
    generate_cpu_usage_data(args.file_path)
