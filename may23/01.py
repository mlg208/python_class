string = input("введите сторку: ")
user_in1 = input("сколько раз повторить")
repeats = int (user_in1)
result = string * repeats
template = "Результат: %s"
message = template % result
print (message)