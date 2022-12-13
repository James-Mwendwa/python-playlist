## open the file
ipsum_file = open("files/ipsum.txt")

## read the file
## using for loop
for line in ipsum_file:
    ##print(line.rstrip())

    ## using readlines() method
    ##ipsum_file.seek(0)

    lines = ipsum_file.readlines()
## print(lines)

## read n number of chars

ipsum_file.seek(50)
file_text = ipsum_file.read(100)
##print(file_text)


## closing a file

ipsum_file.close()


## another way
def sequence_filter(line):
    return ">" not in line


with open("files/dna_sequence.txt") as dna_file:
    lines = dna_file.readlines()

print(list(filter(sequence_filter, lines)))
