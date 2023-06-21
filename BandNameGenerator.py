"""from dynarray import DynamicArray
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
array = DynamicArray()
for i in range(len(two_digit_number)):
    print(two_digit_number[i])

from dynarray import DynamicArray
two_digit_number = input("Type a two digit number: ")

array = DynamicArray()
sum = 0
for i in range(len(two_digit_number)):
    array.append(two_digit_number[i])

for i in range(array):
    int(array[i])+=sum"""

# 🚨 Don't change the code below 👇

class Methods:    
    def check_last_occurrence(self,array):
        lenght_array = 1
        string = ""
        sum = 0
        for i in range(len(array)):
            sum+=int(array[i])

            if (((lenght_array) != len(array))):

                string += str(array[i]) + " + "
                lenght_array+=1
            else:
                string += str(array[i]) + " = " + str(sum)
                print(string)
         

class Main:
    two_digit_number = input("Type a number: ")

    array = list(map(int, two_digit_number))
    my_object = Methods().check_last_occurrence(array)

