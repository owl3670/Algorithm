package main

import "fmt"

type AdjacencyMatrix struct {
	graph [][]int
	size  int
}

func (am *AdjacencyMatrix) init(size int) {
	am.graph = make([][]int, size)
	for i := range am.graph {
		am.graph[i] = make([]int, size)
	}
	am.size = size
}

func (am *AdjacencyMatrix) addEdge(from int, to int, weight int) {
	if from < 0 || from >= am.size || to < 0 || to >= am.size {
		fmt.Println("Node number is invalid")
		return
	}
	am.graph[from][to] = weight
}

func main() {
	g := AdjacencyMatrix{}
	g.init(6)
	g.addEdge(0, 2, 1)
	g.addEdge(2, 0, 1)
	g.addEdge(0, 1, 1)
	g.addEdge(1, 0, 1)
	g.addEdge(1, 4, 1)
	g.addEdge(4, 1, 1)
	g.addEdge(2, 3, 1)
	g.addEdge(3, 2, 1)
	g.addEdge(4, 5, 1)
	g.addEdge(5, 4, 1)

	for _, node := range g.graph {
		fmt.Println(node)
	}
}
