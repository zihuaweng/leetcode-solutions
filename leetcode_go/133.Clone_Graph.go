// https://leetcode.com/problems/clone-graph/

// Fail....

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Neighbors []*Node
 * }
 */

func cloneGraph(node *Node) *Node {
    if node == nil {
        return nil
    }
    graph := make(map[int]*Node)
    graph[node.Val] = &Node{Val: node.Val}
    queue := []*Node{node}
    
    for _, n:=range queue {
        for _, child:=range n.Neighbors {
            if _, ok := graph[child.Val]; !ok {
                graph[child.Val] = &Node{Val: child.Val}
                queue = append(queue, child)
            }
            _=append(graph[n.Val].Neighbors, graph[child.Val])
            
        }
    }
    return graph[node.Val]
}