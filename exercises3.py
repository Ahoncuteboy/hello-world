#!/usr/bin/env python
# coding: utf-8

# # Programming and Data Analysis
# 
# > Assignment 3
# 
# Kuo, Yao-Jen <yaojenkuo@ntu.edu.tw> from [DATAINPOINT](https://www.datainpoint.com)

# In[ ]:


import json


# ## Instructions
# 
# - The assignment will be disconnected if idling over 10 minutes, we can reactivate a new session by clicking the assignment link again.
# - We've imported necessary modules at the top of each assignment.
# - We've put necessary files(if any) in the working directory.
# - We've defined the names of functions/inputs/parameters for you.
# - Write down your solution between the comments `### BEGIN SOLUTION` and `### END SOLUTION`.
# - It is NECESSARY to `return` the answer, tests will fail by just printing out the answer.
# - It is known that `SyntaxError` and `IndentationError` might break our `test_runner.py` and results in a zero point grade. It is highly recommended testing your solution by calling functions/methods in notebook or running tests before submission.
# - Running tests to see if your solutions are right:
#     - File -> Save Notebook to save exercises.ipynb.
#     - File -> New -> Terminal to open a Terminal.
#     - Use command `python test_runner.py` to run test.
# - When you are ready to submit, click File -> Export Notebook As -> Executable Script.
# - Rename the exported Python script with your student ID(e.g. `b01234567.py`) and upload to the Assignment session on NTU COOL/NTNU Moodle.

# ## 01. Define a function named `square_negatives_from_args(*args)` which takes flexible integers and returns positive ones in a list.
# 
# - Expected inputs: `*args`.
# - Expected outputs: `list`.

# In[ ]:


def square_negatives_from_args(*args) -> list:
    """
    >>> square_negatives_from_args(-3, -2, -1, 0, 1, 2, 3)
    [9, 4, 1]
    >>> square_negatives_from_args(-3, -2, -1, 0, 1, 2, 3, '4', '5')
    [9, 4, 1]
    >>> square_negatives_from_args(-3, -2, -1, False, True, 2, 3, '4', '5')
    [9, 4, 1]
    """
    ### BEGIN SOLUTION
    
    ans = set(p ** 2 for p in args if type(p) == int and p != 0)
    
    return(sorted(list(ans), reverse = True))
    
    ### END SOLUTION


# ## 02. Define a function named `find_positives_from_args(*args)` which takes flexible inputs and returns positive ones.
# 
# - Expected inputs: `*args`.
# - Expected outputs: `list`.

# In[ ]:


def filter_positives_from_args(*args) -> list:
    """
    >>> filter_positives_from_args(-3, -2, -1, 0, 1, 2, 3)
    [0, 1, 2, 3]
    >>> filter_positives_from_args(-3, -2, -1, 0, 1, 2, 3, '4', '5')
    [0, 1, 2, 3]
    >>> filter_positives_from_args(-3, -2, -1, False, True, 2, 3, '4', '5')
    [False, True, 2, 3]
    """
    ### BEGIN SOLUTION
    
    ans = list(p for p in args if type(p) != str and p >= 0)
    
    return ans

    ### END SOLUTION


# ## 03. Define a function named `uppercase_keys_from_kwargs(**kwargs)` which takes flexible inputs and returns keys in uppercased.
# 
# - Expected inputs: `**kwargs`.
# - Expected outputs: `list`.

# In[ ]:


def uppercase_keys_from_kwargs(**kwargs) -> list:
    """
    >>> uppercase_keys_from_kwargs(twn='Taiwan')
    ['TWN']
    >>> uppercase_keys_from_kwargs(twn='Taiwan', jpn='Japan')
    ['TWN', 'JPN']
    >>> uppercase_keys_from_kwargs(twn='Taiwan', jpn='Japan', ltu="Lithuania")
    ['TWN', 'JPN', 'LTU']
    >>> uppercase_keys_from_kwargs(twn='Taiwan', jpn='Japan', ltu="Lithuania", svn='Slovenia')
    ['TWN', 'JPN', 'LTU', 'SVN']
    """
    ### BEGIN SOLUTION
    
    new_kwargs = {}
    for key, value in kwargs.items():
        new_kwargs[key.upper()] = value
    
    ans = tuple(new_kwargs.keys())
    
    return(list(ans))
    
    ### END SOLUTION


