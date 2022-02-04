# Student-Grouper
- Program for grouping students based off of academic performance
- The goal of this program is to group students into new groups based off of both quiz score and team evaluation in order to incentivize group contribution and quiz performance

# Adjustable Weights
process_data.py contains weight parameters quiz_weight, group_weight, and random_weight
- increasing quiz_weight makes quiz score have more influence over overall academic score used for grouping
- increasing group_weight makes group evaluation have more influence over next grouping
- increasing random_weight makes academic score approach a normal distribution, introduced to prevent new groupings from becoming too stratified
