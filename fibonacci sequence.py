def main():
    n = int(input("Enter the number of terms: "))
    term1 = 0
    term2 = 1
    nextterm = 0
    for i in range(n):
        print(term1)
        nextterm = term1 + term2
        term1 = term2
        term2 = nextterm

main()