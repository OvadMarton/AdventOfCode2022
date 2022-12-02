def calculate_total_score(filename):
    total_score = 0

    with open(filename, "r") as f:
        strategy_guide = f.readlines()

    for round in strategy_guide:
        opponent_choice, outcome = round.split()
        our_choice = ""
        if outcome == "X":
            if opponent_choice == "A":
                our_choice = "C"
            elif opponent_choice == "B":
                our_choice = "A"
            elif opponent_choice == "C":
                our_choice = "B"
        elif outcome == "Y":
            if opponent_choice == "A":
                our_choice = "A"
            elif opponent_choice == "B":
                our_choice = "B"
            elif opponent_choice == "C":
                our_choice = "C"
        elif outcome == "Z":
            if opponent_choice == "A":
                our_choice = "B"
            elif opponent_choice == "B":
                our_choice = "C"
            elif opponent_choice == "C":
                our_choice = "A"
        
        score_for_shape = 0
        if our_choice == "A":
            score_for_shape = 1
        elif our_choice == "B":
            score_for_shape = 2
        elif our_choice == "C":
            score_for_shape = 3
        
        outcome_score = 0
        if outcome == "X":
            outcome_score = 0
        elif outcome == "Y":
            outcome_score = 3
        elif outcome == "Z":
            outcome_score = 6

        total_score += score_for_shape + outcome_score

    return total_score

total_score = calculate_total_score("strategy_guide.txt")
print(total_score)