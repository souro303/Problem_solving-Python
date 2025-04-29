def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        cf = (n + k - 1) // k
        k *= cf
        print((k + n - 1) // n)
 
if __name__ == "__main__":
    main()