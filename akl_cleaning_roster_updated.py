# re-coded original house cleaning project in Python from Java. This is a WIP
# Author: tbry3467 on GitHub
# don't work too hard, fellas

import random
from datetime import date
from openpyxl import load_workbook

class Person:

    """ Used to regulate which members have been assigned what jobs.
        each obj contains name and jobs1-4 represented as an int
        pass 0 for jobs1-4 when creating an obj, set later when assigned jobs
        '5' would represent 'trash' has been assigned
    """


    def __init__(self, name, job1, job2, job3, job4): # can i just pass name and set jobs to 0 in constructor?
        self.name = name # note: single underscore signifies to readers that it's a private attribute
        self.job1 = job1
        self.job2 = job2
        self.job3 = job3
        self.job4 = job4


def get_mondays():
    day = date.today 
    #d = today.strftime("%m/%d/%y") # mm/dd/y date format
    monday_dates = []
    count = 0
    
    # loop iterates the current date until 4 mondays are found
    while count != 4:
        if day.weekday() == 0: # 0 == monday, 1 == tuesday, etc
            monday_dates.append(day)
            count += count
        day = day + datetime.timedelta(days=1)

    return monday_dates


# lists used to track num of workers per job 
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
        job_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14] # jobs mapped to num, remove num when job is full
        job_sizes = [3,5,1,4,3,3,2,1,5,1,1,1,1,1] # num of ppl allowed in each job, in order

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

                        if x == 1: ppl.job1 = random_job # record job int in player's properties
                        elif x == 2: ppl.job2 = random_job
                        elif x == 3: ppl.job3 = random_job
                        else: ppl.job4 = random_job

                        (all_jobs[random_job]).append(ppl)
                        control=1

    # todo - clear phase
    for jobs in all_jobs:
        jobs.clear

# test to make sure script works
for ppl in member_objects:
    print(ppl.job1, ppl.job2, ppl.job3, ppl.job4)


# todo - writing phase
wb = load_workbook("output")
sheet = wb("master")

# clear workbook
# todo

# set headers to proper date
mondays = get_mondays()



# output the result
out_file = "output.txt" # "C:\\Users\\S537321\\Documents\\School\\Personal Projects\\houseCleaningJobs.txt"



# NOTES BELOW
# ctrl+h find and replace
# ctrl+` terminal
