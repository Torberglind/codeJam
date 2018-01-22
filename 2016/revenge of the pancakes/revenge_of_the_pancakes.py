# @author Tor Berglind
# @git https://github.com/Torberglind/

def revenge_of_the_pancakes(s):
    n = 0
    s_reversed = ''.join(reversed(s))
    s = list(s)
    for i in range(0, len(s)-1):
        if s_reversed[i] != s_reversed[i+1]:
            for j in range(len(s)-i):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
            n = n+1
    if s[0] == '-':
        n = n+1
    return n

t=int(raw_input())
for c in xrange(1,t+1):
    s=str(raw_input())
    print "Case #{}: {}".format(c,revenge_of_the_pancakes(s))






