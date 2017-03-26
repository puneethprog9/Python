#!/usr/bin/python
import datetime
class Message_user():
       messages=[]
       user_details=[]
       unf_message = """Hi {name}! 
	Thank you for the purchase on {date} . 
	We hope you are exicted about using it. Just as a
	reminder the purcase total was ${total}.
	Have a great one!
	Team CFE
	"""
       def add_user(self,name,amount):
           detail={
	          "name":name,
                  "amount":amount
                   }
           today=datetime.date.today()
           detail['date']=today
           self.user_details.append(detail)
       def get_details(self):
           return self.user_details
       def make_message(self):
           if len(self.user_details) > 0:
              for detail in self.get_details():
               	  name=detail["name"]
               	  amount=detail["amount"]
              	  date=detail["date"]
               	  f_message=self.unf_message.format(name=name,date=date,total=amount)
                  self.messages.append(f_message)
              return self.messages
           return []

obj=Message_user()

obj.add_user('puneeth',123)
obj.add_user('madhu',235)

obj.make_message()
print(obj.messages)
