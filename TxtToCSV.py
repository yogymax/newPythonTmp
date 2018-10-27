import csv
csvFile = open('C:\\Users\Yogesh\Desktop\\newcsv.csv','w+')
file = open('C:\\Users\Yogesh\Desktop\\txtFile.txt')
for item in file.readlines():
    for word in item.split():
        print(word ,end=',')
        csvFile.write(word+',')
    csvFile.write('\n')

