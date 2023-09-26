# Zakres lokalny
# 1
def oneFunction (v1):
    v2 = v1 + ' Jak mija Ci dzień?'
    print (v1)
    print (v2)

oneFunction('Cześć')

# 2
def twoFunction (v1):
    print ("Python")

# 3
lengthPython = lambda word: len(word.replace(" ", ""))
print(lengthPython('Tomasz Kowalski'))

# 4
def threeFunction (v1):
    v1 = len(v1)
    print (v1)

threeFunction('Python')

# Zakres obejmujący 
# 1
def fourFunction ():
    v1 = 'Kowalski'

    def fourFunctionV1 ():
        v2 = (f"Jak się masz {v1}")
        print (v2)

    print (fourFunctionV1())

print(fourFunction())

# Zakres globalny
# 1
test = "Test - zakres globalny"

def fiveFunction():
    print(test)

print(fiveFunction())

# 2 zakres globalny - obiekt wewnątrz funkcji

testTwo = 'Obiekt globlany'

def sixFunction ():
    testTwo = 'Obiekt wewnątrz funkcji'
    print (testTwo)

print(sixFunction())

# 3
def sevenFunction ():
    global x
    x = 10
    print (x)

print(sevenFunction())