# # #Lists in python 2021/08/09
# # # days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
# # # print(days)
# # # days.append("Sat")
# # # days.reverse()
# # # print(days)

# # #Lists in python 2021/08/10
# # 하경 = {"name" : "김하궁",
# # "age" : 17,
# # "korean" : True,
# # "fav_food": ["떡볶이","불닭"]}
# # print(하경)
# # 하경["pretty"] = True 
# # print(하경)

# # age = "17"
# # print(age)
# # print(type(age))
# # n_age = int(age)
# # print(n_age)
# # print(type(n_age))

# # def nana():
# #     print("오빠")
# #     print("내가 한거야")
# # nana()
# # print(하경["age"])


# # #Lists in python 2021/08/11
# def plus(a, b):
#     print(a + b)

# def minus(a, b=0):
#     print(a - b)
# plus(6, 8)
# minus(5)

# def nana(name="내 자신"):
#     print("hello",name,"사랑해" )
# nana("하경")
# nana("해영")
# nana()

# def p_plus(a,b):
#     print(a+b) 

# def r_plus(a,b):
#     return a+b

# p_result = p_plus(2,3)
# r_result = 5

# print(p_result, r_result)

# def nana(name, age, are_from, fav_food):
#     return f"Hello {name} you are {age} years old you are from {are_from} you like {fav_food}"
# nana_2 = nana(name="하경",age="17", fav_food="bread", are_from="korea")
# print(nana_2)

# # #Lists in python 2021/08/13
# def plus(a, b):
#     if type(b) is int or type(b) is float:
#         return a+b
#     else:
#       return None

# plus(3, 4.5)

# List in python 2021/08/14
# def age_check(age):
#     print(f"you are {age}")
#     if age < 18:
#         print("you can't drink")
#     elif age ==18 or age ==19:
#         print("you are new to this!")
#     elif age >20 and age < 25:
#         print("you are still kind of young")
#     else:
#         print("enjoy your drink")

# age_check(17)

# days = ("Mon", "Tue", "Wed", "Thu", "Fri")

# for love in days:
#     if love is "Wed":
#         break
#     else:
#         print(love)

# for letter in "hagyeong":
#     print(letter)

# # Modules are math function.
# import math

# print(math.ceil(1.1))
# print(math.fabs(-4.5))

# from math import fsum as love_sum

# print(love_sum([1, 2, 3, 4, 5, 6]))

# from caculator import plus, minus

# print(plus(1,2), minus(4,6))

#List in python 2021/08/15
# import requests

# indeed_result = requests.get ("https://kr.indeed.com/jobs?q=python&limit=50")

# print(indeed_result.text)
# #html 가져오기 끝

#List in python 2021/08/16
# import requests
# from bs4 import BeautifulSoup

# indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")

# indeed_soup = BeautifulSoup(indeed_result.text, "htmlparser")

# pagination = indeed_soup.find("div", {"class":"pagination"})

# pages = pagination.find_all('a')
# spans = []
# for page in pages
#   spans.append(page.find("span"))
# span = spans[:-1]

#List in python 2021/08/17
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "htmlparser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
  pages.append(int(link.string))
  
max_page = pages[-1]