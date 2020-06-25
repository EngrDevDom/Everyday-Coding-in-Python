"An example module"

PI = 3.1416

def sum(lst):
      tot = 0
      for value in lst:
            tot = tot + value
      return tot

def add(x, y):
      a = x + y
      return a

def test():
      l = [0, 1, 2, 3]
      assert(sum(l) == 6)
      print('test passed!')

if __name__ == '__main__':
      test()
