fileOne = open("studentmarks.txt", 'a')
repeat = True
while repeat:
    rollnumber = input("Enter Rolln0. : ")
    nameOfStudent = input("Enter Student Name :")
    phyMarks = input("Enter phy marks : ")
    cheMarks = input("Enter che marks : ")
    matMarks = input("Enter mat marks : ")
    engMarks = input("Enter eng marks : ")
    Yes_No = input (" Enter Y/N if you want to create another record ")
    if Yes_No == "N":
        repeat = False
    fileOne.write(rollnumber+','+nameOfStudent+','+phyMarks+','+cheMarks+','+matMarks+'\n')
fileOne.close()