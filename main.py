# Zadannie Nr. 1

def generator_kod_pocztowych(od,do):
    lista1 = []
    ostatnia_l = 1001
    od_lista = [int(x) for x in od.split("-")]
    do_lista = [int(x) for x in do.split("-")]
    for pierwsza_l in range(od_lista[0], do_lista[0]+1):
        if pierwsza_l == od_lista[0]:
            for x in range(od_lista[1], ostatnia_l): # pierwsza liczba
                lista1.append(str(pierwsza_l) + "-" + str(x))

        elif od_lista[0] < pierwsza_l < do_lista[0]: # liczby miedzy glownymi
            for e in range(1, ostatnia_l):
                if len(str(e)) == 1:
                    lista1.append(str(pierwsza_l) + "-" + "00" + str(e))
                elif len(str(e)) == 2:
                    lista1.append(str(pierwsza_l) + "-" + "0" + str(e))
                elif len(str(e)) == 3:
                    lista1.append(str(pierwsza_l) + "-" + str(e))

        elif do_lista[0] == pierwsza_l:
            for l in range(1, do_lista[1]+1): # ostatnia liczba
                if len(str(l)) == 1:
                    lista1.append(str(pierwsza_l) + "-" + "00" + str(l))
                elif len(str(l)) == 2:
                    lista1.append(str(pierwsza_l) + "-" + "0" + str(l))
                elif len(str(l)) == 3:
                    lista1.append(str(pierwsza_l) + "-" + str(l))
    return lista1

# Zadanie Nr. 2

def sprawdzanie_liczb(*liczy):
    n = [e for e in range(1,11)] # lista od 1-10
    lista_liczb = None # tam wlazi lista z inputa
    output = []
    for e in list(liczy): # sprawdza czy wejscie ma liste
        if isinstance(e, list):
            lista_liczb = e
    for x in n:
        if x not in lista_liczb:
            output.append(x)
    return output

# Zadanie Nr. 3

def wygenerowanie_liczb_decimal(pierwsza_l,druga_l):
    lista = []
    liczba = pierwsza_l
    for x in range(0, int((druga_l - pierwsza_l) / 0.50)+1):
        lista.append(liczba)
        liczba += 0.50
    return lista


if __name__ == '__main__':
    print(generator_kod_pocztowych("75-900","80-155"))
    print("-"*700)
    print(sprawdzanie_liczb([2,3,7,4,9], 10))
    print("-" * 700)
    print(wygenerowanie_liczb_decimal(2,5.50))
