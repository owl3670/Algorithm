package main

import "fmt"

type Node struct {
	name   string
	weight int
}

type AdjacencyList struct {
	graph map[string][]Node
	size  int
}

func (al *AdjacencyList) Init() {
	al.graph = make(map[string][]Node)
}

func (al *AdjacencyList) AddNode(node string) {
	_, exists := al.graph[node]
	if exists {
		fmt.Println("Node already exists")
		return
	}
	al.graph[node] = make([]Node, 0)
}

func (al *AdjacencyList) AddEdge(from string, to string, weight int) {
	fromNode, existsFrom := al.graph[from]
	_, existsTo := al.graph[to]

	if !existsFrom || !existsTo {
		fmt.Println("Node does not exists")
	}

	for _, node := range fromNode {
		if to == node.name {
			fmt.Println("Edge already exsits")
		}
	}

	al.graph[from] = append(fromNode, Node{to, weight})
}

func main() {
	g := AdjacencyList{}
	g.Init()
	g.AddNode("A")
	g.AddNode("B")
	g.AddNode("C")
	g.AddNode("D")
	g.AddEdge("A", "B", 1)
	g.AddEdge("B", "A", 1)
	g.AddEdge("A", "C", 1)
	g.AddEdge("C", "A", 1)
	g.AddEdge("B", "C", 1)
	g.AddEdge("C", "B", 1)
	g.AddEdge("B", "D", 1)
	g.AddEdge("D", "B", 1)

	for _, node := range g.graph {
		fmt.Println(node)
	}
}
