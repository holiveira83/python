# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
nums = []
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    nums.append(float(''.join(ele for ele in line if ele.isdigit() or ele == '.')))
for n in nums:
    total += n
print "Average spam confidence:",total/len(nums)