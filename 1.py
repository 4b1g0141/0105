class Book:
     #書本類別的建構子
    def __init__(self, id, name, author):
        self._id = id
        #目前的self._編號 = 編號
        self._name = name
        #目前的self._名稱 = 名稱
        self._author = author
        #目前的self._作者 = 作者
 
s1 = Book('001', '好看的書', '小明')
print("書本編號=",s1._id)
print("書本名稱=",s1._name)
print("書本作者=",s1._author)

s2 = Book('002', '難看的書', '小王')
print("書本編號=",s2._id)
print("書本名稱=",s2._name)
print("書本作者=",s2._author)
