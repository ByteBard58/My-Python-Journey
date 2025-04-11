
marks=float(input('Provide your mark'))

if marks>=80 and marks <=100:
  print('You have got A+')
elif marks>=70 and marks <=79:
  print('You have got A')
elif marks>=60 and marks <=69:
  print('You have got A-')
elif marks>=50 and marks <=59:
  print('You have got B')
elif marks>=40 and marks <=49:
  print('You have got C')
elif marks>=0 and marks <40:
  print('You have got F')
else:
  print('Enter a valid mark')