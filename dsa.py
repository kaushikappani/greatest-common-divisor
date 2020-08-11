def  gcd(a,b):       #function initilization
    facta=[];
    factb=[];
    for i in range(1,a+1):    #iteration number 1 and finding divisors
        if a%i==0:
            facta.append(i);
        else:
            continue;
    for j in range(1,b+1):       #iteration number 2 and finding divisors
        if b%j==0:
            factb.append(j);
        else:
            continue;
    print(facta);
    print(factb);
    common=[];
    for i in range(len(facta)):             #finding common terms
        for j in range(len(factb)):
            if facta[i]==factb[j]:
                common.append(facta[i])
    print(common);
    print(common[-1])    #pickint the max term
gcd(8,40)

#one scan model still can be improved
def gcd2(a,b):
    cf=[];
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            cf.append(i);
        else:
            continue;
    print(cf[-1]);
gcd2(8,40)

#not storing list
def gcd3(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            mrcf=i;
        else:
            continue;
    print(mrcf);
gcd3(6,14)


#scanning backward
def gcd4(a,b):
    for i in range(min(a,b),1,-1):
        if a%i==0 and b%i==0:
            mrcf=i;
            break;
        else:
            continue;
    print(mrcf)
gcd4(6,14)
