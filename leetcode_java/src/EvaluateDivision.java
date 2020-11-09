// https://leetcode.com/problems/evaluate-division/

// https://leetcode.com/problems/evaluate-division/

class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = buildGraph(equations, values);
        double[] res = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            String u = queries.get(i).get(0);
            String v = queries.get(i).get(1);
            res[i] = calculate(graph, u, v, new HashSet<String>());
        }
        return res;

    }

    public double calculate(Map<String, Map<String, Double>> graph, String u, String v, Set<String> seen) {
        if (!graph.containsKey(u)) {
            return -1;
        }
        if (graph.get(u).containsKey(v)) {
            return graph.get(u).get(v);
        }
        seen.add(u);
        for (Map.Entry<String, Double> entry: graph.get(u).entrySet()) {
            if (!seen.contains(entry.getKey())) {
                double product = calculate(graph, entry.getKey(), v, seen);
                if (product != -1.0) {
                    return product * entry.getValue();
                }
            }
        }
        return -1;
    }

    public Map<String, Map<String, Double>> buildGraph(List<List<String>> equations, double[] values) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            String u = equations.get(i).get(0);
            String v = equations.get(i).get(1);
            double val = values[i];
            graph.putIfAbsent(u, new HashMap());
            graph.get(u).put(v, val);
            graph.putIfAbsent(v, new HashMap());
            graph.get(v).put(u, 1/val);
        }
        return graph;
    }
}