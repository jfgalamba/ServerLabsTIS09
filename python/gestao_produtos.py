"""
Programa para gestão do catálogo de produtos. Este programa permite:
    - Lista o catálogo
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

PRODUCT_TYPES = {
    'AL': 'Alimentação',
    'DL': 'Detergente p/ Loiça',
    'FRL': 'Frutas e Legumes'
}

# id    : > 0 e tem que ter cinco digitos
# nome
# tipo
# quantidade
# preco

class Produto:
    def __init__(
            self, 
            id_: int, 
            nome: str, 
            tipo: str, 
            quantidade: int,
            preco: dec,
    ):
        if id_ < 0 or len(str(id_)) != 5:
            raise InvalidProdAttribute(f'{id_=} inválido (deve ser > 0 e ter 5 dígitos)')
        if not nome:
            raise InvalidProdAttribute('Nome vazio')
        if tipo not in PRODUCT_TYPES:
            raise InvalidProdAttribute(f'Tipo de produto ({tipo}) desconhecido')
        if quantidade < 0:
            raise InvalidProdAttribute('Quantidade deve ser >= 0')
        if preco < 0:
            raise InvalidProdAttribute('Preço deve ser >= 0')

        self.id = id_
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.preco = preco
    #:

    @classmethod
    def from_csv(cls, linha: str, delim = CSV_DEFAULT_DELIM) ->  'Produto':
        attrs = linha.split(delim)
        return cls(
            id_ = int(attrs[0]),
            nome = attrs[1],
            tipo = attrs[2],
            quantidade = int(attrs[3]),
            preco = dec(attrs[4]),
        )
    #:

    @property
    def desc_tipo(self) -> str:
        return PRODUCT_TYPES[self.tipo]
    #:

    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}[id_= {self.id}  nome = "{self.nome}" tipo = "{self.tipo}"]'
    #:

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}(id_={self.id}, nome="{self.nome}", tipo="{self.tipo}", '\
                f'quantidade={self.quantidade}, preco={repr(self.preco)})'
    #:

    def __lt__(self, prod: 'Produto') -> bool:
        return self.id < prod.id
    #:

    def __eq__(self, prod: 'Produto') -> bool:
        return self.id == prod.id
    #:

    def com_iva(self, taxa_iva: dec) -> dec:
        return self.preco * (1 + taxa_iva/100)
    #:
#:

class InvalidProdAttribute(ValueError):
    pass
#:

class CatalogoProdutos:
    def __init__(self):
        self._prods = {}
    #:

    def append(self, prod: Produto):
        if prod.id in self._prods:
            raise DuplicateValue(f'Já existe produto com id {prod.id} no catálogo')
        self._prods[prod.id] = prod
    #:

    def _dump(self):
        for prod in self._prods.values():
            print(prod)
        #:
    #:

    def obtem_por_id(self, id: int) -> Produto | None:
        return self._prods.get(id)
    #:

    def pesquisa(self, criterio) -> 'CatalogoProdutos':
        encontrados = CatalogoProdutos()
        for prod in self._prods.values():
            if criterio(prod):
                encontrados.append(prod)
        return encontrados
    #:

    def remove_por_id(self, id: int) -> Produto | None:
        prod = self._prods.get(id)
        if prod:
            del self._prods[id]
        return prod
    #:

    # def remove(self, criterio) -> 'CatalogoProdutos':
    #     removidos = CatalogoProdutos()
    #     for prod in self._prods.values():    # não funciona: não podemos 
    #         if criterio(prod):               # apagar num dicionário que
    #             del self._prods[prod.id]     # que está a ser iterado
    #             removidos.append(prod)
    #     return removidos
    # #:

    def remove(self, criterio) -> 'CatalogoProdutos':
        a_remover = self.pesquisa(criterio)
        for prod in a_remover:
            del self._prods[prod.id]
        return a_remover
    #:

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}[#produtos = {len(self._prods)}]'
    #:

    def __iter__(self):
        for prod in self._prods.values():
            yield prod
        #:
    #:

    def __len__(self):
        return len(self._prods)
    #:
#:

class DuplicateValue(Exception):
    pass
#:

################################################################################
##
##       LEITURA DOS FICHEIROS
##
################################################################################

def le_produtos(caminho_fich: str, delim = CSV_DEFAULT_DELIM) -> CatalogoProdutos:
    prods = CatalogoProdutos()
    # ler ficheiro e popular catalogo com cada um dos produtos
    # uma linha do ficheiro corresponde a um produto 
    with open(caminho_fich, 'rt') as fich:
        for linha in linhas_relevantes(fich):
            prods.append(Produto.from_csv(linha, delim))
    return prods
#:

def linhas_relevantes(fich: TextIO):
    for linha in fich:
        linha = linha.strip()
        if len(linha) == 0 or linha[0] == '#':
            continue
        yield linha
#:

################################################################################
##
##       MENU, OPÇÕES E INTERACÇÃO COM UTILIZADOR
##
################################################################################

def exibe_msg(*args, indent = DEFAULT_INDENTATION, **kargs):
    print(' ' * (indent - 1), *args, **kargs)
#:

def entrada_info(msg: str) -> str:
    exibe_msg(msg, end='')
    return input()
#:

def entrada(msg: str, indent = DEFAULT_INDENTATION) -> str:
    return input(f"{' ' * DEFAULT_INDENTATION}{msg}")
#:

def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)
    #:
#:

def pause(msg: str="Pressione ENTER para continuar...", indent = DEFAULT_INDENTATION):
    input(f"{' ' * indent}{msg}")
#:

produtos = CatalogoProdutos()

def exec_menu():
    """
    - Lista o catálogo
    - Pesquisar por alguns campos 
    - Eliminar um registo do catálogo
    - Guardar o catálogo em ficheiro
    """

    while True:
        cls()
        exibe_msg("*******************************************")
        exibe_msg("* L - Listar catálogo                     *")
        exibe_msg("* P - Pesquisar por id                    *")
        exibe_msg("* PN - Pesquisar por nome                 *")
        exibe_msg("* A - Acrescentar produto                 *")
        exibe_msg("* E - Eliminar produto                    *")
        exibe_msg("* G - Guardar catálogo em ficheiro        *")
        exibe_msg("*                                         *")
        exibe_msg("* T - Terminar programa                   *")
        exibe_msg("*******************************************")

        print()
        opcao = entrada("OPCAO> ").strip().upper()

        if opcao in ('L', 'LISTAR'):
            exec_listar()
        elif opcao in ('T', 'TERMINAR'):
            # exec_terminar()
            break
        elif opcao in ('P', 'PESQUISAR'):
            exec_pesquisar_por_id()
        elif opcao in ('PN',):
            exec_pesquisar_por_nome()
        else:
            exibe_msg(f"Opção {opcao} inválida!")
            pause()
        #:
    #:
#:

def exec_listar():
    cabecalho = f'{"ID":^8}|{"Nome":^26}|{"Tipo":^8}|{"Quantidade":^16}|{"Preço":^16}'
    separador = f'{"-" * 8}+{"-" * 26}+{"-" * 8}+{"-" * 16}+{"-" * 16}'
    # separador =  '|'.join(['-' * 16] * 5)
    print()
    exibe_msg(cabecalho)
    exibe_msg(separador)
    for prod in produtos:
        linha = f'{prod.id:^8}|{prod.nome:^26}|{prod.tipo:^8}|{prod.quantidade:^16}|{prod.preco:^16}'
        exibe_msg(linha)
    #:
    exibe_msg(separador)
    print()
    pause()
#:

def exec_pesquisar_por_id():
    id_ = int(entrada_info("Indique o ID: "))

    if prod := produtos.obtem_por_id(id_):    # ver nota em baixo
        exibe_msg("Produto encontrado")
        exibe_msg(prod)
    else:
        exibe_msg(f"Não foi encontrado nenhum produto com ID {id_}")
    #:
    print()
    pause()
#:

# NOTA: O operador ':=' (designado de operador morsa/walrus operator) 
# foi introduzido com o Python 3.8 e permite atribuir um valor e devolver
# esse valor. O operador '=' apenas permite atribuir o valor. Ou seja, 
# o operador ':=' é também uma expressão.
#
# Por exemplo, vamos supor que pretendemos atribuir a x o dobro de y 
# e, simultaneamente, queremos exibir esse valor. Com o operador '='
# necessitamos sempre de duas instruções (vamos assumir que y == 10):
#
#       >>> x = 2 * y
#       >>> print(f"Valor de X: {x}")
#       Valor de X: 20
#       >>> x
#       20
#   
# Com o operador ':=' podemos combinar atribuição e print numa só 
# instrução:
#
#       >>> print(f"Valor de X: {(x := 2*y)}")  
#       Valor de X: 20
#       >>> x
#       20
#
# De notar que os parênteses curvos dentro da expressão da f-string são 
# obrigatórios para que o Python não interprete o que está à direita do
# ':' como sendo uma especificação de formatação.

def exec_pesquisar_por_nome():
    nome = entrada_info("Nome do produto: ")
    prods = produtos.pesquisa(lambda prod: nome in prod.nome)
    if len(prods) != 0:   # ver nota em baixo
        cls()
        exibe_msg("Foram encontrados os seguintes produtos:\n".upper())
        for prod in prods:
            exibe_msg(prod, indent=DEFAULT_INDENTATION * 2)
    else:
        exibe_msg(f"Não foram encontrados produtos com a designação {nome}")
    #:
    print()
    pause()
#:

# NOTA: em alternativa também poderíamos ter escrito este if 
# da seguinte forma:
#
#       if prods := produtos.pesquisa(lambda prod: nome in prod.nome):
#           etc
#
# Ou, sem o operador morsa, 
#
#       prods = produtos.pesquisa(lambda prod: nome in prod.nome)
#       if prods:
#           etc
#
# isto é possível porque em Python uma colecção vazia avalia a False.
# Porém, apesar de eu ter utilizado este idioma durante muitos anos, 
# hoje prefiro ser mais explícito e utilizar o teste directo com 
# o len, isto para distinguir dos casos em que uma expressão possa 
# mesmo ser False ou None. O código fica mais claro e legível com o
# len.

def exec_terminar():
    sys.exit(0)
#:

def main():
    global produtos
    produtos = le_produtos('produtos.csv')
    exec_menu()
#

if __name__ == '__main__':
    main()
#: