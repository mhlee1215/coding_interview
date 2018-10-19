# Longest Common Substring | DP-29
# Given two strings 'X' and 'Y', find the length of the longest common substring.
# Examples :

# Input : X = "GeeksforGeeks", y = "GeeksQuiz"
# Output : 5
# The longest common substring is "Geeks" and is of
# length 5.

# Input : X = "abcdxyz", y = "xyzabcd"
# Output : 4
# The longest common substring is "abcd" and is of
# length 4.

# Input : X = "zxabcdezy", y = "yzabcdezx"
# Output : 6
# The longest common substring is "abcdez" and is of
# length 6.



import numpy as np

solution_set = dict()
solution_set[("GeeksforGeeks", "GeeksQuiz")] = (5, "Geeks")
solution_set[("abcdxyz", "xyzabcd")] = (4, "abcd")
solution_set[("zxabcdezy", "yzabcdezx")] = (6, "abcdez")

def lsc(s1s2):
    s1 = s1s2[0]
    s2 = s1s2[1]
    max_len = 0
    max_str = ''

    if len(s1) > len(s2):
        long_str = s1
        short_str = s2
    else:
        long_str = s2
        short_str = s1


    # for i in range(len(long_str)):
    cnt = 0
    for i in range(-len(short_str)+1, len(long_str)):
        print(np.maximum(0, i))
        print(len(short_str)-np.abs(i))
        print("..")
        # for j in range(np.max(0, i), len(short_str)-i):
            
            

    print(len(long_str))
    print(len(short_str))
    # print(cnt)

    return (max_len, max_str)



lsc(("GeeksforGeeks", "GeeksQuiz"))
exit()



is_pass = True
for k in solution_set.keys():
    # print("%d, %d" % (solution_set[k], genUglyNum2(k)))
    if lsc(k) != solution_set[k]:
        is_pass = False


if is_pass:
    print("Pass!")
else:
    print("Fail!")