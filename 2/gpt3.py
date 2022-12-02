def calculate_total_score(filename):
    total_score = 0

    with open(filename, "r") as f:
        strategy_guide = f.readlines()

    for round in strategy_guide:
        opponent_choice, our_choice = round.split()
        score_for_shape = 0
        if our_choice == "X":
            score_for_shape = 1
        elif our_choice == "Y":
            score_for_shape = 2
        elif our_choice == "Z":
            score_for_shape = 3
        
        outcome_score = 0
        if opponent_choice == "A" and our_choice == "Z":
            outcome_score = 0
        elif opponent_choice == "B" and our_choice == "X":
            outcome_score = 0
        elif opponent_choice == "C" and our_choice == "Y":
            outcome_score = 0
        elif opponent_choice == "A" and our_choice == "X":
            outcome_score = 3
        elif opponent_choice == "B" and our_choice == "Y":
            outcome_score = 3
        elif opponent_choice == "C" and our_choice == "Z":
            outcome_score = 3
        else:
            outcome_score = 6

        total_score += score_for_shape + outcome_score

    return total_score

total_score = calculate_total_score("strategy_guide.txt")
print(total_score)
