def multiply(start,end):
  if start==end:
    return start
  return start * multiply(start+1,end)
start=int(input('enter  the start:'))
end=int(input('enter the end:'))

if start > end:
  print('the start should be less than the end number:')
result=multiply(start,end)
print(f'{start} and {end} is : {result}')
