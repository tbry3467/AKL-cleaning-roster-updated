# re-coded original house cleaning project in Python from Java. This is a WIP
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
laundry_room = []

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
                if (len(second_bathroom) == 5): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 2 # record job int in player's properties
                    if x == 2: ppl.job2 = 2
                    if x == 3: ppl.job3 = 2
                    else: ppl.job4 = 1

                    second_bathroom.append(ppl)
                    control = 1

            if (rando == 3):
                if (len(sanitize) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 3 # record job int in player's properties
                    if x == 2: ppl.job2 = 3
                    if x == 3: ppl.job3 = 3
                    else: ppl.job4 = 1

                    sanitize.append(ppl)
                    control = 1

            if (rando == 4):
                if (len(kitchen) == 4): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 4 # record job int in player's properties
                    if x == 2: ppl.job2 = 4
                    if x == 3: ppl.job3 = 4
                    else: ppl.job4 = 1

                    kitchen.append(ppl)
                    control = 1

            if (rando == 5):
                if (len(trash) == 3): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 5 # record job int in player's properties
                    if x == 2: ppl.job2 = 5
                    if x == 3: ppl.job3 = 5
                    else: ppl.job4 = 1

                    trash.append(ppl)
                    control = 1

            if (rando == 6):
                if (len(attic) == 3): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 6 # record job int in player's properties
                    if x == 2: ppl.job2 = 6
                    if x == 3: ppl.job3 = 6
                    else: ppl.job4 = 1

                    attic.append(ppl)
                    control = 1

            if (rando == 7):
                if (len(eagle_nest) == 2): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 7 # record job int in player's properties
                    if x == 2: ppl.job2 = 7
                    if x == 3: ppl.job3 = 7
                    else: ppl.job4 = 1

                    eagle_nest.append(ppl)
                    control = 1

            if (rando == 8):
                if (len(chapter_room) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 8 # record job int in player's properties
                    if x == 2: ppl.job2 = 8
                    if x == 3: ppl.job3 = 8
                    else: ppl.job4 = 1

                    chapter_room.append(ppl)
                    control = 1

            if (rando == 9):
                if (len(odd_jobs) == 5): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 9 # record job int in player's properties
                    if x == 2: ppl.job2 = 9
                    if x == 3: ppl.job3 = 9
                    else: ppl.job4 = 1

                    odd_jobs.append(ppl)
                    control = 1

            if (rando == 10):
                if (len(first_floor_sweep) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 10 # record job int in player's properties
                    if x == 2: ppl.job2 = 10
                    if x == 3: ppl.job3 = 10
                    else: ppl.job4 = 1

                    first_floor_sweep.append(ppl)
                    control = 1

            if (rando == 11):
                if (len(first_floor_swiffer) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 11 # record job int in player's properties
                    if x == 2: ppl.job2 = 11
                    if x == 3: ppl.job3 = 11
                    else: ppl.job4 = 1

                    first_floor_swiffer.append(ppl)
                    control = 1

            if (rando == 12):
                if (len(second_floor_sweep) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 12 # record job int in player's properties
                    if x == 2: ppl.job2 = 12
                    if x == 3: ppl.job3 = 12
                    else: ppl.job4 = 1

                    second_floor_sweep.append(ppl)
                    control = 1

            if (rando == 13):
                if (len(second_floor_swiffer) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 13 # record job int in player's properties
                    if x == 2: ppl.job2 = 13
                    if x == 3: ppl.job3 = 13
                    else: ppl.job4 = 1

                    second_floor_swiffer.append(ppl)
                    control = 1

            if (rando == 14):
                if (len(laundry_room) == 1): # if job is full
                    rando_list.remove(rando)
                    continue # debugger: check this goes back to while loop

                else: # if job has open slot(s)
                    if x == 1: ppl.job1 = 14 # record job int in player's properties
                    if x == 2: ppl.job2 = 14
                    if x == 3: ppl.job3 = 14
                    else: ppl.job4 = 1

                    laundry_room.append(ppl)
                    control = 1
 


    # todo - clear phase
    print ("at this point, objects get cleared")
# todo - writing phase
print("now we write")


# output the result
out_file = "output.txt" # "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\houseCleaningJobs.txt"



# NOTES
# setter: member_name.job1 = 1