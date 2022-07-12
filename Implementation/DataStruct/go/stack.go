package datastruct

type Stack []interface{}

func (s *Stack) Push(data interface{}) {
	*s = append(*s, data)
}

func (s *Stack) Pop() interface{} {
	if s.GetLength() == 0 {
		return nil
	}
	top := s.GetLength() - 1
	data := (*s)[top]
	*s = (*s)[:top]
	return data
}

func (s *Stack) GetLength() int {
	return len(*s)
}
