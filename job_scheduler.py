from binary import BSTDemo, Node
import time
from datetime import datetime

def get_job_input_details():
    job_start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30 -> ")
    while True:
        try:
            datetime.strptime(job_start_time, '%H:%M')
        except ValueError:
            print("Incorrect time format, should be hh:mm ")
            job_start_time = input("Enter the time in hh:mm format, example 18:30 or 6:30 -> ")
        else:
            break
    job_duration = input("Enter the duration of the job in minutes, ex: 60 -> ")
    while True:
        try:
            int(job_duration)
        except ValueError:
            print("Incorrect job duration format")
            job_duration = input("Enter the duration of the job in minutes, ex: 60 -> ")
        else:
            break
    job_name = input("Enter the name of the job (case sensitive)-> ")

    return job_start_time, job_duration, job_name

########## NEXT SECTION #############

my_tree = BSTDemo()

with open("schedule.txt") as f:
    for line in f:
        my_tree.insert(line)

######### START USER INTERFACE #####

user_interface = True

while user_interface:
    print('-'*50)
    print("Please choose from the list below: \n")
    print("Press 1 to view today's schedule jobs")
    print("Press 2 to add a job to today's schedule")
    print("Press 3 to remove a job from the schedule")
    print("Press 4 to quit")
    print('-'*50)
    while True:
        try:
            user_input = int(input("Enter your choice-> "))
            print('-'*50)
            break
        except:
            print("Input invalid please select a number between 1 and 4!!")
            time.sleep(1)

    if user_input == 1:
        my_tree.in_order()

    elif user_input == 2:
        print("You have chosen to add a job to today's schedule")
        job_to_add = get_job_input_details()
        job_to_add = ','.join(map(str, job_to_add))
        num = my_tree.length()
        my_tree.insert(job_to_add)

        if num == my_tree.length()-1:
            with open("schedule.txt", "a+") as to_write:
                to_write.write(job_to_add+"\n")
        input("Press any key to continue... ")

    elif user_input == 3:
        print("You have chosen to remove a job from the schedule")
        start_time, duration_of_job, job_name = get_job_input_details()
        key_to_find = datetime.strptime(start_time, '%H:%M').time()
        result = my_tree.find_val(key_to_find)
        if result:
            if result.name_of_job == job_name and result.duration == duration_of_job:
                print("Removing Job: ")
                print(result)
                my_tree.delete(key_to_find)
                print("Job successfully removed")
                with open("schedule.txt", "r") as f:
                    lines = f.readlines()
                with open("schedule.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != start_time+","+duration_of_job+","+job_name:
                            f.write(line)
                input("Press any key to continue... ")
            else:
                print("The name and/or duration of job did not match")
                input("Press any key to continue...")
        else:
            print("Job not found")
            input("Press any key to continue...")
    elif user_input == 4:
        user_escape = True
        while user_escape:
            while True:
                try:
                    user_escape_input = int(input("Press 1 to confirm or 2 to cancel -> "))
                    break
                except:
                    print("Input invalid please select a number between 1 and 4!! or")
                    time.sleep(2)
            if user_escape_input == 1:
                user_interface = False
                user_escape = False
                print("Exiting program...")
                print('-'*50)
                time.sleep(1)
            elif user_escape_input == 2:
                user_escape = False
            else:
                print("Please Press 1 to confirm or 2 to cancel ->")

    else:
        print("Input invalid please select a number between 1 and 4")
        time.sleep(1)
