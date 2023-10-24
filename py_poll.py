import os
import csv
#create list of voter ids in total
vote_counter = set()
#create list of candidates voted on
list_of_runnerups = set()
#create list of votes for each candidate
charles_stockham_votes = []
raymon_doane_votes = []
diana_degette_votes = []


#set peth for file being read
csvpath = os.path.join("election_data.csv")
with open(csvpath, encoding='UTF-8') as csv_file:
    vote_reader = csv.reader(csv_file, delimiter =",")
    #skip headers
    next(vote_reader)

    for row in vote_reader:
        #define columns
        voter_id = row[0]

        location_voted = row[1]

        candidate = row[2]

        #count number of votes
        vote_counter.add(voter_id)
        #create list of unique candidates
        list_of_runnerups.add(candidate)
        #count number of votes for given candidate
        if candidate == "Charles Casper Stockham":
            charles_stockham_votes.append(voter_id)
        elif candidate == "Raymon Anthony Doane":
            raymon_doane_votes.append(voter_id)
        elif candidate == "Diana DeGette":
            diana_degette_votes.append(voter_id)


    #calculate percentages of votes for candidates
    percent_charles = int(len(charles_stockham_votes))/int(len(vote_counter))
    percent_raymon = int(len(raymon_doane_votes))/int(len(vote_counter))
    percent_diana = int(len(diana_degette_votes))/int(len(vote_counter))

#calculate winner
if percent_charles > percent_diana and percent_charles > percent_raymon:
    winner = "Charles Casper Stockham"
elif percent_diana > percent_raymon and percent_diana > percent_charles:
    winner = "Diana Degette"
elif percent_raymon > percent_diana and percent_raymon > percent_charles:
    winner = "Raymon Anthony Doane"
else:
    winner = "Recount/Revote"



#print number of votes
#print(len(vote_counter))


#print(list_of_runnerups)
#print number of votes for each individual candidate
#print(len(charles_stockham_votes))
#print(len(raymon_doane_votes))
#print(len(diana_degette_votes))

#print percentages as percentage format rounded to third decimal
#print(f'{percent_charles:.3%}')
#print(f'{percent_diana:.3%}')
#print(f'{percent_raymon:.3%}')

#print winner
#print(winner)



with open ('electionresults.txt','w') as file:
    #i have no idea why but i get an error if i try to hit enter and split up the lines for easy viewing after every "\n"
    #error reads:
    #SyntaxError: unterminated string literal
    #And points at the start of the f-string
    #this outputs a text file fine as is though
   
    file.writelines(f'Total Votes: {len(vote_counter)}\nCharles Casper Stockham: {percent_charles:.3%} ({len(charles_stockham_votes)})\nDiana Degette: {percent_diana:.3%} ({len(diana_degette_votes)})\nRaymon Anthony Doane: {percent_raymon:.3%} ({len(raymon_doane_votes)})\nWinner: {winner}')
   

