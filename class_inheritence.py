#!/usr/bin/python

class puneeth():
      name='puneeth'
      course='aws devops'
      language='python'
      scripting='shell'
      def get_course(self):
          return self.course
      def get_name(self):
          return self.name

class ramu(puneeth):
      name='ramu'
      

obj=ramu()
print(obj.get_course())
print(obj.get_name())
print(puneeth.language)
      
