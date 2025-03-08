        # Lesson 33 - Who will pay the bill?

# Goal: Figure out how to pick a random name from 
# a list of a group of friends (or maybe coworkers)

# Given info:
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_number = random.randint(1, len(friends)) - 1  # decided to do it this way, in case there are a different number of
                                                     # people in the list 'friends'.

print(f"{friends[random_number]} has to pay the bill today.")

# after watching solution, random.choose(friends) seems like the easier solution I should have probably used instead.