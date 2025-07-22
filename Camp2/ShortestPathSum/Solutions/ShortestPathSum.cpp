
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int main() {
    int n, m, start_node;
    cin >> n >> m >> start_node;

    vector<int> node_values(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> node_values[i];
    }

    vector<vector<pair<int, int>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    vector<int> dist(n + 1, INT_MAX);
    dist[start_node] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start_node});

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (d > dist[u]) continue;

        for (auto& edge : adj[u]) {
            int v = edge.first;
            int weight = edge.second;

            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    int min_dist = INT_MAX;
    int end_node = -1;
    for (int i = 1; i <= n; ++i) {
        if (dist[i] != INT_MAX && dist[i] < min_dist) {
            min_dist = dist[i];
            end_node = i;
        }
    }

    int sum = 0;
    for (int i = 1; i <= n; ++i) {
      if (dist[i] != INT_MAX)
        sum += node_values[i];
    }

    cout << sum << endl;

    return 0;
}