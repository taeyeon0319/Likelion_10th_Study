# 사전준비
# IMAP 설정 & 보안수준 변경 ==> 같이 푸는 PYTHON/기타 참고하기

import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 #지메일 고유 포트번호

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)): #이메일 유효성 검사
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("이메일 내용")

message["Subject"] = "이것은 제목입니다."
message["From"] = "발신자 이메일 주소"
message["To"] = "수신자 이메일 주소"

image = open('codelion.png', 'rb')
with open("codelion.png", "rb") as image :
    image_file = image.read()

image_type = imghdr.what('codelion', image_file)

message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("지메일주소@gmail.com", "######(구글 패스워드)")
sendEmail("지메일주소@gmail.com")
smtp.quit()