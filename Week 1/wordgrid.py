class WordFinder:
    grided=[]
    def set_grid(self, grid):
        for i in grid:
            self.grided.append(i)
    def count(self, word):
        lenght=len(word)
        count=0
        for i in self.grided:
            matches=0
            for j in i:
                if word[matches]==j:
                    matches+=1
                    if matches==lenght:
                        count+=1
                        matches=0
                else:
                    matches=0
        return count



grid = ["TIRATIRA",
        "IRATIRAT",
        "RATIRATI",
        "ATIRATIR"]

finder = WordFinder()
finder.set_grid(grid)

print(finder.count("TIRA")) # 7 
print(finder.count("TA")) # 13
print(finder.count("RITARI")) # 3
print(finder.count("A")) # 8
print(finder.count("AA")) # 6
print(finder.count("RAITA")) # 0   