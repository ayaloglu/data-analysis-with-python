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

    # Calculate the sum of the profit/losses column since it is already written in positive and negative value

    # seperate csv columns into 2 lists

    months = []
    totalnet = []

    for row in budget:

        months.append(row[0])
        totalnet.append(float(row[1]))

    # Number of total months is equal to the lenght of the months list
    print(f' Total Months: {len(months)}')

    # calculate the total profit/loss
    totalfinal = sum(totalnet)
    print(f' Total: {totalfinal}')

    # max profit calculation

    max_profit = max(totalnet)
    index_max = totalnet.index(max_profit)
    max_profit_month = months[index_max]

    print(f'Greatest increase in Profits: {max_profit_month} ,(${max_profit})')

    # max loss calculation
    max_loss = min(totalnet)
    index_min = totalnet.index(max_loss)
    max_loss_month = months[index_min]

    print(f'Greatest Decrease in Profits: {max_loss_month} ,(${max_loss})')

    total = 0

    for i in range(1, len(totalnet)):

        difference = totalnet[i]-totalnet[i-1]

        total = total + difference

    average = (total)/(len(totalnet)-1)

    print(f'Average Change: $ {round(average,2)}')


textpath = os.path.join('..', 'analysis', 'results.txt')

with open(textpath, 'w', newline='') as textfile:

    textfile.writelines(f' Total Months: {len(months)} \n')
    textfile.writelines(f' Total: {totalfinal} \n')
    textfile.writelines(
        f'Greatest increase in Profits: {max_profit_month} ,(${max_profit}) \n')
    textfile.writelines(
        f'Greatest Decrease in Profits: {max_loss_month} ,(${max_loss}) \n')
    textfile.writelines(f'Average Change: $ {round(average,2)} \n')
