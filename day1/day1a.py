def sol(input):
    output = (input//3)-2
    return output

def main():
    input = open("inputday1.txt", "r")
    sum = 0
    for line in input:
        sum += sol(int(line)) #omvandlar, inte casta
    print(sum)

main()