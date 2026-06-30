#string practice

name = 'john doe'
company_name = 'RUBBER DUCKS INC'
business_age = 8
address = """123 wall street
new york, ny 10001"""
comment = 'he said, "I need new solutions for my business."'

print('Josh' in name)
print('business' in comment)
print(len(address))
print(address[9:20])
print(company_name[-3:])
print(name + ' ' + 'From' + ' ' + company_name)
print(f"""The gentleman {name} is the owner of {company_name} and has been in business for {business_age} years. 
He said {comment}""")
print(address[0:20])
print(name[::3])
print(name.upper())
print(company_name.lower())
print(address.strip())
print(address.replace('york', 'jersey'))
print(name.split())
print(address.find('street'))
print(address.count('new'))
print(name.capitalize())
print(name.title())