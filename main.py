import os
import csv

csvpath = os.path.join('PyBank','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =  ',')

    #print(csvreader)

    csvheader = next(csvreader)

    #print(f"CSV Header: {csvheader}")
    rowcount = 0
    profits = 0
    previousprofits = 0
    change = 0
    changeperday = []
    changes = 0
    for row in csvreader:
        #print(row)
        rowcount += 1
        change = int(row[1]) - previousprofits
        previousprofits = int(row[1])
        changeperday.append(change)
        profits = profits + int(row[1])

    changeperday.sort()
    BIGGEST = changeperday[-1]
    smallest = changeperday[0]
    #print(BIGGEST)
    #print(smallest)
    changecounter = 0
    previousprofits = 0
    csvfile.seek(0)
    csvheader = next(csvreader)
    for row in csvreader:
        changecounter = int(row[1]) - previousprofits
        #print(changecounter)
        if changecounter == BIGGEST:
            dateofBIGGEST = row[0]
        if changecounter == smallest:
            dateofsmallest = row[0]
        previousprofits = int(row[1])
    print("Financial Analysis:")
    print("-------------------")
    print(f"The total number of months in this dataset is " , rowcount)
    print(f"The net profits come out to $", profits)
    print(f"The average change in profits is $", (sum(changeperday)/rowcount))
    print(f"The largest profit is $", BIGGEST, "and it occurred on", dateofBIGGEST)
    print(f'The largest loss is $', smallest, 'and it occurred on ', dateofsmallest)



output_path = os.path.join('Analysis','Financial_Analysis.txt')

with open(output_path, 'w') as fp:
    print(f"Financial Analysis:\n", file = fp )
    print(f"-------------------\n", file = fp)
    print(f"The total number of months in this dataset is {rowcount}", file = fp)
    print(f"The net profits come out to ${profits}", file = fp)
    print(f"The average change in profits is ${(sum(changeperday)/rowcount)}", file = fp)
    print(f"The largest profit is $ {BIGGEST} and it occurred on {dateofBIGGEST}", file = fp)
    print(f'The largest loss is ${smallest} and it occurred on {dateofsmallest}', file = fp)
    
    fp.close()

csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =  ',')

    #print(csvreader)

    csvheader = next(csvreader)
    #print(f"CSV Header: {csvheader}")
    totalvotes = 0
    candidates = []
    for row in csvreader:
        totalvotes += 1
        candidate = row[2]
        candidates.append(row[2])
        #print(candidate)
    print(totalvotes)
    
    different_candidates =  []
    numberofcandidates = 0
    votes = []
    for i in range(len(candidates)):
        if candidates[i] not in different_candidates:
            different_candidates.append(candidates[i])
            numberofcandidates +=1
            votes.append(0)

    print(numberofcandidates)
    print(different_candidates)

    for i in range(len(candidates)):
        for j in range(len(different_candidates)):
            if candidates[i] == different_candidates[j]:
                votes[j] += 1

    print(votes)
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:{totalvotes}")
    print('-------------------------')
    for i in range(len(different_candidates)):
        print(f"{different_candidates[i]}: {(votes[i]/totalvotes)*100}% ({votes[i]})")
    print("-------------------------")
    results = zip(different_candidates,votes)
    resultsdict = dict()
    for i,j in results:
        resultsdict.setdefault(i,[]).append(j)
    print(resultsdict)
    print(f'Winner: {max(resultsdict, key=resultsdict.get)}')

    output_path = os.path.join('Analysis','Voting_Results.txt')

    with open(output_path, 'w') as f:
        print("Election Results", file = f)
        print("-------------------------", file = f)
        print(f"Total Votes:{totalvotes}", file = f)
        print('-------------------------', file = f)
        for i in range(len(different_candidates)):
            print(f"{different_candidates[i]}: {(votes[i]/totalvotes)*100}% ({votes[i]})", file = f)
        print("-------------------------", file = f)
        results = zip(different_candidates,votes)
        resultsdict = dict()
        for i,j in results:
            resultsdict.setdefault(i,[]).append(j)
        print(resultsdict, file = f)
        print(f'Winner: {max(resultsdict, key=resultsdict.get)}', file = f)
        f.close()