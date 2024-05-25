import sys, select

if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
    print(input())

else:
    print("fichero.txt")
