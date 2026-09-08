class Tree:
    def __init__(self, TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName #STRING
        self.__HeightGrowth = HeightGrowth #INTEGER
        self.__MaxHeight = MaxHeight #INTEGER
        self.__MaxWidth = MaxWidth #INTEGER
        self.__Evergreen = Evergreen #STRING

    def GetTreeName(self):
        return self.__TreeName

    def GetHeightGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen

def ReadData():
    TreeArray = []
    try:
        file = open("Trees.txt", "r")
        for line in file:
            line = line.strip().split(",")
            TreeObject = Tree(line[0], line[1], line[2], line[3], line[4])
            TreeArray.append(TreeObject)
        file.close()
        return TreeArray
    except FileNotFoundError:
        print("File not found.")


def PrintTrees(treeobj):
    if treeobj.GetEvergreen().lower() == "yes":
        print(f"{treeobj.name} has a maximum height {treeobj.max_height} a maximum width {treeobj.max_width} and grows {treeobj.growth} cm a year. It does not lose its leaves.")
    else:
        print(f"{treeobj.name} has a maximum height {treeobj.max_height} a maximum width {treeobj.max_width} and grows {treeobj.growth} cm a year. It loses its leaves each year.")

def Main():
    tree = ReadData()
    PrintTrees(tree)
Main()