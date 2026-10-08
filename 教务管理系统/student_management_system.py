# 先定义类（学生）
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def update_score(self, chinese, math, english):
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return (f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} "
                f"| 英语：{self.english} | 总分：{(self.chinese + self.math + self.english)}")


# 定义教务管理系统
class StudentManagement:
    def __init__(self):
        self.list = []  # 定义一个空列表

    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
        for s in self.list:
            if s.name == name:
                print("这个学生已存在")
                return
        chinese = int(input("请输入学生的语文成绩："))
        math = int(input("请输入学生的数学成绩："))
        english = int(input("请输入学生的英语成绩："))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            new_student = Student(name, chinese, math, english)
            self.list.append(new_student)
        else:
            print("输入的成绩应为0-100之间")
            return

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生的姓名：")
        for s in self.list:
            if s.name == name:
                print(f"{s}")
                s.chinese = int(input("请输入新的学生的语文成绩："))
                s.math = int(input("请输入新的学生的数学成绩："))
                s.english = int(input("请输入新的学生的英语成绩："))
                print("修改成功")
                return
        print("没有该学生的信息")
        return

    # 删除学生成绩
    def del_student(self):
        name = input("请输入要删除的学生的姓名：")
        for s in self.list:
            if s.name == name:
                self.list.remove(s)
                print("已经删除成功")
                return
        print("该学生不存在")

    # 查询学生
    def query_student(self):
        name = input("请输入要查询的学生的姓名：")
        for s in self.list:
            if s.name == name:
                print(f"{s}")
                return
        print("没有这个人")

    # 展示全部学生成绩
    def show_student(self):
        for s in self.list:
            print(f"{s}")

    # 运行系统
    def run(self):
        print("欢迎使用教务系统")
        while True:
            print()
            print("#" * 60)
            print("1.添加学生成绩   2.修改学生成绩   3.删除学生成绩   "
                  "4.查询学生成绩   5.展示全部学生成绩   6.退出")
            print("#" * 60)
            choose = input("请输入1-6：")
            try:
                match choose:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.del_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.show_student()
                    case "6":
                        print("bye bye")
                        break
                    case _:
                        print("操作不合法")
            except ValueError:
                print("输入的数据有问题，请检查并重新输入。")
            except Exception as e:
                print("程序报错,程序即将中断错误原因：", e)
                break


# 启动程序
if __name__ == "__main__":
    manager = StudentManagement()
    manager.run()
