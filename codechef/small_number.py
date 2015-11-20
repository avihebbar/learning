test_cases = int( raw_input() )  

while test_cases != 0:
  num =  int (raw_input() )
  
  nodes = [100, 50, 10, 5, 2, 1]
  index = 0
  count = 0

  while num != 0:
    quo  = num / nodes[index]
    if quo >= 1:
      num = num % nodes[index]
      count += quo
    index += 1

  test_cases -= 1
  print count

