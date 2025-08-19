fn = open('white.txt', 'r')
fn1 = open('black.txt', 'w')

cont = fn.readlines()
type(cont)
for i in range (1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass


fn1.close()

fn1 = open('black.txt', 'r')
new = fn1.read()
print(new)

fn.close()
fn1.close()