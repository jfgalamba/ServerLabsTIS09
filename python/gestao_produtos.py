"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Listar o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
"""

from decimal import Decimal as dec
import subprocess
import sys
from typing import TextIO

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3

################################################################################
##
##       PRODUTOS E CATÁLOGO
##
################################################################################

class Produto:
    def __init__(self, id: int, nome: str):
        if id < 0 or len(str(id)) != 5:
            raise ValueError(f'{id=} inválido (deve ser > 0 e ter 5 dígitos)')
        self.id = id
        self.nome = nome
    #:
    
    def __str__(self):
        return f"Produto[id: {self.id} nome: {self.nome}]"
    #:
#:

def main():
    prod1 = Produto(30987, "pão de milho")
    prod2 = Produto(30098, "leite mimosa")

    print(prod1)
    print(prod2)

    try:
        Produto(398, "leite mimosa")
    except ValueError as ex:
        print("ATENÇÃO: Produto inválido!")
        print(ex)
#:

if __name__ == '__main__':
    main()
#:



# class Xpto {

#     public toString() {
#         return String.format("Xpto: valor de a -> %d", a);
#     }

#     private int a;
# }

# var obj = new Xpto();
# obj.a = 100;
# System.out.println(obj);    // Xpto: valor de a -> 100