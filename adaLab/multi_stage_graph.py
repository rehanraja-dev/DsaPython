int shortestDist(int graph[N][N]){

    int cost[N-1], d[N];

    cost[n-1] = 0

    for (int i = N-2; i>=0; i--){
        cost[i] = INF;
        for(int j = i+1; j<N; j++){
            if(graph[i][j] == INF)
            continue;
            if(cost[i]>graph[i][j]+cost[j]){
                cost[i] = graph[i][j] + cost[j];
                d[i] = j;
            }
        }
    }
    return cost[0];
}