#Objective
#Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

#Task
#Given a string,S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).


t=int(input())
for i in range(t):
    s=input()
    print(s[::2],s[1::2])
        