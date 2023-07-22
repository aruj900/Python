import camelot
tables = camelot.read_pdf('docs/Keytruda PI.pdf',pages="8")
print(tables[0].df)