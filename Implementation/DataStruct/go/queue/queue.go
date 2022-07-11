package queue

type Queue []interface{}

func (q *Queue) Enqueue(data interface{}) {
	*q = append(*q, data)
}

func (q *Queue) Dequeue() interface{} {
	if len(*q) == 0 {
		return nil
	}
	data := (*q)[0]
	*q = (*q)[1:]
	return data
}

func (q *Queue) GetLength() int {
	return len(*q)
}
