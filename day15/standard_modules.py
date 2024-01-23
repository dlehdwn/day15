#random : 랜덤 역할을 하는 도구 모음
#math : 수학 관련 도구 모음
#datetime : 날짜, 시간을 다르는 도구 모음
#os : 파일 또는 운영체께 접근

from random import *
from math import *
from datetime import *
import os

now = datetime.now()
print(now) # 2024-01-23 12:22:50.221161


p = os.path.join(os.environ['USERPROFILE'],'DESKTOP')
folder_name = "메가스터디 커피"
new_p = os.path.join(p,folder_name)
os.makedirs(new_p)
