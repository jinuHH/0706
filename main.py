# cnt = 0
# loop = 0
# for idx in range(1, 101):
#     loop = loop + 1
#     if idx % 3 == 0:
#         loop = loop + 1
#         if idx % 4 == 0:
#             cnt = cnt + 1
# print("12의 배수의 개수: ", cnt)
# print("조건 확인 개수: ", loop)
#
# cnt = 0
# loop = 0
# for idx in range(1,101):
#     loop = loop + 1
#     if idx % 4 == 0:
#         loop = loop + 1
#         if idx % 3 == 0:
#             cnt = cnt + 1
# print("12의 배수의 개수: ", cnt)
# print("조건 확인 개수: ", loop)

# #윤년 판별
# year = 2023
# #윤년의 조건 - 둘 중 하나만 True이면 True
# #1. 4의 배수이고 100의 배수가 아닌 경우
# #2. 400의 배수인 경우
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(year, "는 윤년")
# else:
#     print(year, "는 윤년이 아님")

# a = 10 + 20
# b = 30
# print(id(a))
# print(id(b))
# print(type(10.3))
#
# x= 10
# y=10.3
# result = x+y
# print(result)
# print(type(result))

# help(print)
# print("{0} 은 {1}을 좋아합니다.".format("아담","신촌 라이브 카페"))
# print("{1} 은 {0}을 보고 만든건데 초상권에 대한 비용을 지불하지 않았습니다.".format("원빈", "아담"))
# original = "원빈"
# copy = "아담"
# print(f"{copy} 은 {original}을 보고 만든건데 초상권에 대한 비용을 지불하지 않았습니다.")
#
# name = input("이름을 적어주세요: ")
# print(name)
#
# try:
#     age = int(input("나이를 입력해주세요: "))
#     print(age + 1)
# except:
#     print("문제발생")
# print("프로그램 종료")

#여러 개 입력
hobbys = input("취미 , 로 구분해서 입력: ").split(",")
for hobby in hobbys:
    print(hobby)
