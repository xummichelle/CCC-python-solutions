#3/15 in CCC
(N,M,K)=list(map(int,input().split()))

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
        
     
