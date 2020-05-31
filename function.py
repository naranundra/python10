def show():
    f = open('data.txt' , 'r')
    txt = f.read()
    f.close() 
    print(txt)

def showMenu():
    print('\n' '\n' '\n' 'Дүнгийн бүртгэлийн программ\n','-'*30)
    print('1. Дүнгийн мэдээлэл харах')
    print('2. Дүнгийн мэдээлэл бүртгэх')
    print('3. Дүнгийн мэдээлэл устгах')
    print('4. Дүнгийн мэдээлэл засах')
    print('5. Программаас гарах\n','-'*30)

def create():
    owog,ner,dun = input('овог, нэр, дүн: ').split()
    f = open('data.txt', 'a')
    f.write('\n' + owog + ' ' + ner + ' ' + dun)
    f.close()

def remove():
    owog, ner = input('овог, нэр: ').split()
    f = open('data.txt', 'r')
    data = f.readlines() # ['','','']
    f.close()
    for item in data:
        line = item.split() # ['baatar','bold','89\n']
        if line[0] == owog and line[1] == ner:
            data.remove(item)
    txt = ''.join(data)
    f = open('data.txt','w')
    f.write(txt)
    f.close() 

def update():
    f = open('data.txt' , 'r')
    txt = f.read()
    f.close()
    data = txt.split('\n')
    owog, ner = input('Овог, нэр: ').split()
    for item in data:
        row = item.split()
        if row[0] == owog and row[1] == ner:
            dvn = input("Засах дүнгээ оруулна уу: ")
            row[2] = dvn
            index = data.index(item)
            data[index] = ' '.join(row)

    f = open('data.txt', 'w')
    f.write('\n'.join(data))
    f.close()
    print('\n' 'Дүнгийн мэдээлэл амжилттай заслаа.\n')