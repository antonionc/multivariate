import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_time_series_from_csv(file_path):
    data = pd.read_csv(file_path)
    t = data['time'].values
    metrics = data['metric'].values
    return t, metrics

def fourier_transform(time_series):
    freq_representation = np.fft.fft(time_series)
    freq = np.fft.fftfreq(len(time_series))
    return freq, np.abs(freq_representation)

def plot_time_series_and_frequency(t, time_series, freq, freq_representation):
    fig, (ax1, ax2) = plt.subplots(2, 1)
    
    ax1.plot(t, time_series)
    ax1.set_title('Time Series')
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Metric')
    
    ax2.plot(freq, freq_representation)
    ax2.set_title('Frequency Representation')
    ax2.set_xlabel('Frequency [Hz]')
    ax2.set_ylabel('Magnitude')
    
    plt.tight_layout()
    plt.show()

# Example usage
file_path = 'k8s_metrics.csv'  # Path to the CSV file

t, time_series = read_time_series_from_csv(file_path)
freq, freq_representation = fourier_transform(time_series)
plot_time_series_and_frequency(t, time_series, freq, freq_representation)
