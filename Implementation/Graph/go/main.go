package main

import (
	"fmt"

	"algorithm.implementation.graph/internal/graph"
)

func main() {
	g1 := graph.AdjacencyList{}
	g1.Init()
	g1.AddNode("A")
	g1.AddNode("B")
	g1.AddNode("C")
	g1.AddNode("D")
	g1.AddEdge("A", "B", 1)
	g1.AddEdge("B", "A", 1)
	g1.AddEdge("A", "C", 1)
	g1.AddEdge("C", "A", 1)
	g1.AddEdge("B", "C", 1)
	g1.AddEdge("C", "B", 1)
	g1.AddEdge("B", "D", 1)
	g1.AddEdge("D", "B", 1)

	fmt.Println(g1)

	g2 := graph.AdjacencyMatrix{}
	g2.Init(6)
	g2.AddEdge(0, 2, 1)
	g2.AddEdge(2, 0, 1)
	g2.AddEdge(0, 1, 1)
	g2.AddEdge(1, 0, 1)
	g2.AddEdge(1, 4, 1)
	g2.AddEdge(4, 1, 1)
	g2.AddEdge(2, 3, 1)
	g2.AddEdge(3, 2, 1)
	g2.AddEdge(4, 5, 1)
	g2.AddEdge(5, 4, 1)

	fmt.Println(g2)

	fmt.Println(g1.BfsAL("A"))
	fmt.Println(g2.BfsAM(0))

	fmt.Println(g1.DfsAL("A"))
	fmt.Println(g2.DfsAM(0))
}
