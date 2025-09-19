
import sys
from functools import reduce

def process_single_case():
    """
    Reads one test case (X and the list of numbers), validates it,
    and returns the calculated sum or -1.
    """
    try:
        # Read the expected count 'X'
        x = int(sys.stdin.readline())
        
        # Read the line of numbers 'Yn'
        line = sys.stdin.readline()
        numbers = list(map(int, line.split()))

        # --- Validation Step ---
        if len(numbers) != x:
            return -1

        # --- Calculation using functional tools (no loops) ---
        # 1. Filter for non-positive numbers
        non_positives = filter(lambda y: y <= 0, numbers)
        
        # 2. Raise each to the power of 4
        powered = map(lambda y: y**4, non_positives)
        
        # 3. Sum the results. The '0' is the starting value for the sum.
        total = reduce(lambda total, num: total + num, powered, 0)
        
        return total

    except (ValueError, IOError):
        # Handle cases with bad input lines or premature end of input
        return -1

def get_all_results(n):
    """
    Recursively processes 'n' test cases and returns a list of results.
    """
    # Base Case: No more test cases to process.
    if n <= 0:
        return []

    # Process the current case to get its result
    current_result = process_single_case()
    
    # Recursive Call: Get the results for the remaining n-1 cases
    remaining_results = get_all_results(n - 1)
    
    # Combine the current result with the rest
    return [current_result] + remaining_results

def main():
    """
    Main function to start the process.
    """
    try:
        # Read the total number of test cases
        num_test_cases = int(sys.stdin.readline())
        
        # Get all results by starting the recursion
        results = get_all_results(num_test_cases)
        
        # Print all collected results at the end
        if results:
            print('\n'.join(map(str, results)))
            
    except (ValueError, IOError):
        # Handle empty input or invalid N
        return

if __name__ == "__main__":
    main()