# def solution(logs):
#     answer = 0
#     for log in logs:
#         if len(log) > 100:
#             answer += 1
#             continue
#         log_file = log.split(" ")
#
#         if len(log_file) != 12:
#             answer += 1
#             continue
#         if log_file[0] != "team_name" or log_file[3] != "application_name" or log_file[6] != "error_level" or log_file[9] != "message":
#             answer += 1
#             continue
#         check = 0
#         for i in range(len(log_file[2])):
#             if 64 < ord(log_file[2][i]) < 91 or 96 < ord(log_file[2][i]) < 123:
#                 continue
#             else:
#                 check = 1
#                 break
#         if check == 1:
#             answer += 1
#             continue
#         for i in range(len(log_file[5])):
#             if 64 < ord(log_file[5][i]) < 91 or 96 < ord(log_file[5][i]) < 123:
#                 continue
#             else:
#                 check = 1
#                 break
#         if check == 1:
#             answer += 1
#             continue
#         for i in range(len(log_file[8])):
#             if 64 < ord(log_file[8][i]) < 91 or 96 < ord(log_file[8][i]) < 123:
#                 continue
#             else:
#                 check = 1
#                 break
#         if check == 1:
#             answer += 1
#             continue
#         for i in range(len(log_file[11])):
#             if 64 < ord(log_file[11][i]) < 91 or 96 < ord(log_file[11][i]) < 123:
#                 continue
#             else:
#                 check = 1
#                 break
#         if check == 1:
#             answer += 1
#             continue
#
#     print(answer)
#     return answer
#
# solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"])
# # solution(["team_name : db application_name : dbtest error_level : info message : test", "team_name : test application_name : I DONT CARE error_level : error message : x", "team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", "team_name : oberervability application_name : LogViewer error_level : error"])
# # solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange"])
# # solution([ "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test"])
# import copy
#
# def solution(arr, brr):
#     answer = 0
#     temp_arr = copy.deepcopy(arr)
#     for i in range(len(arr)):
#         temp_arr[i] -= brr[i]
#
#     checked_or_not = [0] * len(arr)
#
#     while True:
#
#         print(temp_arr)
#         check_arr = [0] * len(arr)
#         for i in range(0, len(arr) - 1):
#             check_arr[i] = abs(temp_arr[i] + temp_arr[i + 1])
#         check_arr[len(arr) - 1] = 256
#         print(check_arr)
#
#         min_arr = min(check_arr)
#         min_index = []
#         for i in range(len(check_arr)):
#             if check_arr[i] == min_arr:
#                 min_index.append(i)
#         for i in min_index:
#             if temp_arr[i] != 0 and temp_arr[i+1] != 0 and not (temp_arr[i]>0 and temp_arr[i+1]>0) and not (temp_arr[i]<0 and temp_arr[i+1]<0) and checked_or_not[i] ==0:
#                 if abs(temp_arr[i]) > abs(temp_arr[i+1]):
#                     temp_arr[i+1] = 0
#                     checked_or_not[i+1] = -1
#                     if min_arr == 0:
#                         checked_or_not[i] == -1
#                     if temp_arr[i] < 0:
#                         temp_arr[i] = min_arr*-1
#                     else:
#                         temp_arr[i] = min_arr
#                 else:
#                     temp_arr[i] = 0
#                     checked_or_not[i] = -1
#                     if min_arr == 0:
#                         checked_or_not[i+1] == -1
#                     if temp_arr[i+1] < 0:
#                         temp_arr[i+1] = min_arr*-1
#                     else:
#                         temp_arr[i+1] = min_arr
#                 answer += 1
#                 break
#         return_check = 0
#         for i in temp_arr:
#             if i == 0:
#                 return_check += 1
#         if return_check == len(temp_arr):
#             break
#     print(answer)
#
#     return answer
#
# # solution([3, 7, 2, 4]	,[4, 5, 5, 2]	)
# solution([6, 2, 2, 6],[4, 4, 4, 4])

