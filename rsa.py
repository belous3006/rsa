from tkinter import *


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def generate_keys(p, q):
    n = p * q
    m = (p - 1) * (q - 1)

    e = int(2)

    while e < m:
        if euclid(e, m) == 1:
            break
        else:
            e = e + 1


    w = 1
    while (((e * w) % m) != 1):
        w = w + 1

    d = w
    return [(e, n), (d, n)]


def rsa():
    global l2
    p = int(a.get())
    q = int(b.get())
    msg = int(c.get())
    pub_key, priv_key = generate_keys(p, q)

    print('Public Key: ', pub_key)
    print('Private Key: ', priv_key)

    e, n = pub_key
    d, n = priv_key

    crypted = (msg ** e) % n
    l2.config(text=crypted)
    return crypted ** d % n


def decry():
    b = rsa()
    global l3
    original = b
    l3.config(text=original)


root = Tk()

root.geometry("250x200")
root.title('RSA ')

l = Label(root, text='Первое простое число (P)')
l.pack()

a = Entry(root)
a.pack()

l = Label(root, text='Второе простое чилсо (Q)')
l.pack()

b = Entry(root)
b.pack()

l = Label(root, text='Сообщение')
l.pack()

c = Entry(root)
c.pack()

f2 = Frame()
f2.pack(side=TOP)
l2 = Label(f2, text='Зашифрованное')
l2.pack(side=LEFT)

l3 = Label(f2, text='Расшифрованое')
l3.pack(side=RIGHT)

f1 = Frame()
f1.pack(side=TOP)
button = Button(f1, text="Шифровать", command=rsa)
button.pack(side=LEFT)
button2 = Button(f1, text="Расшифровать", command=decry)
button2.pack(side=RIGHT)
root.mainloop()