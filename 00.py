class Box: #클래스 생성
    def __init__(self,size,color):
        self.size=size
        self.color=color

    def showBox(self):
        print("박스 사이즈는"+self.size+"이고"+self.color+"이다")

myB=Box("small","blue")
print(myB.size)
print(myB.color)
myB.showBox()