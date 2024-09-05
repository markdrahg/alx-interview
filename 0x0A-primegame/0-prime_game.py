#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """ Generate a list of booleans where True denotes a prime number """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return is_prime

def isWinner(x, nums):
    """
    Determine the winner of each game round based on prime number selection.
    
    Args:
        x (int): Number of rounds.
        nums (list): List containing n for each round.

    Returns:
        str: The name of the player who won the most rounds (Maria or Ben), or None if a tie.
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes <= n for each n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    # Determine winner for each round
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1  # Maria wins if there's an odd number of prime removals
        else:
            ben_wins += 1  # Ben wins if there's an even number of prime removals

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
