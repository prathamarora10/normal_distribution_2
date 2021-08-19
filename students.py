# Result At Last 👇👇👇

import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics as st

file_data = pd.read_csv('/Users/prathamarora/Downloads/Python_Projects/normal_distribution__bell_curve/StudentsPerformance.csv')

data = file_data['reading score'].to_list()

mean = sum(data) / len(data)
standard_deviation = st.stdev(data)
median = st.median(data)
mode = st.mode(data)

first_stdev_start, first_stdev_end = mean - standard_deviation, mean + standard_deviation
second_stdev_start, second_stdev_end = mean - ( 2 * standard_deviation ), mean + ( 2 * standard_deviation )
third_stdev_start, third_stdev_end = mean - ( 3 * standard_deviation ), mean + ( 3 * standard_deviation )

figure = ff.create_distplot([data], ['Reading Score'], show_hist = False)
figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.03], mode = 'lines', name = 'MEAN'))
figure.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.03], mode = 'lines', name = 'MEAN'))
figure.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.03], mode = 'lines', name = 'MEAN'))
figure.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.03], mode = 'lines', name = 'MEAN'))
figure.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.03], mode = 'lines', name = 'MEAN'))

figure.show()

list_of_data_within_first_stdev = [result for result in data if result > first_stdev_start and result < first_stdev_end]
list_of_data_within_second_stdev = [result for result in data if result > second_stdev_start and result < second_stdev_end]
list_of_data_within_third_stdev = [result for result in data if result > third_stdev_start and result < third_stdev_end]

print('Mean : {}'.format(mean))
print('Median : {}'.format(median))
print('Mode : {}'.format(mode))

print('Standard Deviation : {}'.format(standard_deviation))

print('{} % of data lies within 1 standard deviation'.format(len(list_of_data_within_first_stdev) * 100.0 / len(data)))
print('{} % of data lies within 2 standard deviation'.format(len(list_of_data_within_second_stdev) * 100.0 / len(data)))
print('{} % of data lies within 3 standard deviation'.format(len(list_of_data_within_third_stdev) * 100.0 / len(data)))

# Mean : 69.169
# Mode : 72
# Median : 70.0

# Standard Deviation : 14.600191937252216

# 99.6 % of data lies within 3 standard deviation
# 66.4 % of data lies within 1 standard deviation
# 95.4 % of data lies within 2 standard deviation