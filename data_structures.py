from shapely import geometry
class Edge:
    def __init__(self, id: int, stepLow: int, stepHigh: int, startNode: int, endNode: int, geom: geometry.LineString,
    rightFaceLow: int = None, leftFaceLow: int = None, rightFaceHigh: int = None,  leftFaceHigh: int = None, edgeClass: str = None) -> None:
        #TODO: Too many arguments in the constructor, should change this for an input lost/dict of some sorts
        self.id = id
        self.stepLow = stepLow
        self.stepHigh = stepHigh
        self.startNode = startNode
        self.endNode = endNode
        self.geom = geom
        #TODO Add nullable parameters (not yet used!)

    def __str__(self):
        printStr: str = f'Edge with ID: {self.id}, step low: {self.stepLow}, step ligh: {self.stepHigh}, start node: {self.startNode}, end node: {self.endNode}, geometry: {self.geom}'
        return printStr

    def countNodes(self):
        print(len(self.geom))
        