def centrality_calculater(G):
    deg = nx.degree_centrality(G)
    close = nx.closeness_centrality(G)
    eig = nx.eigenvector_centrality(G)
    bet = nx.betweenness_centrality(G)
    sub = nx.subgraph_centrality(G)
    info = nx.information_centrality(G)

    names = list(deg.keys())
    degree_list = np.array(list(deg.values()))
    closeness_list = np.array(list(close.values()))
    eigenvector_list = np.array(list(eig.values()))
    betweenness_list = np.array(list(bet.values()))
    subgraph_list = np.array(list(sub.values()))
    information_list = np.array(list(info.values()))

    centrality_df = pd.DataFrame()
    centrality_df['Names'] = names
    centrality_df['Degree'] = degree_list
    centrality_df['Closeness'] = closeness_list
    centrality_df['Eigenvector'] = eigenvector_list
    centrality_df['Betweenness'] = betweenness_list
    centrality_df['Subgraph'] = subgraph_list
    centrality_df['Information'] = information_list




    colnames = list(centrality_df.columns)
    transformed = pd.DataFrame()
    for col in colnames:
        arr = np.array(centrality_df[col])
        if col == "Betweenness":
            arr += 1e-10
            arr = np.log(arr)
        elif col != "Closeness" and col != "Information" and col!= "Names":
            arr += 1e-20
            arr = np.log(arr)

        transformed[col] = arr


    importance = []
    for i in range(len(list(transformed["Names"]))):
        importance_score = 0.21*transformed["Degree"][i] + 0.21*transformed["Closeness"][i] + 0.2*transformed["Eigenvector"][i] + 0.16*transformed["Betweenness"][i] + 0.22*transformed["Information"][i]

        importance.append(importance_score)

    transformed["Importance"] = importance

    importance_dict = {}
    for i in range(len(importance)):
        importance_dict[transformed["Names"][i]] = transformed["Importance"][i]

    sorted_importance  = sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_importance

