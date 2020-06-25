questions = ['What is the capital of France?',
             'Which state has only one neighbor?']
answers = ['Paris', 'Maine']

num_right = 0
for i in range(len(questions)):
      guess = input(questions[i])
      if guess.lower() == answers[i].lower():
            print('Correct!')
            num_right += 1
      else:
            print('Wrong. The answer is ', answers[i])

      print('You have ', num_right, ' out of ', i+1, 'right.')
