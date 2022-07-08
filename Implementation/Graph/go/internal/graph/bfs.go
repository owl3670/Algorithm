package graph

import (
	"algorithm.implementation.datastruct/queue"
)

func BfsAL(g AdjacencyList, start string) []string {
	visited := make([]string, g.Size)
	q := queue.Queue{}
	q.Enqueue(start)
	visited = append(visited, start)

	return visited
}
