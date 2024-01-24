

def changetonum(column):
    Letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for counter in range(10):
        if column == Letters[counter]:
            column = Numbers[counter]
            return column