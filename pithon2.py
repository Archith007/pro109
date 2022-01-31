import csv 
import statistics
import pandas as pd

df = pd.read_csv("score.csv")
mathScore = df["math score"].to_list()


mean = statistics.mean(mathScore)

median = statistics.median(mathScore)

mode = statistics.mode(mathScore)

sDev = statistics.stdev(mathScore)


firstSDev,firstSDevEnd = mean-sDev, mean+sDev
secondSDev, secondSDevEnd = mean-(sDev*2), mean+(sDev*2)
thirdSDev, thirdSDevEnd = mean-(sDev*3), mean+(sDev*3)



listOfData1sD = [res for res in mathScore if res > firstSDev and res < firstSDevEnd]
listOfData2sD = [res for res in mathScore if res > secondSDev and res < secondSDevEnd]
listOfData3sD = [res for res in mathScore if res > thirdSDev and res < thirdSDevEnd]


print("{}% of height data for 1sd".format(firstSDev*100.0/len(mathScore)))
print("{}% of height data for 2sd".format(secondSDev*100.0/len(mathScore)))
print("{}% of height data for 3sd".format(thirdSDev*100.0/len(mathScore)))

print("the mode is", mode)
print("the median is", median)
print("the mean is", mean)
print("the standard deviation is", sDev)
