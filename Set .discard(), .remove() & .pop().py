# ============================================
# PROGRAM : Set .discard(), .remove() & .pop()
# ============================================

n = int(input())
s = set(map(int, input().split()))
N = int(input()) # No of cases

for _ in range(N):
    userInputs = input().strip().split() # Input

    if len(userInputs)==1:
        cmd, val = userInputs[0], '' # for non-argumented commands
    else:
        cmd, val = userInputs # for single-argumented commands
        
    eval(f's.{cmd}({val})') # evaluate the command
    
print(sum(s)) # Output