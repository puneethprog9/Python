#!/usr/bin/python

class Animal():
      name='jeo'
      color='dark'
      @property
      def get_color(self):
          return self.color



dog=Animal()
print(dog.get_color)
