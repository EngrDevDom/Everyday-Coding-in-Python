class Dog:

      kind = 'canine'               # class variable shared by all instances

      def __init__(self, name):
            self.name = name        # instance variable unique to each instance
            self.tricks = []        # creates a new empty list for each dog

      def add_trick(self, trick):
            self.tricks.append(trick)
