import random
import time

# 반복하여 출력시키기
while True:
    print(random.choice(["된장찌개", "피자", "제육덮밥", "떡볶이", "김치찌개", "치킨", "찜닭", "초밥"]))
    time.sleep(1) #1초씩 간격을 두고 반복 출력됨


# 데이터 상자 만들기
lunch = random.choice(["된장찌개", "피자", "파스타"])
dinner = random.choice(["김밥", "라면", "떡볶이"])
print(lunch) 


# Dictionary
information={'고향':'서울', '취미':'영화보기', '좋아하는 음식':'치킨'}
print(information)
print(information.get('취미'))


# List와 Dictionary
information = {'고향':'서울', '취미':'영화보기', '좋아하는 음식':'치킨'}
foods = ['된장찌개', '피자', '제육볶음'] #0, 1, 2
information["특기"]="피아노치기" #딕셔너리 추가하기
print(information)

for x in range(len(foods)):
    print(foods[x])

for x, y in information.items():
    print(x)
    print(y)


# 집합
foods = ['된장찌개', '피자', '제육볶음', '된장찌개']
foods_set = set(foods)
print(foods)
print(foods_set) #중복되는 된장찌개가 1번만 나옴 (중복이 알아서 제거됨)

menu1 = set(['된장찌개', '피자', '제육볶음'])
menu2 = set(['된장찌개', '김치찌개', '떡국'])
menu3 = menu1 | menu2 #합집합
menu4 = menu1 & menu2 #교집합
menu5 = menu1 - menu2 #차집합
print(menu3)
print(menu4)
print(menu5)


#if
food = random.choice(['된장찌개', '피자', '제육볶음'])

if(food=='제육볶음'):
    print("곱배기 주세요")
else :
    print("종료")


#함수
def make_dolcelatte():
    print("1. 얼음을 넣는다.")
    print("2. 연유를 30ml 넣는다.")
    print("3. 찬 우유를 넣는다.")
    print("4. 에스프레소샷을 넣는다.")

def make_blueberry_smoothie():
    print("1. 블루베리 20g을 넣는다.")
    print("2. 우유 300ml를 넣는다..")
    print("3. 얼음을 넣는다.")
    print("4. 믹서기에 간다..")

def make_simple_latte():
    print("1. 커피를 넣는다.")
    print("2. 우유를 넣는다.")
    print("3. 신나게 섞는다.")

make_blueberry_smoothie() #블루베리스무디 만드는 방법이 출력됨