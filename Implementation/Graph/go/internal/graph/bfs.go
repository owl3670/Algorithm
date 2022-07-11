package graph

import (
	"fmt"

	"algorithm.implementation.datastruct/queue"
)

func (g AdjacencyList) BfsAL(start string) []string {
	visited := make([]string, 0)
	q := queue.Queue{}
	q.Enqueue(start)
	for q.GetLength() != 0 {
		node := fmt.Sprintf("%v", q.Dequeue())
		var exist bool
		for _, val := range visited {
			exist = val == node || exist
		}

		if exist {
			continue
		}

		visited = append(visited, node)
		for _, val := range g.Graph[node] {
			q.Enqueue(val.name)
		}
	}

	return visited
}
