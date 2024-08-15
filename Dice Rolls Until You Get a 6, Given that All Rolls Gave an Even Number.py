import random

numbers = [1, 2, 3, 4, 5, 6]
total_rolls = 0
successful_trials = 0
trials = 1000000  # Run a large number of trials for accuracy

for i in range(trials):
    c = 0
    while True:
        roll = random.choice(numbers)
        if roll in [1, 3, 5]:  # Stop the trial if an odd number is rolled
            break
        c += 1  # Increment count if the roll is 2, 4, or 6
        if roll == 6:
            total_rolls += c  # Add to total rolls only if we successfully roll a 6
            successful_trials += 1
            break

# Calculate the expected number of rolls for successful trials
if successful_trials > 0:
    expected_rolls = total_rolls / successful_trials
else:
    expected_rolls = float('inf')  # This would be the case if no trials succeeded

print(f"Expected number of rolls: {expected_rolls}")
