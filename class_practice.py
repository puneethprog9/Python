#!/usr/bin/python


tools=['chef','jenkings','docker']

class puneeth():
      name='puneeth'
      course='aws devops'
      language='python'
      scripting='shell'
      def get_course(self,lists):
          return self.course,lists[0]
      def get_name(self):
          return self.name

class ramu(puneeth):
      name='ramu'
      

obj=ramu()
print(obj.get_course(tools))
print(obj.get_name())
print(puneeth.language)
      
