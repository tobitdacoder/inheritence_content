from NormalChief import normal_chief #here we have imported the class "normal_chief" from a file called "NormalChief"
from ChineseChef import ChineseChef #here its the same process as the previous one


myChief = normal_chief()#this is the object we created.. here the "normal_chief()" is the class we created before
myChief.makes_special_dish() #here we are printing that object with a specific task... we are using the object name
# "myChief" and the specific function in that class (sot that we can access the content of that function inside that class)

myChianeseChief = ChineseChef()
#myChianeseChief.make_chicken()
myChianeseChief.makes_special_dish()

#here we can see that, after we used the inheritence, we are now able to print a function which is not in the "ChineseChef()" by taking it from the "ormal_chief"