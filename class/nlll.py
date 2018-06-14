#coding:utf-8
import DataApi
class student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def getName(self):
        return self.name

    def getAvgScore(self):
        avg = (self.math+self.math+self.english)/3
        return avg

zhang = student('张同学',90,98,89)
wang = student('王同学',90,90,87)
# print(wang.math)
# print("姓名：",zhang.getName())
# print("平均成绩",zhang.getAvgScore())
# print("------------------------------")
# print("姓名：",wang.getName())
# print("平均成绩",wang.getAvgScore())


class university:
    def __init__(self,student_table,school):
        self.student_table = student_table
        self.school = school

    def mathavg(self):
        count = 0
        mathsum = 0
        for stu in self.student_table:
            # mathsum = student(stu).math
            # print(stu.math)
            mathsum = mathsum + stu.math
            count = count + 1
        avg = mathsum/count
        return avg

a = university([zhang,wang],'GDUFS').mathavg()
print("平均分：",a)