# ## 04. Define a function named `count_number_of_each_vowel(x)` which counts the number of occurrence for each vowel in a given string.
# 
# - Expected inputs: `str`.
# - Expected outputs: `dict`.

# In[ ]:


def count_number_of_each_vowel(x: str) -> dict:
    """
    >>> count_number_of_each_vowel("Python")
    {'o': 1}
    >>> count_number_of_each_vowel("Anaconda")
    {'a': 3, 'o': 1}
    >>> count_number_of_each_vowel("Programming and Data Analysis")
    {'o': 1, 'a': 6, 'i': 2}
    >>> count_number_of_each_vowel("National Taiwan University")
    {'a': 4, 'i': 4, 'o': 1, 'u': 1, 'e': 1}
    """
    ### BEGIN SOLUTION
    
    vowel = ['a', 'e', 'i', 'o', 'u']
    x = x.lower()
    value = []
    count = 0
    
    for i in vowel:
        for j in x:
            if i == j:
                count += 1
        value.append(count)
        count = 0
           
                    
    result = dict(zip(vowel, value))
    
    ans = {}
    for key, value in result.items():
        if value != 0:
            ans.setdefault(key, value)
    
    return ans
    
    ### END SOLUTION


# ## 05. Define a class named `Palindrome` which instantiates objects with 2 attributes `original_text` and `reversed_text`, and 1 method `is_palindrome()`.
# 
# - Expected inputs: `str`.
# - Expected outputs: `str`/`bool`.

# In[ ]:


class Palindrome:
    """
    >>> palindrome = Palindrome('eye')
    >>> palindrome.original_text
    'eye'
    >>> palindrome.reversed_text
    'eye'
    >>> palindrome.is_palindrome()
    True
    >>> palindrome = Palindrome('dye')
    >>> palindrome.original_text
    'dye'
    >>> palindrome.reversed_text
    'eyd'
    >>> palindrome.is_palindrome()
    False
    """
    ### BEGIN SOLUTION
    
    def __init__(self, x):
        self.x = x
        self.original_text = self.x
        self.reversed_text = self.x[::-1]
    
    def is_palindrome(self):
        if self.original_text == self.reversed_text:
            return True
        else:
            return False
    
    ### END SOLUTION


# ## 06. Define a class named `CommonDivisors` which instantiates objects with 2 attributes `x_divisors` and `y_divisors`, and 1 method `get_common_divisors()`.
# 
# - Expected inputs: `int`.
# - Expected outputs: `set`.

# In[ ]:


class CommonDivisors:
    """
    >>> cd = CommonDivisors(3, 6)
    >>> cd.x_divisors
    {1, 3}
    >>> cd.y_divisors
    {1, 2, 3, 6}
    >>> cd.get_common_divisors()
    {1, 3}
    >>> cd = CommonDivisors(4, 8)
    >>> cd.x_divisors
    {1, 2, 4}
    >>> cd.y_divisors
    {1, 2, 4, 8}
    >>> cd.get_common_divisors()
    {1, 2, 4}
    """
    ### BEGIN SOLUTION

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_divisors = set(p for p in range(1, self.x + 1) if self.x % p == 0)
        self.y_divisors = set(q for q in range(1, self.y + 1) if self.y % q == 0)

    def get_common_divisors(self):
        self.ans = set()
        for i in self.x_divisors:
            for j in self.y_divisors:
                if i == j:
                    self.ans.add(i)
        return self.ans
    
    ### END SOLUTION


# ## 07. Define a class named `PrimeJudgement` which instantiates objects with 2 methods `get_divisors()`, `is_prime()`.
# 
# - Expected inputs: `int`.
# - Expected outputs: `set`/`bool`.

# In[ ]:


