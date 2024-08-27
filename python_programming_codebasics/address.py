book = {}

book['Sherlock'] = {
    'name': 'Sherlock Homes',
    'address': '221 B Baker Street, London',
    'phone': '999999999'
}
book['Lestrade'] = {
    'name': 'Detective Lestrade',
    'address': 'Scotland Yard, Central London',
    'phone': '1234567890'
}
import json

s = json.dumps(book)

with open("C://Users//lenovo//mycode//py//python_programming_codebasics//book.txt", "w") as f:
    f.write(s)
f = open("C://Users//lenovo//mycode//py//python_programming_codebasics//book.txt", "r")
s = f.read()
book1 = json.loads(s)
for record in book1:
    print(book1[record])
