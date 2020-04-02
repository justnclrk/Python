#Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
#Score: 60 - 69; Grade - D
#Score: 70 - 79; Grade - C
#Score: 80 - 89; Grade - B
#Score: 90 - 100; Grade - A
import random
random_num = random.randint(60, 100)
def score_grade():
    if random_num in range(60,69):
        print "Score: {}; Your grade is D".format(random_num)
    if random_num in range(70,79):
        print "Score: {}; Your grade is C".format(random_num)
    if random_num in range(80,89):
        print "Score: {}; Your grade is B".format(random_num)
    if random_num in range(90,100):
        print "Score: {}; Your grade is A".format(random_num)
score_grade()
