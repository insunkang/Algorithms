# def solution(card_numbers):
#     answer = [0] * len(card_numbers)
#     for i in range(len(card_numbers)):
#         one = 0
#         two = 0
#         if len(card_numbers[i])==19 or len(card_numbers[i])==16:
#             number = card_numbers[i].replace('-', '')
#             for j in range(len(number)):
#                 if j % 2 == 0:
#                     oneSum = int(number[j]) * 2
#                     if oneSum >= 10:
#
#                         a = oneSum // 10 + oneSum % 10
#
#                         one += a
#                     else:
#                         one += oneSum
#                 else:
#                     two += int(number[j])
#             if (one + two) % 10 == 0:
#                 answer[i] = 1
#         else:
#             answer[i] = 0
#
#     print(answer)
# solution(["3285-3764-9934-2453", "3285376499342453", "3285-3764-99342453", "328537649934245", "3285376499342459", "3285-3764-9934-2452"])

def solution(scores, k):
    answer = 0
    check = scores[0]
    answerA = []
    appendA = [scores[0]]
    kSum = 0
    for i in range(1, len(scores)):
        a = scores[i] - check
        if i + 1 < len(scores):
            b = scores[i + 1] - scores[i]
            if a <= b:
                appendA.append(scores[i])
            else:
                kSum += 1
                answerA.append(appendA)
                appendA = [scores[i]]
                check = scores[i]
        else:
            if len(answerA)==k-2:
                print("1234")
                answerA.append(appendA)
                answerA.append([scores[i]])
            else:
                print(answerA)
                print(appendA)
                print(scores[i])
                appendA.append(scores[i])
                answerA.append(appendA)

    print(answerA)
    return answer
solution([1,2,12,14,15],2)