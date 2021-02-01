# Operators - Arithmetic and Assignment
x_position = 10
x_position = x_position + 1
print(x_position)


remainder = 5 % 2
print(remainder)
floor_division = 5 // 2
print(floor_division)

five_squared = 5 ** 2
print(five_squared)

first_name = "Jakob"
last_name = "Kobberholm"
print("{} {}".format(first_name, last_name))

# Operators - Conditional and Logical
# > >= < <= == != not or and

x_position = 1
end_position = 10

is_at_end = x_position == end_position
print(is_at_end)
is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

print(not is_at_end)

score = 10
is_game_over = score > 10 and is_at_end
print(is_game_over)

print("\n---------\na/b Testing")
print("a" < "b")
print("a" <= "b")
print("a" == "b")
print("a" != "b")
print("a" >= "b")
print("a" > "b")

print("\n---------\na only")
print("a" < "a")
print("a" <= "a")
print("a" == "a")
print("a" != "a")
print("a" >= "a")
print("a" > "a")

print ("\n---------\na/aa")
print("a" < "aa")
print("a" <= "aa")
print("a" == "aa")
print("a" != "aa")
print("a" >= "aa")
print("a" > "aa")

print ("\n---------\naa/bb")
print("aa" < "bb")
print("aa" <= "bb")
print("aa" == "bb")
print("aa" != "bb")
print("aa" >= "bb")
print("aa" > "bb")