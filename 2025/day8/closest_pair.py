from functools import reduce
import math

"""
FROM PDSA: Divide and Conquer https://pdsaiitm.github.io/
def ClosestPair(Px,Py):
    if len(Px) <= 3:
        compute pairwise distances
        return closest pair and distance
    Construct (Qx,Qy), (Rx,Ry)
    (q1,q2,dQ) = ClosestPair(Qx,Qy)
    (r1,r2,dR) = ClosestPair(Rx,Ry)
    Construct Sy from Qy,Ry
    Scan Sy, find (s1,s2,dS)
    return (q1,q2,dQ), (r1,r2,QR), (s1,s2,dS)
    #depending on which of dQ, dR, dS is minimum

I will combine it with union find to combine minimum pairs  
"""


already_found = set()

def _sort_vertices(vertices, dim=3):
    return [sorted(vertices, key=lambda v: v[i]) for i in range(dim)]

def find_closest_pair(vertices, dim):
    p_sorted = _sort_vertices(vertices, dim)
    dmin, v1, v2 =  _r_find_closest_pair(p_sorted)
    already_found.add((v1, v2))
    return v1, v2


def _r_find_closest_pair(p_sorted):  # O(nlogn)
    px = p_sorted[0]
    if len(px)  <= 3:
        return pairwise_distance_min(px)

    q_sorted, r_sorted = _partition_about_xmid(p_sorted)

    q_mint = _r_find_closest_pair(q_sorted) # Minimum distance in q => tuple => q min tuple
    r_mint = _r_find_closest_pair(r_sorted)

    mint = min(q_mint, r_mint)
    delta = mint[0]
    xr = r_sorted[0][0][0]

    s_mint = _find_min_about_delta(delta, xr, p_sorted)

    return min (mint, s_mint)

def _find_min_about_delta(delta, xr, p_sorted):  # O(n)
    s_sorted = []

    for v in p_sorted[1]: # Check about  y
        if abs(v[0] - xr) <= delta:
            s_sorted.append(v)

    mind = math.inf
    minv1, minv2 = (None, None)
    for i in range(len(s_sorted)):
        for j in range(i+1, min(i + 16, len(s_sorted))):
            assert j < len(s_sorted)
            v1, v2 = s_sorted[i], s_sorted[j]
            # if unionfind.find(v1) == unionfind.find(v2): continue
            if (v1, v2) in already_found: continue
            d = distance(v1, v2)
            if  d < mind:
                minv1, minv2 = v1, v2
                mind = d
    return mind, minv1, minv2


def _partition_about_xmid(p_sorted):
    px = p_sorted[0]
    s = len(px) // 2

    qx = px[:s]
    rx = px[s:]

    q_sorted = [qx]
    r_sorted = [rx]

    xr = rx[0][0]

    for i in range(1, len(p_sorted)):
        pi = p_sorted[i]
        qi =[] 
        ri = []
        for v in pi:
            if v[0] < xr:
                qi.append(v)
            else:
                ri.append(v)
        q_sorted.append(qi)
        r_sorted.append(ri)

    return q_sorted, r_sorted


def distance(v1, v2):
    assert len(v1) == len(v2)
    return (reduce(lambda x, y: x + (y[0] - y[1]) ** 2, zip(v1, v2), 0)) ** 0.5


def pairwise_distance_min(vertices):
    n = len(vertices)

    dmin = math.inf
    minv1, minv2 = None, None

    for i in range(n):
        for j in range(i + 1, n):
            v1, v2 = vertices[i], vertices[j]
            # if unionfind.find(v1) == unionfind.find(v2): continue
            if (v1, v2) in already_found: continue
            
            d = distance(v1,v2)
            if d < dmin:
                dmin = d
                minv1, minv2 = v1, v2
    return dmin, minv1,minv2
