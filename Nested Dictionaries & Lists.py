x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z =  {'x': 10, 'y': 20} 

z['x'] = 15
print(z)

students[0]['last_name'] = 'Bryant'
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z['y'] = 30
print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for key in students:
        print('first_name', '-', key['first_name'], ',', 'last_name', '-', key['last_name'])

print(iterateDictionary(students))

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict, keys):
    print(len(some_dict[keys]), keys)
    for i in some_dict[keys]:
        print(i)

print(printInfo(dojo, 'locations'))
print(printInfo(dojo, 'instructors'))