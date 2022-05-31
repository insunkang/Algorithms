from itertools import combinations
def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]


def solution(goods):
    answer = []
    strings = []
    for i in goods:
        string_list = get_all_substrings(i)
        string_list = set(string_list)
        for j in string_list:
            strings.append(j)

    for i in goods:
        string_list = get_all_substrings(i)
        string_list.sort()
        least = len(i)
        string_part = []
        for j in string_list:
            if strings.count(j) == 1:
                if len(j)<least:
                    least = len(j)
                string_part.append(j)
        answer_set = []
        for j in set(string_part):
            if len(j) == least:
                answer_set.append(j)
        answer_set.sort()
        temp_answer_set = " ".join(answer_set)
        if temp_answer_set == "":
            answer.append("None")
        else:
            answer.append(temp_answer_set)



    print(strings)
    print(answer)
    # for i in goods:
    #     string_set = list(i)
    #     print(string_set)
    #     for j in range(len(string_set)):
    #         for k in combinations(string_set,j):
    #             strings.append("".join(k))
    # for i in goods:
    #     string_set = list(i)
    #     for j in range(len(string_set)):
    #         for k in combinations(string_set, j):
    #             if strings.count("".join(k)) > 1:
    #                 continue
    #             else:
    #                 answer.append("".join(k))
    # print(strings)
    # print(answer)
    return answer

# solution(["pencil","cilicon","contrabase","picturelist"])
# solution(["abcdeabcd","cdabe","abce","bcdeab"]	)
from collections import deque
import heapq


def solution(arr, processes):
    answer = []
    answer_heap = []
    work_process = deque()
    work_read_write = deque()
    wait_process = deque()
    wait_read_write = deque()
    time = 1
    answer_check = 0
    processes = deque(processes)
    for i in range(len(processes)):
        processes[i] = processes[i] + " " + str(i)
    while (True):

        if len(work_process) != 0:
            answer_check += 1
            temp_work_process = deque()
            temp_work_read_write = deque()
            for i in range(len(work_process)):
                if work_process[i][2] != "0":
                    temp_work_process.append(work_process[i])
                    temp_work_read_write.append(work_read_write[i])
                else:
                    if work_process[i][0] == "read":
                        temp_arr = "".join(arr)
                        heapq.heappush(answer_heap, (int(work_process[i][5]), temp_arr[int(work_process[i][3]):int(work_process[i][4]) + 1]))
                    else:
                        for j in range(int(work_process[i][3]), int(work_process[i][4]) + 1):
                            arr[j] = work_process[i][5]
                        # print(arr)
            work_process = temp_work_process
            work_read_write = temp_work_read_write

        for i in processes:
            process = i.split(" ")
            if int(process[1]) != time:
                break
            else:
                if len(work_process) == 0:
                    work_process.append(process)
                    work_read_write.append(process[0])
                elif "write" in work_read_write:
                    wait_process.append(process)
                    wait_read_write.append(process[0])
                elif "write" in wait_read_write:
                    wait_process.append(process)
                    wait_read_write.append(process[0])
                elif "read" in work_read_write:
                    if "write" in wait_read_write:
                        wait_process.append(process)
                        wait_read_write.append(process[0])
                    else:
                        if process[0] == "read":
                            work_process.append(process)
                            work_read_write.append(process[0])
                        else:
                            wait_process.append(process)
                            wait_read_write.append(process[0])
                processes.popleft()
                break
        if len(work_process) == 0 and len(wait_process) != 0:
            if "write" in wait_read_write:
                for i in range(len(wait_process)):
                    if wait_process[i][0] == "write":
                        work_process.append(wait_process[i])
                        work_read_write.append("write")
                        del wait_process[i]
                        del wait_read_write[i]
                        break
            else:
                work_process = wait_process
                work_read_write = wait_read_write
                wait_process = deque()
                wait_read_write = deque()

        # print(answer_check, work_process,work_read_write, time, wait_process,wait_read_write)
        for i in range(len(work_process)):
            work_process[i][2] = str(int(work_process[i][2]) - 1)

        time += 1

        if len(work_process) == 0 and len(processes) == 0:
            break
    print(answer_heap)
    while answer_heap:
        a, b = heapq.heappop(answer_heap)
        answer.append(b)

    # print(answer)
    # print(answer_check)

    answer.append(str(answer_check))
    print(answer)
    return answer

solution(["1","2","4","3","3","4","1","5"]	,["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]	)
solution(["1","1","1","1","1","1","1"]	,["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]	)