import random
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
readingScore = df["reading score"].to_list()
mean = sum(readingScore)/len(readingScore)
std_deviation = statistics.stdev(readingScore)
median = statistics.median(readingScore)
mode = statistics.mode(readingScore)
firstStdDeviationStart,firstStdDeviationEnd = mean-std_deviation,mean+std_deviation
secondStdDeviationStart,secondStdDeviationEnd = mean-(2*std_deviation),mean+(2*std_deviation)
thirdStdDeviationStart,thirdStdDeviationEnd = mean-(3*std_deviation),mean+(3*std_deviation)
fig = ff.create_distplot([readingScore],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[firstStdDeviationStart,firstStdDeviationStart],y=[0,0.17],mode="lines",name="standarddeviation1"))
fig.add_trace(go.Scatter(x=[firstStdDeviationEnd,firstStdDeviationEnd],y=[0,0.17],mode="lines",name="standarddeviation1"))
fig.add_trace(go.Scatter(x=[secondStdDeviationStart,secondStdDeviationStart],y=[0,0.17],mode="lines",name="standarddeviation2"))
fig.add_trace(go.Scatter(x=[secondStdDeviationEnd,secondStdDeviationEnd],y=[0,0.17],mode="lines",name="standarddeviation2"))
fig.show()
listofdatawithin1stddeviation = [result for result in readingScore if result>firstStdDeviationStart and result<firstStdDeviationEnd]
listofdatawithin2ndstddeviation = [result for result in readingScore if result>secondStdDeviationStart and result<secondStdDeviationEnd]
listofdatawithin3rdstddeviation = [result for result in readingScore if result>thirdStdDeviationStart and result<thirdStdDeviationEnd]
print("mean of this data is {}".format(mean))
print("median of this data is {}".format(median))
print("mode of this data is {}".format(mode))
print("standard deviation of this data is {}".format(std_deviation))
print("{}% of data lines within 1st standard deviation".format(len(listofdatawithin1stddeviation)*100/len(readingScore)))
print("{}% of data lines within 2nd standard deviation".format(len(listofdatawithin2ndstddeviation)*100/len(readingScore)))
print("{}% of data lines within 3rd standard deviation".format(len(listofdatawithin3rdstddeviation)*100/len(readingScore)))