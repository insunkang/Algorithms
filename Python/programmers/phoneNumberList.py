def solution(phone_book):
    answer = True
    phone_book=[str (i) for i in phone_book]
    for i in range(0,len(phone_book)-1):
        a = str(phone_book[i])

        for j in range(i+1,len(phone_book)):
            b = str(phone_book[j])

            if len(a) <= len(b):
                k = b[0:len(a)]
                if k==a:
                    # return False
                    print("False")
            else:
                k = a[0:len(b)]
                if k==b:
                    # return False
                    print("False")
    print(answer) 

solution([119, 97674223, 1195524421])