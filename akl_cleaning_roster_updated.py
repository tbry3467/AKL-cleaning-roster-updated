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

member_objects = []
in_file = "test_names.txt" # "akl_member_names.txt" 


# reading members and adding to list
with open(in_file) as f:
    content = f.read().splitlines() # chops off the NL char

for line in content: # pull names, create member objects and add to list
    line = Person(line,0,0,0,0)
    member_objects.append(line)

# structure outline
## check obj properties for duplicates when random rolls
## loop member_objects, assign to lists & add int to member properties
## clear job lists

# main loop
for x in range (1,5): # loops 4 times for 4 job assignments per person

    for ppl in member_objects:
        # todo - assignment phase
        control = 0
        rando_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # number mapped to job, remove num when job is full

        while control == 0:
            rando = int(random.random() * len(rando_list)) # num btwn 1 and len of rando_list, adjusts when nums get removed

            if (rando == 1):
                if (len(first_bathroom) == 3): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 1 # record job int in player's properties
                    if x == 2: ppl.job2 = 1
                    if x == 3: ppl.job3 = 1
                    else: ppl.job4 = 1

                    first_bathroom.append(ppl)
                    control = 1

            if (rando == 2):
                if (len(second_bathroom) == 3): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 1 # record job int in player's properties
                    if x == 2: ppl.job2 = 1
                    if x == 3: ppl.job3 = 1
                    else: ppl.job4 = 1

                    first_bathroom.append(ppl)
                    control = 1
 



    # todo - writing phase

    # todo - clear phase
     


# output the result
out_file = "output.txt" # "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\houseCleaningJobs.txt"



# NOTES
# setter: member_name.job1 = 1