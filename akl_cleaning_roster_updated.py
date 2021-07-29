# re-coded original house cleaning project in Python from Java. This is a WIP
# Author: tbry3467 on GitHub
# don't work too hard, fellas

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

all_jobs = [first_bathroom, second_bathroom, sanitize, kitchen, trash, attic,
eagle_nest, chapter_room, odd_jobs, no_job, first_floor_sweep, 
first_floor_swiffer, second_floor_sweep, second_floor_swiffer, laundry_room]

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
        # jobs mapped to num, remove num when job is full
        job_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] 
        # num of ppl allowed in each job, in order
        job_sizes = [3,5,1,4,3,3,2,1,5,1,1,1,1,1] 

        while control == 0:
            random_job = int(random.random() * len(job_nums)) # num btwn 1 and len of job_num, adjusts when nums get removed

            # start of experimental for loop - need to test this

            for job in job_nums:
                if job == random_job:

                    # check if job is at max capacity
                    if len(all_jobs[random_job]) == job_sizes[random_job]: # if len(job) == capacity for said job:
                        job_nums.remove(job) # removes job num b/c full
                        del job_sizes[job-1] # removes corresponding size for that job
                        continue

                    else: 
                        if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs w/in 1 month
                            continue

                        if x == 1: ppl.job1 = 1 # record job int in player's properties
                        elif x == 2: ppl.job2 = 1
                        elif x == 3: ppl.job3 = 1
                        else: ppl.job4 = 1

                        (all_jobs[random_job]).append(ppl)
                        control=1
                        

            # end of experimental for loop

            # if (random_job == 1):
            #     if (len(first_bathroom) == 3): # if job is full
            #         job_nums.remove(job) # removes job num b/c full
            #         job_sizes.remove[job] # removes corresponding size for that job
            #         continue

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue

            #         if x == 1: ppl.job1 = 1 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 1
            #         elif x == 3: ppl.job3 = 1
            #         else: ppl.job4 = 1

            #         first_bathroom.append(ppl)
            #         control = 1

            # elif (random_job == 2):
            #     if (len(second_bathroom) == 5): # if job is full
            #         job_num.remove(2)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue

            #         if x == 1: ppl.job1 = 2 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 2
            #         elif x == 3: ppl.job3 = 2
            #         else: ppl.job4 = 2

            #         second_bathroom.append(ppl)
            #         control = 1

            # elif (random_job == 3):
            #     if (len(sanitize) == 1): # if job is full
            #         job_num.remove(3)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue

            #         if x == 1: ppl.job1 = 3 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 3
            #         elif x == 3: ppl.job3 = 3
            #         else: ppl.job4 = 3

            #         sanitize.append(ppl)
            #         control = 1

            # elif (random_job == 4):
            #     if (len(kitchen) == 4): # if job is full
            #         job_num.remove(4)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 4 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 4
            #         elif x == 3: ppl.job3 = 4
            #         else: ppl.job4 = 4

            #         kitchen.append(ppl)
            #         control = 1

            # elif (random_job == 5):
            #     if (len(trash) == 3): # if job is full
            #         job_num.remove(5)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 5 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 5
            #         elif x == 3: ppl.job3 = 5
            #         else: ppl.job4 = 5

            #         trash.append(ppl)
            #         control = 1

            # elif (random_job == 6):
            #     if (len(attic) == 3): # if job is full
            #         job_num.remove(6)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 6 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 6
            #         elif x == 3: ppl.job3 = 6
            #         else: ppl.job4 = 6

            #         attic.append(ppl)
            #         control = 1

            # elif (job == 7):
            #     if (len(eagle_nest) == 2): # if job is full
            #         job_num.remove(7)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 7 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 7
            #         elif x == 3: ppl.job3 = 7
            #         else: ppl.job4 = 7

            #         eagle_nest.append(ppl)
            #         control = 1

            # elif (job == 8):
            #     if (len(chapter_room) == 1): # if job is full
            #         job_num.remove(8)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 8 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 8
            #         elif x == 3: ppl.job3 = 8
            #         else: ppl.job4 = 8

            #         chapter_room.append(ppl)
            #         control = 1

            # elif (job == 9):
            #     if (len(odd_jobs) == 5): # if job is full
            #         job_num.remove(9)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 9 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 9
            #         elif x == 3: ppl.job3 = 9
            #         else: ppl.job4 = 9

            #         odd_jobs.append(ppl)
            #         control = 1

            # elif (job == 10):
            #     if (len(first_floor_sweep) == 1): # if job is full
            #         job_num.remove(10)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 10 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 10
            #         elif x == 3: ppl.job3 = 10
            #         else: ppl.job4 = 10

            #         first_floor_sweep.append(ppl)
            #         control = 1

            # elif (job == 11):
            #     if (len(first_floor_swiffer) == 1): # if job is full
            #         job_num.remove(11)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 11 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 11
            #         elif x == 3: ppl.job3 = 11
            #         else: ppl.job4 = 11

            #         first_floor_swiffer.append(ppl)
            #         control = 1

            # elif (job == 12):
            #     if (len(second_floor_sweep) == 1): # if job is full
            #         job_num.remove(12)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 12 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 12
            #         elif x == 3: ppl.job3 = 12
            #         else: ppl.job4 = 12

            #         second_floor_sweep.append(ppl)
            #         control = 1

            # elif (job == 13):
            #     if (len(second_floor_swiffer) == 1): # if job is full
            #         job_num.remove(13)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 13 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 13
            #         elif x == 3: ppl.job3 = 13
            #         else: ppl.job4 = 13

            #         second_floor_swiffer.append(ppl)
            #         control = 1

            # else:
            #     if (len(laundry_room) == 1): # if job is full
            #         job_num.remove(14)
            #         continue 

            #     else: # if job has open slot(s)
            #         if ppl.job1 == job or ppl.job2 == job or ppl.job3 == job or ppl.job4 == job: # prevents duplicate jobs per month
            #             continue
                    
            #         if x == 1: ppl.job1 = 14 # record job int in player's properties
            #         elif x == 2: ppl.job2 = 14
            #         elif x == 3: ppl.job3 = 14
            #         else: ppl.job4 = 14

            #         laundry_room.append(ppl)
            #         control = 1
 


    # todo - clear phase
    for jobs in all_jobs:
        jobs.clear
# todo - writing phase
# test to make sure script works
for ppl in member_objects:
    print(ppl.job1, ppl.job2, ppl.job3, ppl.job4)


# output the result
out_file = "output.txt" # "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\houseCleaningJobs.txt"



# NOTES BELOW
# ctrl+h find and replace
# ctrl+` terminal
