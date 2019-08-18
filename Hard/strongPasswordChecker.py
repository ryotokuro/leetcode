def strongPasswordChecker(s: str) -> int:
    least = 6
    most = 20
    lower = False
    upper = False
    sequence = 0

    changes = 0  # stores amount of changes if needed
    numCharacters = len(s)  # number of characters in the pw
    digit = any(i.isdigit() for i in s)

    for i in s:
        if lower is False:
            if i.islower():
                lower = True

        if upper is False:
            if i.isupper():
                upper = True

    index = 2
    while index < len(s):
        if s[index] == s[index-1] == s[index-2]:
            sequence += 1
        index += 1
    sequence += 2

        # index += 1
        # if repeated == 0:
        #     prevTwo = i
        #     repeated += 1
        # elif repeated == 1:
        #     prev = i
        #     repeated += 1
        # else:
        #     if prev == i:
        #         prev = i
        #         sequence += 1
        #     else:
        #         prev = i  # assign new king
        #         sequence = 0
        #         repeated = 0

    # count changes need to be made
    if numCharacters == 0:  # empty
        changes = least
    else:
        if numCharacters >= least and numCharacters <= most:  # meets criteria
            if lower is False:
                changes += 1
                sequence -= 1

            if upper is False:
                changes += 1
                sequence -= 1

            if digit is False:
                changes += 1
                sequence -= 1

            if sequence >= 3:
                changes += sequence // 3

        elif numCharacters < least:
            changes += least - numCharacters

        else:
            if numCharacters > most:
                changes += numCharacters - most

            if lower is False:
                if sequence >= 3:
                    changes += sequence // 3
                else:
                    changes += 1

            if upper is False:
                if sequence >= 3:
                    changes += sequence // 3
                else:
                    changes += 1

            if digit is False:
                if sequence >= 3:
                    changes += sequence // 3
                else:
                    changes += 1

    return changes


s = input()
print(strongPasswordChecker(s))
