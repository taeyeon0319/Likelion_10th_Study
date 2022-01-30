# Googletrans : 언어감지, 번역 하는 라이브러리
# pip install googletrans==4.0.0-rc1
# 참고문헌 https://py-googletrans.readthedocs.io/en/latest/
# 프랑스어 : fr  베트남어 : vi  스페인어 : es  중국어:zh-CN
# 아랍어 : ar  독일어 : de  몽골어 : mn  힌디어 : hi

from googletrans import Translator

translator = Translator()

sentence = input("번역을 원하는 문장을 입력해주세요 : ")
detected = translator.detect(sentence) #어느나라 언어인지 감지하기

dest = input("어떤 언어로 번역을 원하시나요? : ")

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("==========출 력 결 과==========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("==============================")
