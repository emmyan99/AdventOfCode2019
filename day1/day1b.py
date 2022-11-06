def sol(input):
    output = 0
    while input > 2:
        print(input)
        input = (input//3)-2
        if input > 0:
            output+= input
    return output

def main():
    input = open("inputday1.txt", "r")
    sum = 0
    for line in input:
        sum += sol(int(line)) #omvandlar, inte samma som casta
    print(sum)

main()