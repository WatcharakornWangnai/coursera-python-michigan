#Count email name in file(mbox-short.txt)
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
n = 0

for line in handle:
    if not line.startswith("From "):
        continue
    else:    
        sentline = line.split()
        x = sentline[5]
        y = x.split(":")
        z = y[0]
        count[z] = count.get(z,0) + 1
for k,v in sorted(count.items()):
    print(k,v)