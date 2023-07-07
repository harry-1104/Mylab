# import math

try:
        snt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97]
        for i in range(0, len(snt)+1, 1):
                j = snt[i]
                print("\nSNT: {}".format(j))
                bth1 = 4 * j * j + 1
                print("\t4pp+1={}".format(bth1))
                bth2 = 6 * j * j + 1
                print("\t6pp+1={}".format(bth2))

        # bai khac
        # uoc = []
        # for i in range(0, len(snt), 1):
        #         p = snt[i]
        #         sothu = p*p*p*p
        #         print("p = {}\nsố thử: {}".format(p, sothu))
        #         uoc = []
        #         for j in range(1, sothu + 1, 1):
        #                 if sothu % j == 0:
        #                         uoc.append(j)
        #         tong = 0
        #         for k in uoc:
        #                 tong = tong + k
        #         if math.sqrt(tong) == int(math.sqrt(tong)):
        #                 print("chấp nhận số thử: {}\n\ttổng các ước = {}\n".format(sothu, tong))
        #         print("------------")
                                
except Exception as bugg:
        print(bugg)
