''' ITERATION 5

Macmillan Learning: Not Just A Publisher, A Learning Company

In this module, I demonstrate the integration of essential statistics into our analytics projects.
With the goal of making our code both reusable and insightful, this update includes:
1. Detailed statistics for client satisfaction scores.
2. Enhanced insights into our custom numeric list.
3. A refined docstring reflecting the purpose and scope of this module.

Process:
- Import the necessary module for statistical calculations.
- Calculate and display key statistics (min, max, mean, standard deviation) for both example and custom data.
- Ensure all relevant variables and insights are incorporated into the byline for comprehensive reporting.
'''

import statistics  # Import the statistics module for calculating mean and stdev

#####################################
# Declare global variables.
#####################################

# Example client satisfaction scores
client_satisfaction_scores: list[float] = [85.0, 90.5, 78.0, 88.2, 92.1]

# Calculate statistics for client_satisfaction_scores
min_client_score: float = min(client_satisfaction_scores)
max_client_score: float = max(client_satisfaction_scores)
mean_client_score: float = statistics.mean(client_satisfaction_scores)
stdev_client_score: float = statistics.stdev(client_satisfaction_scores)

# Custom numeric list
custom_scores: list[float] = [72.4, 85.1, 90.5, 88.0, 79.6]

# Calculate statistics for custom_scores
min_custom_score: float = min(custom_scores)
max_custom_score: float = max(custom_scores)
mean_custom_score: float = statistics.mean(custom_scores)
stdev_custom_score: float = statistics.stdev(custom_scores)

# Update the byline to include statistics for both sets of scores
byline: str = (
    f'Macmillan Learning: Not Just A Publisher, A Learning Company\n'
    f'Pet Friendly: {is_pet_friendly}\n'
    f'Number of Projects: {number_of_projects}\n'
    f'Languages Used: {", ".join(languages_used)}\n'
    f'Recent Scores: {", ".join(map(str, recent_scores))}\n'
    f'Client Satisfaction Scores:\n'
    f'  Min: {min_client_score}\n'
    f'  Max: {max_client_score}\n'
    f'  Average: {mean_client_score:.2f}\n'
    f'  Standard Deviation: {stdev_client_score:.2f}\n'
    f'Custom Scores:\n'
    f'  Min: {min_custom_score}\n'
    f'  Max: {max_custom_score}\n'
    f'  Average: {mean_custom_score:.2f}\n'
    f'  Standard Deviation: {stdev_custom_score:.2f}'
)

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
