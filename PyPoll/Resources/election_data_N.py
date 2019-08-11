import csv
import os

votes = []
# Path 
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'election_data.csv')) as election_data_file:
    election_data = csv.DictReader(election_data_file)
    # Iteration
    for row in election_data:
        votes.append(row['Candidate'])

result = 'Election Results\n--------------------------------------\n'
# Votes total
result += 'Total Votes: %d\n' % len(votes)
result += '--------------------------------------\n'

# The list of votes
candidates = set(votes)

# Calculation of votes
candidate_results = []
for candidate in candidates:
    candidate_results.append((candidate, votes.count(candidate)))

# Sortint results
candidate_results.sort(key=lambda x: x[1], reverse=True)

for candidate_result in candidate_results:
    
    result += '%s: %.4f%% (%d)\n' % (candidate_result[0], candidate_result[1] / len(votes) * 100, candidate_result[1])

result += '--------------------------------------\n'
# The winner
result += 'Winner: %s\n' % candidate_results[0][0]
result += '--------------------------------------'

# Printing results
print(result)

# Writing to a text file
with open(os.path.join(__location__, 'result.txt'), 'w') as result_file:
    result_file.write(result)
