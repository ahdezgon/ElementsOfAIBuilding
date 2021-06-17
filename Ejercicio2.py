portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

co2 = 0.020
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    global smallest
    global bestroute
    if len(ports)==0:
        emission = sum([D[route[i]][route[i+1]]*co2 for i in range(len(route)-1)])
        if emission < smallest:
            smallest = emission
            bestroute = route
   
    # Mantener la ruta con menos emisiones
    for i, port in enumerate(ports):
        permutations(route+[port], ports[:i]+ports[i+1:])

def main():
    permutations([0], list(range(1, len(portnames))))

    # Imprimir la mejor ruta
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
