'''
class ChineseChef:
   #these is our special chief (he can make everything the normal chief can do):
   def make_chicken(self):
      print("The Chef makes a chicken")
   def make_salad(self):
      print("the chef makes a salad")
   def makes_special_dish(self):
      print("the chef makes orange chicken")


   # but also he ca do even more than what the normal chief can):
   
   def make_fried_rice(self):
      print("the ChineseChef makes fried_rice")
'''  
   # , instead of just copying and pasting the contents from the other class,like this 👆,  
   
'''

SO, TO USE INHERITENCE(so that we can use the "chef class in this new "chinese class just by doing this")

'''

from NormalChief import normal_chief 

class ChineseChef(normal_chief):
#here we are just saying that every functions "from normal_chief" so that we can use them after imported it

#THIS IS INHERITENCE

   def makes_special_dish(self):
     print("the chef makes orange chicken")
   def make_fried_rice(self):
      print("the ChineseChef makes fried_rice")


   

  