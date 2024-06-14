"""
Life gets hard for everyone and as a programmer,
the basics when solving a problem get fuzzy. 

Don't forget FOR loops. Because they can make
a difference in your code and in your life too

P.S. I added this code block as my LinkedIn Backgroun Imaage.
Only those who discover it will understand it (muahaha)

"""
# Define a list of problems
problems = ["problem1", "problem2", "problem3", "problem4"]

# Define a dictionary with solutions for the problems
solutions = {
    "problem1": "solution1",
    "problem2": "solution2",
    "problem3": "solution3",
    "problem4": "solution4"
}

# Variable to hold the solution
solution = None

# for loop to iterate through each problem
for problem in problems:
    # Check if there is a solution for the current problem
    if solutions[problem] != False:
        solution = solutions[problem]
        print(f"For {problem}, we have found a solution: {solution}")

# And eventually print out a successful cheer because for each problem,
# The right solution was found.
print("Solutions were found to each problem!")

# This is applicable to life too :)
