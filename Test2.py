"""
start
First open the text file in read mode.
The for every line in a new list remove all the characters from the right in the list and then.
create a new variable for this list of integesters by mapping each one as an integer to the list.
The number of grades is simply the length of this new integer based list.
the average of these grades is simply the sum of the list divided by the length of the list.
print the number of grades & the average grade to the consol.

Create a new definition
    Create a blank list
    Assign a value to the score to be calculated 
    For every variable in the list of grades, if the variable is greater than average.
    Add that variable to a new list. of above avg grades
    Calculate the percentage of grades that are above average by dividing the length of the above average scores list by the length of the regular scores.
    Round the final percent to two decimal places, as is standard.
    Print that final percent to the consol
Call that definition
end



"""



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

