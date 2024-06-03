import random
import numpy as np 

def coin_toss(p_heads = 0.5):
    if random.random() < p_heads:
        return "heads"
    else:
        return "tails"

p_heads = np.linspace(0, 100)
corrects = np.zeros(100)


def sleeping_beauty(p_range, rounds): 
    num_tries = 0
    for _ in range(rounds):
        result = coin_toss()
        wake_ups = result == "heads" and 1 or 2
        for _ in range(wake_ups):
            num_tries += 1
            for i, p in enumerate(p_heads):
                if (coin_toss(p) == result):
                    corrects[i] += 1

