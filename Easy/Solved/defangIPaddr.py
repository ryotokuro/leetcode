# link: https://leetcode.com/problems/defanging-an-ip-address/

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".


def defangIPaddr(address: str) -> str:
    # Using .replace() is SUPER SLOW
    # In Python, strings are immutable objects
    # Meaning that in order for .replace() to search for '.', it will need to have multiple stack calls
    # > SLOW: address = address.replace('.', '[.]')
    # So for worst case, we have O(n*k) where k=n then it is O(n*n), where n is the length of the string
    address = list(address)

    i = 0
    while i < len(address):
        if address[i] == '.':
            address.insert(i, '[')
            address.insert(i+2, ']')
            i += 3
        else:
            i += 1
    address = ''.join(address)

    return address


print(defangIPaddr('1.1.1.1'))
