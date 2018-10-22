#Que1
print("1. read n lines of a file")
class FileHandling:
    def readFile(self):
        file = open("testfile1.txt",'r')
        for each in file:
            print(each)
obj = FileHandling()
obj.readFile()
print("\r")

#Que2
print("2. count the frequency of words in file")
class FileHandling:
    def readFile(self):
        file = open("testfile1.txt",'r')
        wordCount = {}
        for word in file.read().split():
            if word not in wordCount:
                wordCount[word] = 1
            else:
                wordCount[word] += 1
        for p,q in wordCount.items():
            print(p,q)
obj = FileHandling()
obj.readFile()
print("\r")

#Que3
print("3. copy contents of one file to another file")
class FileHandling:
    def readFile(self):
        file1 = open("testfile1.txt",'r+')
        file2 = open("testfile2.txt",'w')
        for each in file1:
            print(each)
            file2.write(each)
        file2.close()
obj = FileHandling()
obj.readFile()
print("\r")

#Que4
print("combine one file with another line by line")
class FileHandling:
    def readFile(self):
        file1 = open("testfile1.txt",'r')
        file2 = open("testfile2.txt",'r')
        for line1, line2 in zip(file1, file2):
            print(line1 + " " + line2)
obj = FileHandling()
obj.readFile()
print("\r")

#Que5
print("sort the numbers")
class FileHandling:
    def writeFile(self):
        file = open("testfile3.txt", 'w')
        l = []
        print("enter data : ")
        for i in range(0,10):
            data = input()
            l.append(data)
        l.sort()
        file.writelines(l)
        file.close()
        file1 = open("testfile3.txt",'r')
        file2 = open("testfile4.txt", 'w')
        for each in file1:
            print(each)
            file2.write(each)
        file2.close
obj = FileHandling()
obj.writeFile()
