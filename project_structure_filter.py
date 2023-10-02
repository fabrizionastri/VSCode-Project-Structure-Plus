import os

with open('.project_structure_filter', 'r') as file:
    filterPatterns = [line.strip() for line in file.readlines()]

if filterPatterns[-1] == '':
    filterPatterns.pop()
print('filterPatterns:', filterPatterns)


def matchesFilterPatterns(filePath):
    return (any)(filter in filePath for filter in filterPatterns)


input = open('project_structure.txt', 'r', encoding='utf-8', errors='replace')
output = open('project_structure_filtered.txt', 'w', encoding='utf-8')

keepThisSection = True

for line in input:

    if line.startswith('--- File: '):
        filePath = line[len('--- File: '):].strip()
        print('filePath:', filePath)
        keepThisSection = matchesFilterPatterns(filePath)
        print('keepThisSection:', keepThisSection)

    if keepThisSection:
        output.write(line)

input.close()
output.close()
print('Done')
