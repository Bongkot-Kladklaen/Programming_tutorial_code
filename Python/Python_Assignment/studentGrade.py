try:
    # fw=open("Score.txt","a",encoding="utf-8")
    # while True:
    #     studentid = input("รหัสนักเรียน: ")
    #     if studentid == "exit":
    #         break
    #     score = input("ป้อนคะแนน: ")
    #     fw.writelines(studentid + "\t" + score + "\n")
    # fw.close()
    fr = open("score.txt","r",encoding="utf-8")
    fw = open("grade.txt","w",encoding="utf-8")
    grade = None
    for line in fr.readlines():
        score=int(line[-4:].strip())
        studentid=line[:-4].strip()
        if score >= 80:
            grade = "A"
        elif score >= 70 :
            grade = "B"
        elif score >= 60 :
            grade = "C"
        elif score >= 50 :
            grade = "D"
        else:
            grade = "F"
        
        fw.writelines("รหัส = " + str(studentid) + "\t" + "คะแนน = " + str(score) + "\t" +  "เกรด = " + grade + "\n")

except Exception as e:
    print(e)