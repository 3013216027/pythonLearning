g = (x * x for x in range(10))
for n in g:
    print(n)

def triangles():
    L1 = [1]
    yield L1
    for d in range(0, 16):
        L2 = [1]
        for d in range(0, len(L1) - 1):
            L2.append(L1[d] + L1[d + 1])
        L2.append(1)
        L1 = L2
        yield L2
    return 'done'

#try:
for x in triangles():
    print(x)
print(triangles())
#except StopIteration as e:
 #   print('Generator returns', e.value)
  #  break

