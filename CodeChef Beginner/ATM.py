(X, Y) = (input().split())
Y = float(Y)
nY = Y - 0.5
X = int(X)
if X % 5 == 0 and X <= nY:
    print(nY - X)
else:
    print(Y)