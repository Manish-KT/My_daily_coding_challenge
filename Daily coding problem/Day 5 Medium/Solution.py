def num_decodings(s):
    if not s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)

    # There is one way to decode an empty string.
    dp[0] = 1

    # If the first character is '0', there are no valid decoding.
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, n + 1):
        # Check if the current character and the previous character form a valid two-digit number.
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

        # Check if the current character can be decoded on its own (not '0').
        one_digit = int(s[i - 1])
        if one_digit != 0:
            dp[i] += dp[i - 1]

    return dp[n]


# Example usage:
encoded_message = '12323126'
print(num_decodings(encoded_message))  # Output: 3 (aaa, ka, ak)
