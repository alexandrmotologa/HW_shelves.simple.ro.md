class Cabinet():
    # properties
    top = None
    middle = None
    bottom = None
    
    thing_top = None
    thing_middle = None
    thing_bottom = None
    
    def putOn(self, shelfName, thing):
        self.shelfName = shelfName
        if shelfName == "top":
            if self.top == None:
                self.top = shelfName
                if thing != None:
                    self.thing = thing
                    self.thing_top = self.thing
            else:
                print("Cannot place \"Flash light\" on top shelf, it is not empty! top")
        
        if shelfName == "middle":
            if self.middle == None:
                self.middle = shelfName
                if thing != None:
                    self.thing = thing
                    self.thing_middle = self.thing
            else:
                print("Cannot place \"Flash light\" on top shelf, it is not empty! middle")
        
        if shelfName == "bottom":
            if self.bottom == None:
                self.bottom = shelfName
                if thing != None:
                    self.thing = thing
                    self.thing_bottom = self.thing
            else:
                print("Cannot place \"Flash light\" on top shelf, it is not empty! bottom")
    
    
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
        print(f"#{self.thing_top}#" )

        print(f"#{self.thing_middle}#" )

        print(f"#{self.thing_bottom}#" )










a1 = Cabinet()
a1.putOn("top", "a book")
a1.putOn("middle", "flashlight")
a1.putOn("bottom", "laptop")
a1.printSchema()
a1.takeFrom("top")
a1.takeFrom("top")
a1.putOn("top", "a book")
a1.putOn("top", "a book2")
a1.takeFrom("top")
a1.putOn("top", "a book2")
a1.putOn("top", "a book2")
