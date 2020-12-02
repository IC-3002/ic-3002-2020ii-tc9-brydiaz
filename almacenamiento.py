def maximizar(As, D):

    As.sort(key=lambda x: x[1])
    total = 0
    sucesion = []

    i = 0

    while total < D and i < len(As):
        if total + As[i][1] <= D:
            total =  total + As[i][1]
            sucesion.append(As[i])
        else:
            return  sucesion

        i = i + 1