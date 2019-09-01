# A loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary)
# , a set, or a string

people = ['Awanish', 'Ravi', 'Amit', 'Ram']

# Simple for loop

# for person in people:
#     print('Current person: ', person)

# Break out

# for person in people:
#     print('Current person: ', person)
#     if person == 'Amit':
#         break

# Continue

# for person in people:
#     if person == 'Amit':
#         continue
#     print('Current person: ', person)

# Range

# for i in range(len(people)):
#     print('Current person: ', people[i])

# While loops execute a set of statements as long as conidition is true

count = 0

while count <=10:
    print('Count ', count)
    count += 1
