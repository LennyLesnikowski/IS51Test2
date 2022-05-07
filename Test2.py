

scoreList = open("Final.txt", "r")

for line in scoreList:
    scoreVar = [line.rstrip() for line in scoreList]
    scoreVar = list(map(int, scoreVar))


print ("number of grades: ", len(scoreVar))

average = (sum(scoreVar)) / (len(scoreVar))

print ("Average grade: ", average)


def calculate_percent_above_average():
    aboveAvgScore= []
    percentAboveAvg = 0
    for var in scoreVar:
        if var > average:
            aboveAvgScore.append(var)
    percentAboveAvg = ((len(aboveAvgScore)) / (len(scoreVar))) * 100
    finalPercent = round(percentAboveAvg, 2)
    print(finalPercent, "%")

calculate_percent_above_average()

