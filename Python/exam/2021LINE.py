##1

# def solution(table, languages, preference):
#     answerList = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
#     languageList = []
#     pointList = [0,5,4,3,2,1]
#
#     for i in table:
#         tableValue = list(map(str,i.split(" ")))
#         print(tableValue)
#         point = 0
#         for j in range(len(languages)):
#             if languages[j] in tableValue:
#                 print(tableValue[j])
#                 print(tableValue.index(tableValue[j]))
#                 point += pointList[tableValue.index(languages[j])]* preference[j]
#                 print(point)
#         languageList.append(point)
#
#     print(languageList)
#     answerNumber = max(languageList)
#
#     result = []
#
#     for k in range(len(answerList)):
#         if languageList[k] == answerNumber:
#             result.append(answerList[k])
#     print(result)
#     result.sort()
#     print(result)
#     print(result[0])

    # return answer
# solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
#          ["PYTHON", "C++", "SQL"], [7, 5, 5])
# solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
#          ["JAVA", "JAVASCRIPT"], [7, 5])


##2

# def solution(inp_str):
#     answer = []
#
#     # Step 1
#     if len(inp_str) < 8 or len(inp_str) >15:
#         answer.append(1)
#
#     # Step 2
#     Step2 = [0] * 4
#
#     specialStr = [126,33,64,35,36,37,94,38,42]
#
#     for i in inp_str:
#         if ord(i) >= 65 and ord(i) <= 90:
#             Step2[0] = 1
#         else:
#             if ord(i) >= 97 and ord(i) <= 122:
#                 Step2[1] = 1
#             else:
#                 if ord(i) >= 48 and ord(i) <= 57:
#                     Step2[2] = 1
#                 else:
#                     if ord(i) in specialStr:
#                         Step2[3] = 1
#                     else:
#                         if 2 not in answer:
#                             answer.append(2)
#
#     # Step 3
#
#     if sum(Step2) < 3:
#         answer.append(3)
#
#     # Step 4
#
#     if len(inp_str) >= 4:
#         for j in range(len(inp_str) - 4):
#             if inp_str[j] == inp_str[j + 1]:
#                 if inp_str[j + 1] == inp_str[j + 2]:
#                     if inp_str[j + 2] == inp_str[j + 3]:
#                         answer.append(4)
#                         break
#
#     # Step 5
#
#     for k in inp_str:
#         if inp_str.count(k) >=5:
#             answer.append(5)
#             break
#
#
#     if len(answer) == 0:
#         answer.append(0)
#     print(answer)
#
# solution("ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824ZzZz9Z824")



# 3

# def solution(enter, leave):
#     answer = [0] * len(enter)
#
#     for i in range(1, len(enter) + 1):
#         for j in range(1, len(leave) + 1):
#             if i != j:
#                 if enter.index(i) > enter.index(j) and leave.index(i) < leave.index(j):
#                     answer[i - 1] += 1
#                 elif enter.index(i) < enter.index(j) and leave.index(i) > leave.index(j):
#                     answer[i - 1] += 1
#                 else:
#
#                     if leave.index(i) < leave.index(j) and leave.index(i) > 0:
#                         leaveFirst = leave[0:leave.index(i)]
#                         if enter.index(i) > enter.index(j) and enter.index(i) < len(enter)-1:
#                             enterLate = enter[enter.index(i):len(enter)]
#                             for k in leaveFirst:
#                                 if k in enterLate:
#                                     answer[i - 1] += 1
#                                     break
#                         elif enter.index(i) < enter.index(j) and enter.index(i) > len(enter)-1:
#                             enterLate = enter[enter.index(j): len(enter)]
#                             for k in enterLate:
#                                 if k in leaveFirst:
#                                     answer[i - 1] += 1
#                                     break
#                     elif leave.index(i) > leave.index(j) and leave.index(j) > 0:
#                         leaveFirst = leave[0:leave.index(j)]
#                         if enter.index(i) > enter.index(j) and enter.index(i) < len(enter)-1 :
#                             enterLate = enter[enter.index(i): len(enter)]
#                             for k in leaveFirst:
#                                 if k in enterLate:
#                                     answer[i - 1] += 1
#                                     break
#                         elif enter.index(i) < enter.index(j) and enter.index(i) > len(enter)-1:
#                             enterLate = enter[enter.index(j): len(enter)]
#                             for k in enterLate:
#                                 if k in leaveFirst:
#                                     answer[i - 1] += 1
#                                     break
#
#
#
#
#     print(answer)
#
#
# solution([1,4,2,3],[2,1,3,4])

#CLI #1


