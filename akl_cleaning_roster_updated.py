# re-coded original house cleaning project in Python from Java
# Author: tbry3467 on GitHub
# don't work too hard, fellas

# new features from prior project:
#   one week -> one month outputted
#   prevents duplicate jobs from being assigned in a one-month timeframe

import random


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

members = []
member_objects = []
inFile = "test_names.txt" # "akl_member_names.txt" 


# reading members and adding to list
with open(inFile) as f:
    content = f.read().splitlines() # chops off the NL char

for line in content: # transfer file lines to list
    members.append(line)

for i in members: # create person objects from each name in list
    i = Person(i,0,0,0,0)
    member_objects.append(i)


# main loop
for x in range (0,4):
    for ppl in members:

    # todo - assignment phase
        control = 0
        rando_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # remove num from list once respective chore is full

        while control == 0:
            rando = int(random.random() * len(rando_list)) # picks random num in rando_list i think?

            if (rando == 1):
                if (len(first_bathroom) == 3):
                    rando_list.remove(rando)
                    continue

                else: 
                    first_bathroom.append(ppl)
                    control = 1



    # todo - writing phase

    # todo - clear phase
     


# output the result
outFile = "output.txt" # "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\houseCleaningJobs.txt"



# NOTES
# setter: member_name.job1 = 1