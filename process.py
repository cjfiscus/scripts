InFile=open("operate.txt", 'r')

OutFile=open("operate1.txt", 'w')
for Line in InFile:
        
        
        for Item in ElementList:
        	Item = Item.strip()
        OutFile.write(ElementList[0] + '\t' + ElementList[1] + '\t' + ElementList[5] + '\n')

InFile.close
OutFile.close
