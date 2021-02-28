# -------------------- Finding Inter Arrival Time ---------------------------

import random

int_arrival_t = 0
arrival_time = 0

print("Customer No.\t\t Inter Arrival Time\t\t\t Arrival Time")
for i in range(1, 21):
    if (i == 1):
        print("%i \t\t\t\t\t - \t\t\t\t\t\t\t %i" % (i, arrival_time))

    else:
        print("%i \t\t\t\t\t %i \t\t\t\t\t\t\t %i" % (i, int_arrival_t, arrival_time))

    int_arrival_t = random.randrange(1, 10)
    arrival_time = int_arrival_t + arrival_time
