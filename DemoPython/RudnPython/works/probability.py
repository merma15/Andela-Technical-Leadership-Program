import math

# Total combinations of drawing 4 balls from the hat
total_combinations = math.comb(11, 4)

# Number of ways to draw 1 red and 2 green balls
ways_to_draw_red_green = math.comb(4, 1) * math.comb(2, 2) + math.comb(5, 1)

# Probability calculation
probability = ways_to_draw_red_green / total_combinations

print(f"The calculated probability is: {probability:.4f}")
