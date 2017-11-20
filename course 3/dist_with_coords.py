""" 
bidirectional_a_star: bidirectional A* search 

g: input graph (networkx object)
s, t: source and destination nodes
pi_forward, pi_backward: forward and backward potential function values
wt_attr: attribute name to be used as edge weight 
"""

def bidirectional_a_star(g,s,t,pi_forward, pi_backward, wt_attr='weight' ):
    # initialization
    gRev = g.reverse() # reverse graph
    ds =   { v:float('inf') for v in g } # best distances from s or t
    dt = ds.copy()
    ds[s]=0
    dt[t]=0
    parents = {} # predecessors in forward/backward search
    parentt = {}
    pqueues =[(ds[s]+pi_forward[s],s)]  # priority queues for forward/backward search
    pqueuet = [(dt[t]+pi_backward[t],t)]

    mu = float('inf') # best s-t distance

    scanned_forward=set() # set of scanned vertices in forward/backward search
    scanned_backward=set()

    while (len(pqueues)>0 and len(pqueuet)>0):
        # forward search
        (priority_s,vs) = heappop(pqueues) # vs: first node in forward queue

        if (priority_s >= mu): # stop condition
            break

        for w in g.neighbors(vs): # scan outgoing edges from vs
            newDist = ds[vs] + g.edge[vs][w][wt_attr]

            if (ds[w] > newDist and w not in scanned_backward):
                ds[w] = newDist  # update w's label
                parents[w] = vs
                heappush(pqueues, (ds[w]+pi_forward[w] , w) )

            if ( (w in scanned_backward) and  (newDist + dt[w]<mu)):
                 mu = newDist+dt[w]

        scanned_forward.add(vs)  # mark vs as "scanned"

        # backward search
        (priority_t,vt) = heappop(pqueuet) # vt: first node in backward queue

        if (priority_t>= mu ):
            break

        for w in gRev.neighbors(vt):
            newDist = dt[vt] + gRev.edge[vt][w][wt_attr]

            if (dt[w] >= newDist and w not in scanned_forward):
                if (dt[w] ==newDist and parentt[vt] < w):
                    continue
                else:
                    dt[w] = newDist
                    parentt[w] = vt
                    heappush(pqueuet,(dt[w]+pi_backward[w],w))
            if ( w in scanned_forward and  newDist + ds[w]<= mu):
                 mu = newDist+dt[w]

        scanned_backward.add(vt)

    # compute s-t distance and shortest path
    scanned = scanned_s.intersection(scanned_t)
    minPathLen = min( [ ds[v]+dt[v] for v in scanned ] ) # find s-t distance
    minPath = reconstructPath(ds,dt,parents,parentt,scanned) # join s-v and v-t path

    return (minPathLen, minPath)