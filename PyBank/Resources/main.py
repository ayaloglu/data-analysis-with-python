# Import csv and import os

import os
import csv

# create the path to your file

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# open your file with the with command


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents

    budget = csv.reader(csvfile, delimiter=',')

    # remove the header row

    csv_header = next(csvfile)

    # print(f"CSV Header: {csv_header}")

    # The number of total months equal to the length of the file without the header. Find the length of the file.

    # print(len(list(budget)))

    # Calculate the sum of the profit/losses column since it is already written in positive and negative value
    # print(list(budget))

    totalnet = [float(row[1]) for row in (budget)]
    totalfinal = sum(totalnet)
    print(totalfinal)

    totalnet_next = totalnet[1:]
    average_sum = 0
    for i, j in zip(totalnet, totalnet_next):
        average_sum += j - i
    print(round(average_sum/len(totalnet_next), 2))
    # budgetlist = list(budget)

    # dates = [k[0] for k in budgetlist]
    # budgets = [float(k[1]) for k in budgetlist]
    # total = sum(budgets)
    # minimum = min(budgets)
    # maximum = max(budgets)
    # print("total: ", total)
    # print("minimum: ", dates[budgets.index(minimum)], minimum)
    # print("maximum: ", dates[budgets.index(maximum)], maximum)
