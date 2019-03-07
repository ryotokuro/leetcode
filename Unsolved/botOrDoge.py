def botOrDoge(string):
    isBot = "DOGE"
    # if number of unique characters is ODD, then user is a bot

    if map % 2 != 0:  # if number of unique characters in dictionary is ODD
        isBot = "BOT"  # then the user is a bot

    # else: real person
    return isBot  # return result


# single line containing only lowercase characters
string = str(input())

# Test Case 1: BOT
print(botOrDoge("muchcoin"))

# Test Case 2: DOGE
print(botOrDoge("abcd"))

# Test Case 2: BOT
print(botOrDoge("aaaa"))

botOrDoge(string)