class PrimeJudgement:
    """
    >>> pj = PrimeJudgement(1)
    >>> pj.get_divisors()
    {1}
    >>> pj.is_prime()
    False
    >>> pj = PrimeJudgement(2)
    >>> pj.get_divisors()
    {1, 2}
    >>> pj.is_prime()
    True
    >>> pj = PrimeJudgement(4)
    >>> pj.get_divisors()
    {1, 2, 4}
    >>> pj.is_prime()
    False
    """
    ### BEGIN SOLUTION
    
    def __init__(self, x):
        self.x = x

    def get_divisors(self):
        divisors = set()
        for i in range(1, self.x + 1):
            if self.x % i == 0:
                divisors.add(i)
        return divisors

    def is_prime(self):
        self.divisors = PrimeJudgement(self.x).get_divisors()
        if len(self.divisors) == 2:
            return True
        else:
            return False
    
    ### END SOLUTION


# ## 08. Define a function named `load_teams_json` that is able to load `teams.json` in our working directory and returns a `dict`.
# 
# Source: <https://docs.python.org/3/library/json.html>
# 
# - Expected inputs: `str`
# - Expected outputs：`dict`.

# In[ ]:


def load_teams_json(x):
    """
    >>> teams = load_teams_json('teams.json')
    >>> type(teams)
    dict
    >>> len(teams)
    2
    >>> teams.keys()
    dict_keys(['_internal', 'league'])
    """
    ### BEGIN SOLUTION   

    with open("teams.json", "r") as file:
         full_dict = json.load(file)
    file.close()
        
    return full_dict
    
    ### END SOLUTION


# ## 09. Define a function named `find_team_full_names` that is able to extract the full names of 30 NBA teams.
# 
# - Expected inputs: `str`
# - Expected outputs：`list`.

# In[ ]:


def find_team_full_names(x):
    """
    >>> team_full_names = find_team_full_names('teams.json')
    >>> type(team_full_names)
    list
    >>> len(team_full_names)
    30
    >>> team_full_names[:5]
    ['Atlanta Hawks',
     'Boston Celtics',
     'Brooklyn Nets',
     'Charlotte Hornets',
     'Chicago Bulls']
    >>> team_full_names[-5:]
    ['Sacramento Kings',
     'San Antonio Spurs',
     'Toronto Raptors',
     'Utah Jazz',
     'Washington Wizards']
    """
    ### BEGIN SOLUTION
    
    with open("teams.json", "r") as file:
         full_dict = json.load(file)
    file.close()
            
    name_list = []
    for i in (full_dict['league']['vegas']):
        if i['isNBAFranchise'] == True:
            name_list.append(i['fullName'])     
    
    return name_list
    
    ### END SOLUTION


# ## 10. Define a function named `find_teams_with_special_tricodes` that is able to find teams whose tricode is not the first 3 letters of their full name in upper-cased. e.g. teams like Brooklyn Nets(BKN) and San Antonio Spurs(SAS) are what we are looking for. Teams like Boston Celtics(BOS) and LA Clippers(LAC) are NOT what we are looking for.
# 
# - Expected inputs: `str`.
# - Expected outputs：`dict`.

# In[ ]:


def find_teams_with_special_tricodes(x):
    """
    >>> teams_with_special_tricodes = find_teams_with_special_tricodes('teams.json')
    >>> type(teams_with_special_tricodes)
    dict
    >>> len(teams_with_special_tricodes)
    8
    >>> teams_with_special_tricodes['BKN']
    'Brooklyn Nets'
    >>> teams_with_special_tricodes['SAS']
    'San Antonio Spurs'
    """
    ### BEGIN SOLUTION
    
    with open("teams.json", "r") as file:
        full_dict = json.load(file)
    file.close()
        
    team_dict = {}

    for i in (full_dict['league']['vegas']):
        if i['isNBAFranchise'] == True:
            team_dict.setdefault(i['tricode'], i['fullName'])
    
    ans = {}
    
    for key, value in team_dict.items():
        compare_value = ''.join(value.split())
        if key.lower() != compare_value[0:3].lower():
            ans.setdefault(key, value)
    
    return ans
    
    ### END SOLUTION

