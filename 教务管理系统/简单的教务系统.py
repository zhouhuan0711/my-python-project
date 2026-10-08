# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1．添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2．修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3．删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4．查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5．列出所有学生：遍历所有学生信息并输出。
# 6．统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7．退出系统。
# 存储学生：key学生名字，value内层字典{"语文":xx,"数学":xx,"英语":xx}


student_dict = {}

chinese_total = 0
math_total = 0
english_total = 0
print("=====欢迎使用教务成绩管理系统=====")
system = """
============教务管理系统============
1. 添加学生信息
2. 修改学生信息
3. 删除学生信息
4. 查询学生信息
5. 列出所有学生
6. 统计班级成绩
7. 退出系统
===================================
"""
# students = {"name" : {"语文成绩":  , "数学成绩":  ,"英语成绩":  }
while True:
    print(system)
    op = input("请输入您要执行的功能序号：")
    match op:
        case "1":
            name = input("请输入新增的学生姓名：")
            if name in student_dict:
                print(f"{name}信息已存在")
                continue
            chinese_score = int(input("请输入该学生的语文成绩:"))
            math_score = int(input("请输入该学生的数学成绩:"))
            english_score = int(input("请输入该学生的英语成绩:"))
            student_dict[name] = {"语文成绩": chinese_score, "数学成绩": math_score, "英语成绩": english_score}
            print("---添加学生信息成功---")
            print(f'添加的学生姓名：{name},语文成绩：{chinese_score},数学成绩：{math_score},英语成绩：{english_score}')

        case "2":
            name = input("请输入要修改的学生姓名：")
            if name not in student_dict:
                print(f"{name}信息不存在")
            else :
                chinese_score = int(input("请输入该学生的语文成绩:"))
                math_score = int(input("请输入该学生的数学成绩:"))
                english_score = int(input("请输入该学生的英语成绩:"))
                student_dict[name] = {"语文成绩": chinese_score, "数学成绩": math_score, "英语成绩": english_score}
                print("---修改学生信息成功---")
                print(f'修改后的学生姓名：{name},修改后语文成绩：{chinese_score},修改后数学成绩：{math_score},修改后英语成绩：{english_score}')
                continue

        case "3":

            name = input("请输入要删除的学生姓名：")

            if name  in student_dict:
                student_info = student_dict[name]
                del student_dict[name]
                print("---删除学生信息成功---")
                print(f'所删除的学生姓名：{name},语文成绩：{student_info["语文成绩"]},数学成绩：{student_info["数学成绩"]},英语成绩：{student_info["英语成绩"]}')
                continue

            else:

                print(f"{name}信息不存在")

        case "4":

            name = input("请输入要查询的学生姓名：")

            if name  in student_dict:
                student_info = student_dict[name]
                print("---查询学生信息成功---")
                print(f'学生姓名：{name},语文成绩：{student_info["语文成绩"]},数学成绩：{student_info["数学成绩"]},英语成绩：{student_info["英语成绩"]}')
                continue

            else:

                print(f"{name}信息不存在")

        case "5":
            for student_name, student_info in student_dict.items():
                print(f'学生姓名：{student_name},语文成绩：{student_info["语文成绩"]},数学成绩：{student_info["数学成绩"]},英语成绩：{student_info["英语成绩"]}')

        case "6":
            # =========统计班级成绩，自己写代码=========
            chinese_total = 0
            math_total = 0
            english_total = 0
            if len(student_dict) == 0:
                print("暂无学生，无法统计！")
                continue
            for student_name, student_info in student_dict.items():
                chinese_total += student_info["语文成绩"]
                math_total += student_info["数学成绩"]
                english_total += student_info["英语成绩"]
            chinese_avg = chinese_total/len(student_dict)
            math_avg = math_total/len(student_dict)
            english_avg = english_total/len(student_dict)
            print(f'语文总分是:{chinese_total}，数学总分是:{math_total}，英语总分是:{english_total}')
            print(f'语文平均分是:{chinese_avg:.1f}，数学平均分是：{math_avg:.1f}，英语平均分是：{english_avg:.1f}')
            continue


        case "7":
            print("退出教务管理系统，再见！")
            break

        case _:
            print("输入序号非法，请重新选择！")