# from itertools import combinations
# def solution(sentences, n):
#     answer = 0
#     points = []
#     string_sets = []
#     for sentence in sentences:
#         point = 0
#         yes_shift = 0
#         string_set = []
#         for i in range(len(sentence)):
#             if sentence[i] != ' ' and sentence[i] not in string_set:
#                 string_set.append(sentence[i].lower())
#             if 64 < ord(sentence[i]) < 91:
#                 point += 2
#                 yes_shift = 1
#             else:
#                 point += 1
#         if yes_shift == 1:
#             string_set.append("shift")
#         points.append(point)
#         string_sets.append(string_set)
#     print(points)
#     print(string_sets)
#     items = [i for i in range(len(sentences))]
#
#     for i in range(len(items)+1,0,-1):
#         for combs in list(combinations(items,i)):
#             check_set = []
#             check_points = 0
#             # print(combs)
#             for comb in combs:
#                 check_set += string_sets[comb]
#                 check_points += points[comb]
#
#             if len(set(check_set)) <= n and check_points > answer:
#
#                 answer = check_points
#     print(answer)
#     return answer
#
# solution(["line in line", "LINE", "in lion"],5)
# solution(["ABcD", "bdbc", "a", "Line neWs"],7)

# def solution(num_teams, remote_tasks, office_tasks, employees):
#     answer = []
#     team_members_statuses = [[] * i for i in range(num_teams)]
#     team_members_len = [[] * i for i in range(num_teams)]
#     print(team_members_statuses)
#     employee_member = 1
#     for employee in employees:
#         employee_tasks = employee.split(" ")
#         team_members_len[int(employee_tasks[0])-1].append(employee_member)
#         print(employee_tasks)
#
#         task_check = 0
#         for task in employee_tasks:
#             if task in remote_tasks:
#                 task_check += 1
#         print(task_check,len(employee_tasks)-1)
#         if task_check == len(employee_tasks)-1:
#             team_members_statuses[int(employee_tasks[0])-1].append(employee_member)
#             answer.append(employee_member)
#         employee_member += 1
#
#     print(team_members_statuses)
#     print(team_members_len)
#     for i in range(len(team_members_statuses)):
#         if len(team_members_statuses[i]) == len(team_members_len[i]):
#             answer.remove(team_members_statuses[i][0])
#
#     print(answer)
#     return answer

# solution(3,["development","marketing","hometask"]	,["recruitment","education","officetask"]	,["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]	)
import heapq
def solution(abilities, k):
    answer = 0
    abilities.sort(reverse = True)
    print(abilities)
    last_chance = 0
    check_priority = []
    check_priority_length = 0
    if len(abilities)%2 !=0:
        check_priority_length = len(abilities)//2 + 1
        last_chance = 1
    else:
        check_priority_length = len(abilities)//2
    print("check_pro_len",check_priority_length)
    print(last_chance)
    check_while = 0
    while check_while < len(abilities):
        if last_chance == 1 and check_while == len(abilities) -1:
            check_priority.append(abilities[check_while])
            break
        else:
            check_priority.append(abilities[check_while] - abilities[check_while + 1])
        if last_chance == 1 and check_while == len(abilities)-2:
            check_while += 1
        else:
            check_while += 2
    print(check_priority)
    print(last_chance)
    q = []
    for i in range(len(check_priority)):
        if last_chance == 1 and i == len(check_priority)-1:
            heapq.heappush(q,(-check_priority[i], (abilities[i*2]),))
        else:
            heapq.heappush(q,(-check_priority[i],(abilities[i*2],abilities[i*2+1])))

    print(q)

    check_k=0
    while q:
        a,b = heapq.heappop(q)
        if check_k < k:
            if type(b) == int:
                answer += b
            else:
                answer += b[0]
            check_k += 1
        else:
            if type(b) == int:
                continue
            else:
                answer += b[1]
        print(answer)
    print(answer)
    return answer

# solution([2, 8, 3, 6, 1, 9, 1, 9]	,2)
solution([7, 6, 8, 9, 10]	,1)