# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
import random


def toss(reps):
    # print new_toss
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    result_string_complete = ""

    for x in range(reps):
        new_toss = random.randint(0, 1)
        if new_toss == 1:
            head_count += 1
            result = "head"
            print("Attempt #", attempt_count, ": Throwing a coin... It's a ", result,
                  "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far")
        else:
            tail_count += 1
            result = "tail"
            print("Attempt #", attempt_count, ": Throwing a coin... It's a ", result,
                  "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far")
        attempt_count += 1


toss(5000)
print("Ending the program, thank you!")
