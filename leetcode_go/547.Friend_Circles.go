// https://leetcode.com/problems/friend-circles/

type UnionFind struct {
    parent []int
}

func NewUnionFind(m int) *UnionFind {
    uf := new(UnionFind)
    parent := make([]int, m)
    for i := range parent {
        parent[i] = i
    }
    uf.parent = parent
    return uf
}

func (uf *UnionFind) find(x int) int {
    if x != uf.parent[x] {
        uf.parent[x] = uf.find(uf.parent[x])
    }
    return uf.parent[x]
}

func (uf *UnionFind) union(x, y int) {
    p_x := uf.find(x)
    p_y := uf.find(y)
    if (p_x != p_y) {
        uf.parent[p_x] = p_y
    }
}

func findCircleNum(M [][]int) int {
    n := len(M)
    uf := NewUnionFind(n)
    
    for i:=0;i<n-1;i++ {
        for j:=i+1;j<n;j++ {
            if M[i][j] == 1 {
                uf.union(i,j)
            }
        }
    }
    
    set := make(map[int]bool)
    for i:=0;i<n;i++ {
        uf.find(i)
        set[uf.parent[i]] = true
    }
    
    return len(set)
}
