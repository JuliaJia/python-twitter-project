list1 = ["1","2"]

str1 = ",".join(list1)

print(str1)

str2 = "/api/tweets/{}/".format(123)

print(str2)
URL_STR = "/api/tweets/{user_id}/{name}"
str3 = URL_STR.format(name="Ryoma",user_id=123456)

print(str3)

list2 = str1.split(",")
print(list2)