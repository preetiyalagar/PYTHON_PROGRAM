#sum of n num using for loop
n=int(input('Enter number:'))
sm=0
for x in range(1, n+1, 1):
    if x%2!=0:
        sm=sm+x
        print(x)
print('sum of n nums:',sm)