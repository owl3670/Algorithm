package graph

import "fmt"

type Node struct {
	name   string
	weight int
}

type AdjacencyList struct {
	Graph map[string][]Node
	size  int
}

func (al *AdjacencyList) Init() {
	al.Graph = make(map[string][]Node)
}

func (al *AdjacencyList) AddNode(node string) {
	_, exists := al.Graph[node]
	if exists {
		fmt.Println("Node already exists")
		return
	}
	al.Graph[node] = make([]Node, 0)
}

func (al *AdjacencyList) AddEdge(from string, to string, weight int) {
	fromNode, existsFrom := al.Graph[from]
	_, existsTo := al.Graph[to]

	if !existsFrom || !existsTo {
		fmt.Println("Node does not exists")
	}

	for _, node := range fromNode {
		if to == node.name {
			fmt.Println("Edge already exsits")
		}
	}

	al.Graph[from] = append(fromNode, Node{to, weight})
}
