package graph

import "fmt"

type AdjacencyMatrix struct {
	Graph [][]int
	size  int
}

func (am *AdjacencyMatrix) Init(size int) {
	am.Graph = make([][]int, size)
	for i := range am.Graph {
		am.Graph[i] = make([]int, size)
	}
	am.size = size
}

func (am *AdjacencyMatrix) AddEdge(from int, to int, weight int) {
	if from < 0 || from >= am.size || to < 0 || to >= am.size {
		fmt.Println("Node number is invalid")
		return
	}
	am.Graph[from][to] = weight
}
