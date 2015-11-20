async = require 'async'

numbers = [2..20]

mul_factors = [1..20]

primes = []


multiple = (input, factor)->
  return input.map((input)->
    return input * factor)

deleteNumber = (number)->
  index = numbers.indexOf(number)
  numbers.splice(index, 1)if index isnt -1

while numbers.length isnt 0
  num = numbers[0]
  primes.push(num)
  for n in multiple(mul_factors, num) 
    deleteNumber(n)

console.log primes
