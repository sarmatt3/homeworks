import sys

if sys.argv[3]=='+':
    print(int(sys.argv[1]) + int(sys.argv[2]))
elif sys.argv[3]=='-':
    print(int(sys.argv[1]) - int(sys.argv[2]))
elif sys.argv[3]=='*':
    print(int(sys.argv[1]) * int(sys.argv[2]))
elif sys.argv[3]=='/':
    print(int(sys.argv[1]) / int(sys.argv[2]))

#3
def os_check():
    if sys.platform=='win32':
        return True
    else: 
        return 'ERROR'

#4
sys.setrecursionlimit(500)
def recursion(n):
    if n==0:
        return 0
    else:
        return n + recursion(n-1)

if __name__ == '__main__':
    os_check()
    recursion(5)
    