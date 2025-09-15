file = open('my_file.txt', 'w')
file2 = open('newFile.txt', 'r')

lines_seen_so_far=set()
print("Eliminating duplicate lines..")

for line in file2:
    if line not in lines_seen_so_far:
        file.write(line)
        lines_seen_so_far.add(line)

file.close()
file2.close