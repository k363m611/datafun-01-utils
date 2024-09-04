'''
ITERATION 2

In this iteration, we'll define a new function that returns the byline.
We'll also update the main() function to use this new function.

Process:

1. Define a new function named get_byline() that returns the byline.
2. Update the main() function to print the value returned by get_byline().
3. Test the updated script to ensure it works correctly.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Macmillan Learning: Not Just A Publisher, A Learning Company'

#####################################
# Define a function that returns the byline.
#####################################

def get_byline() -> str:
    '''Return the byline string.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline returned by get_byline() to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
