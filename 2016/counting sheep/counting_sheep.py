# @author Tor Berglind
# @git https://github.com/Torberglind/

def counting_sheep(n):
    found_digits = []
    for i in xrange(1, 1000):
        for j in str(i * n):
            if j not in found_digits:
                found_digits.append(j)
        if len(found_digits) == 10:
            return i*n
    return 'INSOMNIA'

t=int(raw_input())
for c in xrange(1,t+1):
    n=int(raw_input())
    print "Case #{}: {}".format(c,counting_sheep(n))
