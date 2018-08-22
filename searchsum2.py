# Use the file name mbox-short.txt as the file name
total = 0.00
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        print(line)
        sppos = line.find(':')
        print(sppos)
        num = line[sppos+1:sppos+8]
        print(num)
        count = count +1
        total = total + float(num)
        print(count)
        print(total)

print("Done")
print(total)
average = total/count
print("Average spam confidence:", average)
