### Day Two Blueprint #####################################
#
# """
# As you can see, the code is broken.
# Create the missing functions, use default arguments.
# Sometimes you have to use 'return' and sometimes you dont.
# Start by creating the functions
# """
#
# # \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#
# print("Is Wed on 'days' list?", is_on_list(days, "Wed"))
#
# print("The fourth item in 'days' is:", get_x(days, 3))
#
# add_x(days, "Sat")
# print(days)
#
# remove_x(days, "Mon")
# print(days)
#
#
# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #

"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(days,day):
  day in days
  return True
print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

def get_x(days, day):
    return days[day]
print("The fourth item in 'days' is:", get_x(days, 3))

def add_x(days, day):
    return days.append(day)
add_x(days, "Sat")
print(days)

def remove_x(days, day):
    return days.remove(day)
remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #


###############################################
# ## 정답
###############################################
#
# def is_on_list(a_list=[], word=""):
#   return word in a_list
#
# def get_x(a_list=[], index=0):
#   return a_list[index]
#
# def add_x(a_list=[], word=""):
#   a_list.append(word)
#
# def remove_x(a_list=[], word=""):
#   a_list.remove(word)
#
# # \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #
#
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#
# print("Is Wed on 'days' list?", is_on_list(days, "Wed"))
#
# print("The fourth item in 'days' is:", get_x(days, 3))
#
# add_x(days, "Sat")
# print(days)
#
# remove_x(days, "Mon")
# print(days)
#
#
# # /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #
#




