# Import csv and import os

import os
import csv

# create the path to your file

csvpath = os.path.join('election_data.csv')

# with open(csvpath) as csvfile:

#     election = csv.reader(csvfile, delimiter=',')

#     csv_header = next(csvfile)

#     # print(csv_header)
#     print("Total number of votes cast: ", len(list(election)))

with open(csvpath) as csvfile:

    # reading the csv file

    election = csv.reader(csvfile, delimiter=',')

    # removing the header

    csv_header = next(csvfile)

    # making a new list with all the candidate names

    names = [row[2] for row in election]

    # finding the unique names with the set() function

    unique_names = list(set(names))

    # because the length of the names is equal to the total votes use the length of names

    total_vote_count = len(names)

    print(f'Total Votes: {total_vote_count}')

    # finding the total counts for each unique name

    results = {}

    with open("results.txt", 'w', newline='') as textfile:

        textfile.writelines(f'Total Votes: {total_vote_count} \n')

        for name in unique_names:

            #print(name, ': ', names.count(name))
            candidate_count = names.count(name)

            percent_count = round((candidate_count/total_vote_count)*100, 3)

            final = (f"{name} : {percent_count} % ({candidate_count})")

            print(final)

            textfile.writelines(final+"\n")

        # make a dictionary of the candidate names as keys and their vote counts as values

            results[name] = candidate_count

        print(f' winner {max(results, key=results.get)}')

        textfile.writelines(f' winner {max(results, key=results.get)}')
