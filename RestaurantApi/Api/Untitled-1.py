def show(name):
    print('hello',name)
wish = show
print(id(wish))
print(id(show))

del wish

# wish('durga')

show('neha')

def outer():
    print('outer function')
    def inner():
       print('inner function')
    print('outer function call inner')
    inner()
outer()

from random import*
for i in range(5):
    print(random())

from random import*
for i in range(5):
    print(randint(1,4))
