#Check the no. is Prime or NOT
K=int(input())
for i in range(2,K):
    if K%i==0:
        print("No Prime")
        break
    else:
        print("Prime no.")
