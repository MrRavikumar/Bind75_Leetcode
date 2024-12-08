# Print Name N Times Using Recursion
print('Print Name N Times Using Recursion')
def printName(i, n):
    if i > n:
        return
    print('Ravi')
    printName(i + 1, n)

printName(1, 5)

# Print Linearly from 1 to N Using Recursion
print('\nPrint Linearly from 1 to N Using Recursion')
def printLinearly(i, n):
    if i > n:
        return
    print(i)
    printLinearly(i + 1, n)

printLinearly(1, 5)

# Print N to 1 Using Recursion
print('\nPrint N to 1 Using Recursion')
def printReverse(i, n):
    if i < 1:
        return
    print(i)
    printReverse(i - 1, n)

printReverse(5, 5)

# Print Linearly from 1 to N Using Backtracking i.e. Should not use f(i+1, n)
print('\nPrint Linearly from 1 to N Using Backtracking')
def printLinearlyBackTrack(i, n):
    if i < 1:
        return
    printLinearlyBackTrack(i -1, n)
    print(i)

printLinearlyBackTrack(5, 5)

# Print N to 1 Using Backtracking i.e. Should not use f(i-1, n)
print('\nPrint N to 1 Using Backtracking')
def printReverseBackTrack(i, n):
    if i > n:
        return
    printReverseBackTrack(i + 1, n)
    print(i)

printReverseBackTrack(1, 5)