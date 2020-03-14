#python program in Graph colouring to find the solution and assign the colours
class Graph():

        def __init__(self, vertices):
                self.v = vertices
                self.graph = [[0 for column in range(vertices)]
                for row in range(vertices)]

         #A function to check if the current colour assignment is safe for vertex v
        def isSafe(self, v, colour, c):
                for i in range(self.v):
                        if self.graph[v][i] == 1 and colour[i] == c:
                                return False
                return True

        def graphColour(self, m, colour, v):
                if v == self.v:
                        return True

                for c in range(1, m+1):
                        if self.isSafe(v, colour, c) == True:
                                colour[v] = c
                                if self.graphColour(m, colour, v+1) == True:
                                        return True
                                colour[v] = 0

        def graphColouring(self, m):
                colour = [0] * self.v
                if self.graphColour(m, colour, 0) == None:
                        return False


                print ("Solution exist and Following are the assigned colours:")
                for c in colour:
                        print (c),
                return True

g = Graph(4)
g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
m=3
g.graphColouring(m)

                       

    
        
