inputLines = 0
N = K =0

process.stdin.on('data', (data)->
  num = data.toString().split(" ")
  if inputLines is 0
    inputLines++
    N = Number(num[0])
    K = Number(num[1])
  else
    a = []
    for i in [0..N-1]
      a.push( Number(num[i]) )
    pr = computeWay(N, K, a)
    console.log pr
    process.exit(0)
)


computeWay = (N, K, a)->
  rem = (N - 1) % K
  quo = parseInt( (N - 1) / K )

  product = 1
  factor = 0

  product *= a[rem]

  while factor < quo
    rem = rem + K
    product *= a[rem]
    product %= 1000000007
    factor++   
  return product
