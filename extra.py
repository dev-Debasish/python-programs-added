



# apple = 100
# x = int("apple") - 10
# print(x)


# fruit = "banana"

# for index, i in enumerate(fruit):
#     print(index, i)




def StringChallenge(strParam):
  str = []
  for char in strParam:
    str.append(char)
  str = list(dict.fromkeys(str))
  if (len(str) == 10):
      return True
  else:
    return False  
      
  # code goes here
#   return strParam

# keep this function call here 
print(StringChallenge(input()))


# 12334bbmma:=6




