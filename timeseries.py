import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt


class TimeSeries:

    def __init__(self):
        self.batch_size = 500
        self.n_steps = 1

    def generate_time_series(self):
        freq1, freq2, offset1, offset2 = np.random.rand(4, self.batch_size, 1)
        time = np.linspace(0, 1,self.n_steps)
        series = 0.5 * np.sin((time - offset1)) * (freq1 * 10 + 10)  # Welle 1
        series += 0.2 * np.sin((time - offset2)) * (freq2 * 20 + 20)  # Welle 2
        series += 0.1 * (np.random.rand(self.batch_size, self.n_steps) - 0.5)  # Rauschen
        return series[..., np.newaxis].astype(np.float32)

    def plot_series(self,series,xrange=10):
        x = np.linspace(-xrange, xrange, self.batch_size)
        fig = plt.figure()
        plt.plot(x, series[:, 0, 0], '-')

        plt.show()


timeseries = TimeSeries()

series = timeseries.generate_time_series()
timeseries.plot_series(series)



