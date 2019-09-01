# Python has function for creating, reading, updating, and deleting files.

# Open a file

myFile = open('myfile.txt', 'w')

# Get file info

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Writing in the file

myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

# Append to file

myFile = open('myfile.txt', 'a')
myFile.write(' I also love PHP.')
myFile.close()

# Read from file

myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)



