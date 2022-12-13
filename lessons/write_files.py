with open("files/write.txt", "w") as write_file:
    write_file.write("Just created a file using python")

## amend file
with open("files/write.txt", "a") as write_file:
    write_file.write("\nanother file using python")

quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

## cycle through lines
with open('files/write.txt','a') as write_file:
    write_file.writelines(quotes)