print("hello world")

# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))
# print(python.count("n"))

# print("a" + "b")
# print("a","b")

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요." % "A")

# print("나는 %s살입니다." % 20)

# print("나는 %s색과 %s색을 좋아해요." % ("파란","빨간"))

# print("나는 {}살입니다.". format(20))
# print("나는 {}색과 {}색을 좋아해요." . format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." . format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." . format("파란","빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요."

# print("백문이 불여일견\n백견이 불여일타")

# print('저는 '"나도코딩"'입니다.')

# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# print("C:\\Users\\samsung\\Desktop\\Study\\파이썬\\Python>")

# print("Red Apple\rPine")

# print("Redd\bApple")

# print("Red\tApple")

# url = "http://naver.com"
# my_str = url.replace("http://", "")
# # print(my_str)
# my_str = my_str[:my_str.index(".")]
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석","조세호","박명수"]
# print(subway)

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20 , True]
# print(mix_list)

# num_list.extend(mix_list)
# print(num_list)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # true
# print(5 in cabinet) # false

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# 간 손님
# del cabinet["A-3"]
# print(cabinet)

# key 들만 출력
# print(cabinet.keys())

# value 들만 출력
# print(cabinet.values())

# 둘 다 출력
# print(cabinet.items())

# 다 지우기
# cabinet.clear()
# print(cabinet)

# menu = ("돈까스", "치즈돈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") # 튜플은 값 변경 불가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 사람)
# print(java & python)
# print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 사람)
# print(java | python)
# print(java.union(python))

# 차집합 (java 힐 스 있지만 python은 할 줄 모르는 사람)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람 늘어남
# python.add("김태호")
# print(python)

# java를 잊어먹음
# java.remove("김태호")
# print(java)

# 자료구조의 변경
# 커피숍

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# from random import *

# users = range(1, 21)
# users = list(users)

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4)

# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print(" -- 축하합니다 --")

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요.")
# else:
#     print("너무 추워요. 나가지 마세요")

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# randrange()
# for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0} 님 커피가 준비되었습니다.".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0} 님 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print
#     print("{0} 님 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0} 님 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# from re import A

# absent = [2,5] # 결석
# no_book = [7] # 책이 없음
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# from random import *

# people = range(1, 51)
# drive = range(5, 50)
# drive = list(drive)
# times = range(5, 15)
# times = list(times)

# print(drive)
# shuffle(drive)
# print(drive)

# print(times)
# shuffle(times)
# print(times)

# print("{0}번째 손님 (소요시간 : {1} )".format(people[0],times[0]) + "분")

# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1 - 50 이라는 수 (승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission
# balance = 0 # 잔액
# balance = deposit(balance , 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

# 같은 학교 같은 학년 같은 반 같은 수업.
# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))


# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang = "파이썬", age = 20)
# profile(main_lang = "파이썬", age = 20, name = "김태호")
    
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python","Java","C","C++","C#","JavaScript")
# profile("김태호", 25, "Kotlin","Swift","","","")

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# gender = 1

# def std_weight(height, weight):
#     if gender == 1:
#         man = height * height * 22
#         print("키 {0} 남자의 표준 체중은 {1} 입니다.".format(height, weight))
#     else:
#         woman = height * height * 21

# def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# import sys
# print("Python","Java", file=sys.stdout)
# print("Python","Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(100000000000))
# # 3자리 마다 콤마를 찍어주기
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))
# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 지릿수 확보하기
# # 돈이 많으면 행봉하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(100000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r", encoding = "utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt","r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt","r", encoding = "utf8")
# lines = score_file.readline() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

# import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("-{0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 잇는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# tank2_name = "탱크2"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location,damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크",150, 35)

# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80 ,5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage) )

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#_________________________________________________________________

# from random import *

# # 일반 유닛
# from turtle import speed


# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         # print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))
# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정 시간 동안 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150 , 1, 5)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드일 때 -> 시즈모드 해제    
#         else:
#             print("{0} : 시즈모드로 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

        
# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         # print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,"레이스", 80, 20, 5)
#         self.clocked = False # 클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True: # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked == False
#         else: # 클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg") # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")

# # 게임 시작
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attact_units = []
# attact_units.append(m1)
# attact_units.append(m2)
# attact_units.append(m3)
# attact_units.append(t1)
# attact_units.append(t2)
# attact_units.append(w1)

# # 전군 이동
# for unit in attact_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드 , 레이스 : 클로킹)
# for unit in attact_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attact_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attact_units:
#     unit.damaged(randint(5, 21)) # 공격을 랜덤을 받음 (5 ~ 20)

# # 게임 종료
# game_over()

# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 별쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# -----------------------------------------------------------
# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type\
#             , self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억","2010년")
# house2 = House("마포", "오피스텔", "전세", "5억","2007년")
# house3 = House("송파", "빌라", "월세", "500/50","2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)

# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

#_______________________________________________________________

# class SoldOutError(Exception):
#     pass
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만서, 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다." \
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하셨습니다.")
#     except SoldOutError:
#         print("재고 소진되어 더 이상 주문을 받지 않습니다.")
#         break

# __________________________________________________________

# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때 가격

# import theater_module as mv # mv는 별명
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import *
# price(3)
# price_soldier(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# # price_soldier(7)

# from theater_module import price_soldier as pr # 군인의 별명이 pr
# pr(5)

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThillandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

#_____________________________________________________

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1,2,3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

#_____________________________________________

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후