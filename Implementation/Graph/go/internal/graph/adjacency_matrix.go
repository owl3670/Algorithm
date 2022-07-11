package graph

import "fmt"

type AdjacencyMatrix struct {
	Graph [][]int
	Size  int
}

func (am *AdjacencyMatrix) Init(size int) {
	am.Graph = make([][]int, size)
	for i := range am.Graph {
		am.Graph[i] = make([]int, size)
	}
	am.Size = size
}

func (am *AdjacencyMatrix) AddEdge(from int, to int, weight int) {
	if from < 0 || from >= am.Size || to < 0 || to >= am.Size {
		fmt.Println("Node number is invalid")
		return
	}
	am.Graph[from][to] = weight
}
