import time

while True:
   timer = input('please input how many seconds you want the timer to last, or say stop to stop: ')

   if timer == 'stop':
      break
   
   input('Press Enter to start the countdown.')
   print('Countdown started.')
   timer = int(timer)
   for i in range(timer):
      print(timer-i)
      time.sleep(1)
      
   print('Time is up')
   time.sleep(1)
