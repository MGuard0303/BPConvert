class Region():
    def __init__(self, value: tuple) -> None:
        self.value = value
        self.order = 0


class BPConvert():
    def __init__(self) -> None:
        self.id = ""
        self.sequence = ""
        self.regions = []


    def parse(self, file: str, format: str = "bpseq") -> None:
        with open(file, "r") as f:
            for line in f:
                if line.startswith(r"#"):
                    self.id = line[1:-1]
                else:
                    line = line.strip().split()
                    self.sequence += line[1]

                    # Record base pair as a tuple starting with a smaller number
                    if int(line[0]) < int(line[2]):
                        self.regions.append(Region((int(line[0]), int(line[2]))))


    def convert(self) -> tuple:
        ORD = (("(", ")"), ("[", "]"), ("{", "}"), ("<", ">"))
        
        regions_number = len(self.regions)

        self.__set_region_order(self.regions, regions_number)
        
        db_l = ["."] * len(self.sequence)
        
        for region in self.regions:
            for i in range(4):
                if region.order == i:
                    db_l[region.value[0]-1] = ORD[i][0]
                    db_l[region.value[1]-1] = ORD[i][1]

        db = ""
        for i in db_l:
            db += i

        return (self.id, db)
    

    def __conflicted(self, region1: tuple, region2: tuple) -> bool:
        if region1 == region2:
            return False
        
        if region1[0] < region2[0]:
            outer = region1
            inner = region2
        elif region1[0] > region2[0]:
            outer = region2
            inner = region1

        if inner[0] < outer[1]:
            if inner[1] > outer[1]:
                return True
            if inner[1] < outer[1]:
                return False
            
        if inner[0] > outer[1]:
            return False
        

    def __set_region_order(self, regions: list, number: int) -> None:
        regions[0].order == 0

        for i in range(1, number):
            regions[i].order == 0
            ord_0 = [regions[0].value]
            ord_1, ord_2 = [], []
            
            for j in range(0, i):
                if regions[j].order == 0:
                    ord_0.append(regions[j].value)
                elif regions[j].order == 1:
                    ord_1.append(regions[j].value)
                elif regions[j].order == 2:
                    ord_2.append(regions[j].value)

            for r in ord_0:
                if self.__conflicted(regions[i].value, r):
                    regions[i].order += 1
                    break
            
            if regions[i].order == 1:
                for r in ord_1:
                    if self.__conflicted(regions[i].value, r):
                        regions[i].order += 1
                        break

            if regions[i].order == 2:
                for r in ord_2:
                    if self.__conflicted(regions[i].value, r):
                        regions[i].order += 1
                        break