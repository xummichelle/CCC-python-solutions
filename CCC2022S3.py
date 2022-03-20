#3/15 in CCC
(N,M,K)=list(map(int,input().split()))
##print('N={0},M={1},K={2}'.format(N,M,K))

##out=[]
##b=[]
##def prepare():
##    global out

def make_seq(N, M):
    seq = ""
    for i in range(N):
        seq += "1"
    return seq

def output(seq):
    s = ""
    for c in seq:
        s = s + c + " "
    print(s[:-1])

max_samples=(2*N-M+1)*M/2
min_samples = N
seq = make_seq(N, M)

if K > max_samples:
    print(-1)
elif K < min_samples:
    print(-1)
else:
    cur_val = min_samples
    while cur_val != K:
        if seq[N-1] != "2":
            seq = seq[1:] + "2"
            cur_val += 1
        elif seq[N-1] == "2":
            seq = seq[1:] + "1"
            cur_val += 1
    output(seq)
        


##if K>num_of_samples:
##    print(-1)
##elif K==num_of_samples:
##    for i in range(1,N+1):
##        a=i
##        if i>M:
##            a=2*M-i
##        print(a, end=' ')
##else:
##    
##    for i in range(1,N+1):
##        a=i
##        if i>M:
##            a=2*M-i
##        b.append(a)
##    print(b)
     
