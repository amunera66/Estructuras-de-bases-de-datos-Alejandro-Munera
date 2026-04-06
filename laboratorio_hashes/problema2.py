import hashlib
import itertools

##input
root = "58c89d709329eb37285837b042ab6ff72c7c8f74de0446b091b6a0131c102cfd"

t = ["a","b","c","d"]

def h(x):
    return hashlib.sha256(x).hexdigest()

def merkle(xs):
    xs = [h(x.encode()) for x in xs]
    while len(xs) > 1:
        xs = [h((xs[i]+xs[i+1]).encode()) if i+1 < len(xs) else xs[i]
              for i in range(0, len(xs), 2)]
    return xs[0]

for p in itertools.permutations(t):
    if merkle(p) == root:
        print("Orden encontrado:", p)
        break
else:
    print("No existe orden con este modelo")
