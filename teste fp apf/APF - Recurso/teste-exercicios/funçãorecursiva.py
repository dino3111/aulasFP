def piramide(layer):
    if layer == 1:
        return 1
    else:
        return 4 * (layer-1) + piramide(layer-1)
    
print(piramide(3))
    