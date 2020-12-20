// https://leetcode.com/problems/course-schedule-ii/

func findOrder(n int, prerequisites [][]int) []int {
    indegree := make([]int, n)
    next := make([][]int, n)
    res := make([]int, 0, n)
    
    for _, v := range prerequisites {
        indegree[v[0]]++
        next[v[1]] = append(next[v[1]], v[0])
    }
    
    for i, v := range indegree {
        if v == 0 {
            res = append(res, i)
        }
    }
		
		
		// same as python: iterate array to work as queue
    for i:=0; i<len(res);i++{
        cur := res[i]
        cls := next[cur]
        for _, v := range cls {
            indegree[v]--
            if indegree[v] == 0 {
                res = append(res, v)
            }
        }
    }
    
    if len(res) == n {
        return res
    }
    
    return []int{}
}