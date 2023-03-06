class person01:
    def code(self,idea):
        idea.execute()
        
class person02:
    def execute(self): 
        print("Practice make everything perfect")

idea = person02() #// create person02 object

quote = person01()#// person01 object

quote.code(idea)#// calling the function by giving idea object as the argument.