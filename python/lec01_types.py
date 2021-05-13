###################################################
## Challenge day 1
## Lecture 1.0 ~ 1.2
## about : types
## string, number, boolean, None, list, tuple, dictionary
## None : Java 의 undefined와 동일
## tuple : list와 달리 길이나 요소값/데이터 변경 불가
## dictionary : Key와 Value를 한 쌍으로 갖는 자료형
##              (리스트나 튜플처럼 sequential로 해당 요솟값을 구하지 않고
##              Key를 통해 Value를 얻음) 
###################################################

### String
# days = "Mon, Tue, Wed, Thu, Fri"
# print(days)

### list
# days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# days = ("Mon", "Tue", "Wed", "Thu", "Fri")
# print("Mon" in days)
# print(len(days))
# days.append("Sat")
# print(days)
# days.reverse()
# print(days)

### tuple
days = ("Mon", "Tue", "Wed", "Thu", "Fri")
print(days)
print("Mon" in days)
print(len(days))

#######################################

### dictionary
helen = {
    "name": "helen",
    "age" : 29,
    "Korean" : True,
    "fav_food" : ["kimchi", "sushi"]
}

print(helen)
helen["type"] = "cute"
print(helen)