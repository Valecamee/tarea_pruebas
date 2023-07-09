import pytest 
from TareaPruebasPython.numerosAmigos import numerosAmigos

def test_prueba1():
    assert numerosAmigos(356408,399592) == "356408 y 399592 son amigos"
    
def test_prueba2():
    assert numerosAmigos(100485,124155) == "100485 y 124155 son amigos"

def test_prueba3():
    assert numerosAmigos(56,4) == "56 y 4 no son amigos"

def test_prueba4():
    assert numerosAmigos(15,10) == "15 y 10 no son amigos"

def test_prueba5():
    assert numerosAmigos(666,999) == "666 y 999 no son amigos"

def test_prueba6():
    assert numerosAmigos(3,4) == "3 y 4 son amigos"

def test_prueba7():
    assert numerosAmigos(7,15) == "7 y 15 son amigos"

def test_prueba8():
    assert numerosAmigos(177,288) == "220 y 284 no son amigos"

def test_prueba9():
    assert numerosAmigos(1184,1210) == "1184 y 1210 no son amigos"

def test_prueba10():
    assert numerosAmigos(9,2) == "9 y 2 son amigos"

if __name__ == '_main_':
    test_prueba1()
    test_prueba2()
    test_prueba3()
    test_prueba4()
    test_prueba5()
    test_prueba6()
    test_prueba7()
    test_prueba8()
    test_prueba9()
    test_prueba10()