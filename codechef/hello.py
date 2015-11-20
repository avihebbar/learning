

test_cases = int( raw_input() )

while test_cases > 0:
  both = 0
  neither = 0
  input = map(int, raw_input().split(' '))
  parent_array = [-2] * input[0]
  ign = map(int, raw_input().split(' '))
  for entry in ign:
    parent_array[entry - 1] += 1
  tra = map(int, raw_input().split(' '))
  for entry in tra:
    parent_array[entry - 1] += 1
  for entry in parent_array:
    if entry == 0:
      both += 1
    elif entry == -2:
      neither += 1

  test_cases -= 1
  print both,neither

  




# print [-2]* 5 
