def maximo(x,y,z):
    if ((x >= y) and (x >= z)):
        return x
    elif ((y >= x) and (y >= z)):
        return y
    else:
        return z

#print(maximo(7, 7, 6))