import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse

def generate_cpu_usage_data(file_path, start_time, end_time):
    # Generate hourly timestamps between start_time and end_time
    timestamps = pd.date_range(start_time, end_time, freq='H')[:-1]

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
    parser.add_argument('start_time', type=str, help='The start time in YYYY-MM-DD HH:MM:SS format.')
    parser.add_argument('end_time', type=str, help='The end time in YYYY-MM-DD HH:MM:SS format.')
    args = parser.parse_args()
    
    start_time = datetime.strptime(args.start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(args.end_time, '%Y-%m-%d %H:%M:%S')
    
    generate_cpu_usage_data(args.file_path, start_time, end_time)
