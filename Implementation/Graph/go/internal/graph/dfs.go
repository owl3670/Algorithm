package graph

import (
	"fmt"

	"algorithm.implementation/datastruct"
)

func (g AdjacencyList) DfsAL(start string) []string {
	visited := make([]string, 0)
	s := datastruct.Stack{}
	s.Push(start)
	for s.GetLength() != 0 {
		node := fmt.Sprintf("%v", s.Pop())
		var exist bool
		for _, val := range visited {
			exist = val == node || exist
		}

		if exist {
			continue
		}

		visited = append(visited, node)
		for _, val := range g.Graph[node] {
			s.Push(val.name)
		}
	}

	return visited
}

func (g AdjacencyMatrix) DfsAM(start int) []int {
	visited := make([]int, 0)
	s := datastruct.Stack{}
	s.Push(start)
	for s.GetLength() != 0 {
		node := s.Pop().(int)
		var exist bool
		for _, val := range visited {
			exist = val == node || exist
		}

		if exist {
			continue
		}

		visited = append(visited, node)
		for idx, val := range g.Graph[node] {
			if val == 0 {
				continue
			}
			s.Push(idx)
		}
	}

	return visited
}
