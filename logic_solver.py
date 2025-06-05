import itertools

def solve_einstein_riddle():
    houses = range(5)
    permutations = list(itertools.permutations(houses))
    
    for nat in permutations:
        for color in permutations:
            for drink in permutations:
                for smoke in permutations:
                    for pet in permutations:
                        if color[0] != 0: continue  # Example: the Norwegian lives in the first house
                        if nat[color.index(2)] != 1: continue  # Example: the Brit lives in the red house
                        # Add all rules as `if not ...: continue`
                        return list(zip(nat, color, drink, smoke, pet))
    return None