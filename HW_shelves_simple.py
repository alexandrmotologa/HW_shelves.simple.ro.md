class Cabinet():
    # properties
    top = None
    middle = None
    bottom = None
    
    def putOn(self, shelfName, thing):
        self.shelfName = shelfName
        if thing != None:
            if shelfName == "top":
                if self.top == None:
                    self.top = shelfName
                    self.thing = thing
                    self.thing_top = thing
                    print('add' , thing)
                else:
                    print(f"Cannot place {self.thing_top} on top shelf, it is not empty!")
            
            if shelfName == "middle":
                if self.middle == None:
                    self.middle = shelfName
                    self.thing = thing
                    self.thing_middle = self.thing
                    print('add' , thing)
                else:
                    print(f"Cannot place {self.thing_middle} on middle shelf, it is not empty!")
            
            if shelfName == "bottom":
                if self.bottom == None:
                    self.bottom = shelfName
                    self.thing = thing
                    self.thing_bottom = self.thing
                    print('add' , thing)
                else:
                    print(f"Cannot place {self.thing_bottom} on bottom shelf, it is not empty!")
    
    
    def takeFrom(self, shelfName):
        try:
            if shelfName == "top":
                del self.top
                print("delete thing from top")
            elif shelfName == "middle":
                del self.middle
                print("delete thing from top")
            elif shelfName == "bottom":
                del self.bottom
                return self.bottom
        except AttributeError:
            print("Nothing to take! The top shelf is empty")

    def printSchema(self):
        rows = 0
        size = 32
        while rows <=6:
            rows += 1
            if rows == 2:
                x = round((size - len(self.thing_top)-2) / 2)
                a = x * " "
                if x%2 == 1:
                    a + "  "
                print(f"#{a}{self.thing_top}{a}#")
            if rows == 4:
                x = round((size - len(self.thing_middle)-2) / 2)
                a = x * " "
                if x%2 == 1:
                    a + "  "
                print(f"#{a}{self.thing_middle}{a}#")
            if rows == 6:
                x = round((size - len(self.thing_bottom)-2) / 2)
                a = x * " "
                if x%2 == 1:
                    a + "  "
                print(f"#{a}{self.thing_bottom}{a}#")
            if rows%2==1:
                print("#"*size)






a1 = Cabinet()
a1.putOn("top", "a book")
a1.putOn("middle", "flashlight")
a1.putOn("bottom", "laptop")
a1.takeFrom("top")
a1.takeFrom("top")
a1.putOn("top", "a book")
a1.putOn("top", "a book")
a1.takeFrom("top")
a1.putOn("top", "a book")
a1.putOn("top", "a book")
a1.printSchema()
