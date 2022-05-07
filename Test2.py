"""Structured english
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
"""Psudocode
open txt file
add each line of the file to a list
change the values from strings to integers
add the values to a list
print(len(list))

average the integers of the list (sum/len)

make new list ABV=[]
assigin percentage variable percent = 0 (for now)

add scores that are above average from old list to new list ( if score > avg then ABV.append)
calculate rough percent avg:
%avg = (lenABV/lenList)* 100
format average to 2 decimal places, avgPercent = round(ABV, 2)
print final formatted percent
print(avgPercent)
return

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

#examend