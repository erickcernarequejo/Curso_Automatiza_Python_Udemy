import camelot

table = camelot.read_pdf('foo.pdf', pages=1)
print(table)
table.export('foo.pdf', f='csv', compress=True)
table[0].to_csv('foo.csv')