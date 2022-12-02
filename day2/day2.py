with open("example_data/day2.txt") as f:
    lines = f.readlines()
    
    score = 0

    for line in lines:
        opp, player = line.split()

        opp = "ABC".index(opp)
        player = "XYZ".index(player)

        if (opp - player == -1) or (opp - player == 2):
            score += player + 7
        elif opp - player == 0:
            score += player + 4
        else:
            score += player + 1
    
    print(f"total: {score}")

    
    score = 0
    for line in lines:
        opp, player = line.split()

        opp = "ABC".index(opp)
        
        match player:
            case "X":
                # score for chosen shape
                score += (opp - 1) % 3 + 1
            case "Y":
                # score equals opponents score + 3 (for draw)
                score += opp + 4
            case "Z":
                # score for chosen shape + 6 (for winning)
                score += (opp + 1) % 3 + 7
    
    print(f"total: {score}")
