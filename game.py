number = 23
running = True
while running:
 guess = int(raw_input('enter an integer'))
 if guess == number:
   print 'congratulations, you got it'
   running = False
 elif guess < number:
   print "no, it is a little higher than that"
 else:
   print "no, it is a little lesser than that"
print "the while loop is over" 

