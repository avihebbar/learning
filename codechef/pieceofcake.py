test_cases = int( raw_input() )

while test_cases > 0:
  test = raw_input()
  frequency = [0] * 26
  for char in test:
   frequency[ ord(char) - 97 ] += 1

  if 2 * max(frequency) == len(test):
    print "YES"
  else:
    print "NO"

  test_cases -= 1

