import csv

with open('csv/exemplo.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "email", "telefone"])
    writer.writerow(["lucas", "lmirandae@gmail", "11548664"])
    writer.writerow(["lucas", "lmirandae@gmail", "11548664"])
    writer.writerow(["lucas", "lmirandae@gmail", "11548664"])
    writer.writerow(["lucas", "lmirandae@gmail", "11548664"])
    writer.writerow(["lucas", "lmirandae@gmail", "11548664"])