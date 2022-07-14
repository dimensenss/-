
line = '������ ��� ���, ��� ����� ������������ ��� ����� �������� � ������� ��������, ������� �����, ��� �� ������.'
if line.islower():line = line.capitalize()
print(line, end ='\n\n')
line.find('������������')
print(line.find('������������'), end = '\n\n')
#print(line.find('������������'))
print(line.replace('������������','������������'), end = '\n\n')
line = line.split(",")
print(line, end ='\n\n')
line = ','.join(line)
print(line)