# Each FlagName to List
# def findFlagName(flag_rules):
#
#     flag_names = []
#
#     for i in flag_rules:
#         rule = list(map(str, i.split(" ")))
#         flag_names.append(rule[0])
#
#     return flag_names
#
#
# # Each FlagArgType to List
# def fineFlagArgType(flag_rules):
#
#     flag_argument_type = []
#
#     for i in flag_rules:
#         rule = list(map(str, i.split(" ")))
#         flag_argument_type.append(rule[1])
#
#     return flag_argument_type
#
#
# # Find commands that match with Rules
# def commandsMatchRule(program, flag_names, flag_argument_type, command):
#
#     contents = list(map(str, command.split(" ")))
#
#
#     # Program Name
#     if contents[0] != program:
#         return False
#
#     index = 1
#     while index < len(contents):
#         now_flag_name = contents[index]
#
#         if now_flag_name in flag_names:
#             # STRING
#             if flag_argument_type[flag_names.index(now_flag_name)] == "STRING":
#                 if index + 1 < len(contents):
#                     check = 0
#                     for j in contents[index + 1]:
#
#                         if 90 >= ord(j) >= 65:
#                             check += 1
#                             continue
#                         elif 122 >= ord(j) >= 97:
#                             check += 1
#                             continue
#                         else:
#                             return False
#                     if check == len(contents[index + 1]):
#                         index += 2
#                         continue
#                 else:
#                     return False
#
#             # NUMBER
#             elif flag_argument_type[flag_names.index(now_flag_name)] == "NUMBER":
#                 if index + 1 < len(contents):
#                     check = 0
#                     for j in contents[index + 1]:
#                         if 57 >= ord(j) >= 48:
#                             check += 1
#                         else:
#                             return False
#                     if check == len(contents[index + 1]):
#                         index += 2
#                         continue
#                 else:
#                     return False
#
#             # NULL
#             elif flag_argument_type[flag_names.index(now_flag_name)] == "NULL":
#                 if index + 1 < len(contents):
#                     if contents[index + 1] in flag_names:
#                         index += 1
#                         continue
#                     else:
#                         return False
#                 else:
#                     return True
#         else:
#             return False
#
#
# def solution(program, flag_rules, commands):
#     answer = []
#     flag_names = findFlagName(flag_rules)  # Each Rule to List
#     flag_argument_type = fineFlagArgType(flag_rules)
#
#     for i in commands:
#         answer.append(commandsMatchRule(program, flag_names, flag_argument_type, i))
#
#     print(flag_names)
#     print(flag_argument_type)
#
#     print(answer)
#     # return answer



# 2

# Each FlagName to List
def findFlagName(flag_rules):

    flag_names = []

    for i in flag_rules:
        rule = list(map(str, i.split(" ")))
        flag_names.append(rule[0])

    return flag_names


# Each FlagArgType to List
def fineFlagArgType(flag_rules):

    flag_argument_type = []

    for i in flag_rules:
        rule = list(map(str, i.split(" ")))
        flag_argument_type.append(rule[1])

    return flag_argument_type


# Find commands that match with Rules
def commandsMatchRule(program, flag_names, flag_argument_type, command):

    contents = list(map(str, command.split(" ")))


    # Program Name
    if contents[0] != program:
        return False

    index = 1
    while index < len(contents):
        now_flag_name = contents[index]

        if now_flag_name in flag_names:
            # STRING
            if flag_argument_type[flag_names.index(now_flag_name)] == "STRING":
                if index + 1 < len(contents):
                    check = 0
                    for j in contents[index + 1]:

                        if 90 >= ord(j) >= 65:
                            check += 1
                            continue
                        elif 122 >= ord(j) >= 97:
                            check += 1
                            continue
                        else:
                            return False
                    if check == len(contents[index + 1]):
                        index += 2
                        continue
                else:
                    return False

            #STRINGS
            elif flag_argument_type[flag_names.index(now_flag_name)] == "STRINGS":
                next_current_string = 0
                print(contents[index])
                while index + 1 < len(contents) and contents[index + 1] not in flag_names:

                    check = 0
                    for j in contents[index + 1]:

                        if 90 >= ord(j) >= 65:
                            check += 1
                            continue
                        elif 122 >= ord(j) >= 97:
                            check += 1
                            continue
                        else:
                            return False

                    if check == len(contents[index + 1]):
                        next_current_string += 1
                        index += 1

                if next_current_string == 0:
                    return False
                else:
                    continue


            # NUMBER
            elif flag_argument_type[flag_names.index(now_flag_name)] == "NUMBER":
                if index + 1 < len(contents):
                    check = 0
                    for j in contents[index + 1]:
                        if 57 >= ord(j) >= 48:
                            check += 1
                        else:
                            return False
                    if check == len(contents[index + 1]):
                        index += 2
                        continue
                else:
                    return False

            # NUMBERS
            elif flag_argument_type[flag_names.index(now_flag_name)] == "NUMBERS":

                checkList = []
                for o in range(index, len(contents)):
                    if contents[o] not in flag_names:
                        checkList.append(o)
                    else:
                        break

                for p in checkList:
                    check = 0
                    for j in p:
                        if 57 >= ord(j) >= 48:
                            check += 1
                        else:
                            return False
                    if check == len(contents[index + 1]):
                        index += 1
                    else:
                        return False




            # NULL
            elif flag_argument_type[flag_names.index(now_flag_name)] == "NULL":
                if index + 1 < len(contents):
                    if contents[index + 1] in flag_names:
                        index += 1
                        continue
                    else:
                        return False
                else:
                    return True
        else:
            return False


def solution(program, flag_rules, commands):
    answer = []
    flag_names = findFlagName(flag_rules)  # Each Rule to List
    flag_argument_type = fineFlagArgType(flag_rules)

    for i in commands:
        answer.append(commandsMatchRule(program, flag_names, flag_argument_type, i))

    print(flag_names)
    print(flag_argument_type)

    print(answer)
    # return answer

# solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -n 100 -s hi -e -s", "lien -s Bye"])
# solution("line",["-s STRINGS", "-n NUMBERS", "-e NULL"],["line -s str str", "line -s -s str"])
solution("line",["-s STRINGS", "-n NUMBERS", "-e NULL"],["line -n 100 102 -s hi -e", "line -n id pwd -n 100"])