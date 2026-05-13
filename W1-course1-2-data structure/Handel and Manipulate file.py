# Handle and manipulate file
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From "):
        continue
    else:    
        line = line.rstrip()
        count = count + 1
        x = line.split()
        y = x[1]
        print(y)

print("There were", count, "lines in the file with From as the first word")