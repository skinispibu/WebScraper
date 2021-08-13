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
def plus(a, b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
      return None

print(plus(3, 4.5))