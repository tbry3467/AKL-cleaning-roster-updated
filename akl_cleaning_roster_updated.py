# re-coded original house cleaning project in Python from Java
# Author: tbry3467 on GitHub
# don't work too hard, fellas

# new features from prior project:
#   one week -> one month outputted
#   prevents duplicate jobs from being assigned in a one-month timeframe

class Person:

    """ Used to regulate which members have been assigned what jobs.
        each obj contains name and jobs1-4 represented as an int
        pass 0 for jobs1-4 when creating an obj, set later when assigned jobs
        '5' would represent 'trash' has been assigned
    """
    def __init__(self, name, job1, job2, job3, job4):
        self.name = name
        self.job1 = job1
        self.job2 = job2
        self.job3 = job3
        self.job4 = job4

# arrays used to track num workers per job

first_bathroom = []
second_bathroom = []
sanitize = []
kitchen = []
trash = []
attic = []
eagle_nest = []
chapter_room = []
odd_jobs = []
no_job = []
first_floor_sweep = []
first_floor_swiffer = []
second_floor_sweep = []
second_floor_swiffer = []

#structure outline & code notes:
# setter: member_name.job1 = 1
#assign users to a random list - various lists for each job
#write this output to the file
# object person, holds name & ints to jobs assigned (ex: 1,3,2,5, no duplicates)
# var establishment

members = []

inFile = "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\AKLMemberNames.txt"

# reading members and adding to list
with open(inFile) as f:
    content = f.read().splitlines() # chops off the NL char

for line in content: # transfer file lines to list
    members.append(line)

for i in members: # create person objects from each name in list
    i = Person(i,0,0,0,0)

for x in range (0,4)


# output the result
outFile = "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\houseCleaningJobs.txt"
