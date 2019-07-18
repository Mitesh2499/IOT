try:
    cities,edges=map(int,input().split())
    d={}
    for _ in range(edges):
        start,end,price=map(int,input().split())
        d1={end:price}
        if start in d.keys():
            d[start].update(d1)
        else:
            d.update({start:d1 })

    total_cost=0
    s,e=1,cities
    while s!=e:
        next_node=d[s]
        next_city=list(next_node.keys())
        l=len(next_city)
        if l>1:
            for i in range(l-1):
                if next_node[next_city[i]]<next_node[next_city[i+1]]:
                    total_cost+=next_node[next_city[i]]
                    #print(total_cost)
        else:
            total_cost+=next_node[next_city[0]]
            #print(total_cost)
            

        s=next_city[i]
      

    print(total_cost)

except:
    pass
        

