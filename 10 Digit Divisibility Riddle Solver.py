# 10 Digit Divisibility Riddle Solver
"""
This script finds all 10-digit numbers using each digit from 0 to 9 exactly once,
where the number formed by the first i digits is divisible by i for i from 1 to 10.
"""

def is_valid_number(digits):
    """
    Check if a sequence of digits satisfies the divisibility conditions:
    - Position 1: a divisible by 1 (always true)
    - Position 2: ab divisible by 2
    - Position 3: abc divisible by 3
    - ...
    - Position 10: abcdefghij divisible by 10
    """
    for i in range(1, len(digits) + 1):
        # Get the number formed by first i digits
        num = int(''.join(map(str, digits[:i])))
        if num % i != 0:
            return False
    return True

def solve_divisibility_riddle():
    """
    Find all 10-digit numbers where each digit 0-9 appears exactly once
    and satisfies the divisibility conditions.
    """
    from itertools import permutations
    
    solutions = []
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    print("Searching for solutions...")
    print("This may take a while as we're checking all permutations...")
    
    count = 0
    for perm in permutations(digits):
        count += 1
        if count % 100000 == 0:
            print(f"Checked {count:,} permutations so far...")
        
        # Skip if first digit is 0 (would make it a 9-digit number)
        if perm[0] == 0:
            continue
            
        if is_valid_number(perm):
            solution = ''.join(map(str, perm))
            solutions.append(solution)
            print(f"Found solution: {solution}")
            
            # Verify the solution by showing each step
            print("Verification:")
            for i in range(1, 11):
                prefix = solution[:i]
                divisor = i
                remainder = int(prefix) % divisor
                print(f"  {prefix} ÷ {divisor} = {int(prefix) // divisor} remainder {remainder}")
            print()
    
    print(f"\nTotal permutations checked: {count:,}")
    print(f"Solutions found: {len(solutions)}")
    return solutions

def optimized_solve():
    """
    More efficient approach using backtracking with early pruning.
    """
    def backtrack(current_digits, used_digits):
        # If we have all 10 digits, we found a solution
        if len(current_digits) == 10:
            return [''.join(map(str, current_digits))]
        
        solutions = []
        position = len(current_digits) + 1
        
        # Try each unused digit
        for digit in range(10):
            if digit in used_digits:
                continue
                
            # Skip leading zero
            if len(current_digits) == 0 and digit == 0:
                continue
            
            # Try adding this digit
            test_digits = current_digits + [digit]
            test_number = int(''.join(map(str, test_digits)))
            
            # Check if current prefix satisfies divisibility condition
            if test_number % position == 0:
                # Recursively try to complete the solution
                new_used = used_digits | {digit}
                sub_solutions = backtrack(test_digits, new_used)
                solutions.extend(sub_solutions)
        
        return solutions
    
    print("Using optimized backtracking approach...")
    solutions = backtrack([], set())
    
    for solution in solutions:
        print(f"Found solution: {solution}")
        print("Verification:")
        for i in range(1, 11):
            prefix = solution[:i]
            divisor = i
            remainder = int(prefix) % divisor
            print(f"  {prefix} ÷ {divisor} = {int(prefix) // divisor} remainder {remainder}")
        print()
    
    return solutions

if __name__ == "__main__":
    print("=" * 50)
    print("DIVISIBILITY RIDDLE SOLVER")
    print("=" * 50)
    print("Finding 10-digit numbers (using digits 0-9 exactly once)")
    print("where position i is divisible by i")
    print()
    
    # Use the optimized version for better performance
    solutions = optimized_solve()
    
    if solutions:
        print(f"Found {len(solutions)} solution(s)!")
        for i, sol in enumerate(solutions, 1):
            print(f"Solution {i}: {sol}")
    else:
        print("No solutions found.")
    
    print("\nDone!")