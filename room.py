from row import Row;

class Room():
    name = ""
    rows = dict()
    
    def __init__(self, name=""):
        self.name = name
    
    def getName(self):
        return self.name
    
    def addRow(self, row):
        self.rows[row.getName()] = row
        
    def removeRow(self, rowName):
        if (rowName in rows):
            del rows[rowName]
            
    def getRow(self, rowName):
        if (rowName in self.rows):
            return self.rows[rowName]
        else:
            row = Row(rowName)
            self.rows[rowName] = row
            return row
    
    def __str__(self):
        return list(self.rows.keys()).__str__() 