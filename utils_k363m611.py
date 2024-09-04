''' ITERATION 3

Macmillan Learning: Not Just A Publisher, A Learning Company

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare global variables to include new information for testing.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare global variables.
#####################################

# Update the byline with a multiline f-string to include new information.
is_pet_friendly: bool = True
number_of_projects: int = 5
languages_used: list[str] = ["Python", "R", "SQL"]
recent_scores: list[float] = [88.5, 92.3, 79.0]

byline: str = (
    f'Macmillan Learning: Not Just A Publisher, A Learning Company\n'
    f'Pet Friendly: {is_pet_friendly}\n'
    f'Number of Projects: {number_of_projects}\n'
    f'Languages Used: {", ".join(languages_used)}\n'
    f'Recent Scores: {", ".join(map(str, recent_scores))}'
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
