s="azcbobobegghaklin"
count = 0
total = 0
for i in range(0,len(s)-2):
    if (s[i] == 'b'):
        if (s[i+1] == 'o' ):
            if(s[i+2] == 'b'):
                total += 1
print (total)
