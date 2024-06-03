import random;

def coin_toss():
    if random.random() < 0.5:
        return "heads"
    else:
        return "tails"

def halfer_guess():
    return coin_toss()

def thirder_guess():
    if random.random() < 1/3:
        return "heads"
    else:
        return "tails"
    
def fourther_guess():
    if random.random() < 1/4:
        return "heads"
    else:
        return "tails"
    
def fifther_guess():
    if random.random() < 1/4:
        return "heads"
    else:
        return "tails"

def sleeping_beauty(): 
    rounds = 10000000
    num_tries = 0
    num_correct_halfer = 0
    num_correct_thirder = 0
    num_correct_fourther = 0
    num_correct_fifther = 0
    num_correct_only_tails = 0
    num_correct_only_heads = 0
    for _ in range(rounds):
        result = coin_toss()
        wake_ups = result == "heads" and 1 or 2
        for _ in range(wake_ups):
            num_tries += 1
            if result == "heads":
                num_correct_only_heads += 1
            else:
                num_correct_only_tails += 1
            
            if halfer_guess() == result:
                num_correct_halfer += 1
            if thirder_guess() == result:
                num_correct_thirder += 1
            if fourther_guess() == result:
                num_correct_fourther += 1
            if fifther_guess() == result:
                num_correct_fifther += 1
        
            
    print("Halfer pcnt correct: ", round(num_correct_halfer/num_tries, 6))
    print("Thirder pcnt correct: ", round(num_correct_thirder/num_tries, 6))
    print("Fourther pcnt correct: ", round(num_correct_fourther/num_tries, 6))
    print("Fifther pcnt correct: ", round(num_correct_fifther/num_tries, 6))
    print("Heads pcnt correct: ", round(num_correct_only_heads/num_tries, 6))
    print("Tails pcnt correct: ", round(num_correct_only_tails/num_tries, 6))
        
sleeping_beauty()