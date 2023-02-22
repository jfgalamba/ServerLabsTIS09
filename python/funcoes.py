##########################################
#
#       FUNÇÕES
#
##########################################

# concat('abc', 'def') => 'abcdef'
# concat('abc', 23, True, ['alberto', 19]) => "abc23True['alberto', 19]"
# concat('abc', 23, 'def', sep='/', end='.') => 'abc/23/def.'

from typing import Iterable


def concat(*args, sep='', end='') -> str:
    items_str = []
    for arg in args:
        items_str.append(str(arg))
    #:
    items_str.append(end)
    return sep.join(items_str)
#:

# concat('abc', 'def')
# concat('abc', 'def')


def fun1(a, b, *args):
    print(a)
    print(b)
    print(args)
#:

fun1(2, 3)
fun1(2, 3, 4, 5, 6)

def fun2(a, b, *args, c):   # sim, isto é possível...
    print(a)
    print(b)
    print(args)
    print(c)

fun2(1, 2, 4, 5, c = 3)

def fun3(a, b, *args, c=78, d=90, **kargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kargs)
#:

fun3(1, 2, 3, 4, 5, d = 5, e = 900, xpto = 'alberto')

def fun4(*args, **kargs):
    print(args)
    print(kargs)
#:

#####################################################
# 
#       FUNÇÕES DE PRIMEIRA ORDEM
#       Funções parametrizadas com outras funções
#
#####################################################

nums = [100, -2, -1, 59, 44, 46, 77]
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

def filtra_positivos(itens: Iterable) -> list:
    seleccionados = []
    for item in itens:
        if item > 0:
            seleccionados.append(item)
    return seleccionados
#:

def filtra_pares(itens: Iterable) -> list:
    seleccionados = []
    for item in itens:
        if item % 2 == 0:
            seleccionados.append(item)
    return seleccionados
#:

def filtra_maiores_que_50(itens: Iterable) -> list:
    seleccionados = []
    for item in itens:
        if item > 50:
            seleccionados.append(item)
    return seleccionados
#:

def filtra_tamanho_maior_que_6(itens: Iterable) -> list:
    seleccionados = []
    for item in itens:
        if len(item) > 6:
            seleccionados.append(item)
    return seleccionados
#:

def filtra(itens: Iterable, criterio) -> list:
    seleccionados = []
    for item in itens:
        if criterio(item):
            seleccionados.append(item)
    return seleccionados
#:

def e_positivo(num: int) -> bool:
    return num > 0
#:

def e_par(num: int) -> bool:
    return num % 2 == 0
#:

def tamanho_maior_que_6(elem) -> bool:
    return len(elem) > 6
#:

filtra(nums, e_par)
filtra(nums, lambda num: num % 2 == 0)
filtra(nums, e_positivo)
filtra(nums, lambda num: num % 2 == 0)

filtra(nomes, tamanho_maior_que_6)
dim = int(input("Tamanho? "))
filtra(nomes, lambda nome: len(nome) > dim)

# MAPEIA

def mapeia(itens: Iterable, mapeamento) -> list:
    transformados = []
    for item in itens:
        transformados.append(mapeamento(item))
    #:
    return transformados
#:

def dobro(num: int | float) -> float:
    return 2.0 * num
#:

mapeia(nums, dobro)
mapeia(nums, lambda num: 2.0 * num)
mapeia(nomes, lambda nome: nome[0])
mapeia(nomes, lambda nome: nome[-1])
mapeia(nomes, len)

# FUNÇÕES BUILT-IN FILTER, MAP, SORTED

nums = [100, -2, -1, 59, 44, 46, 77]
nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina']

list(filter(lambda num: num > 0, nums))
tuple(map(lambda num: 2 * num, nums))

# Três 1as letras dos nomes com mais do que 6 caracteres
map(lambda nome: nome[:3], filter(lambda nome: len(nome) > 6, nomes))

# SORTED

nums = [100, -2, -1, 59, 44, 46, 77, 1000000, 10, 440, -7003]

# Ordenação ascendente usando o operador <
sorted(nums)

sorted(nums, key = lambda num: str(abs(num))[0])

# Ordenação ascendente pelo último caractere
sorted(nomes, key = lambda nome: nome[-1])

# Ordenação descendente
sorted(nomes, reverse=True)

#####################################################
# 
#       EXPRESSÃO LISTA (e outras)
#       Alternativa mais idiomática a MAP e FILTER
#
#####################################################

# list(map(lambda x: 2 * x, nums))
# list(filter(lambda x: x > 0, nums))
# list(map(lambda x: 2 * x, filter(lambda x: x > 0, nums)))

[2 * x for x in nums]
[x for x in nums if x > 0]
[2 * x for x in nums if x > 0]

#####################################################
# 
#       RECURSIVIDADE
#       FUNÇÕES INTERNAS / ANINHADAS / NESTED
#
#####################################################

#
# FACTORIAL 

# N! = N x (N-1) x (N-2) x ... x 1
# N! = N x (N-1)!
# 1! = 1
# 0! = 1

def factorialI(n: int) -> int:
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res
#:

def factorialR(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorialR(n - 1)
#:

# factorialR(5) = 5 * 24 = 120
# factorialR(4) = 4 * 6 = 24
# factorialR(3) = 3 * 2 = 6
# factorialR(2) = 2 * 1 = 2
# factorialR(1) = 1

#
# FIBONACCI 

# Fib(N) = Fib(N-1) + Fib(N-2)
# Fib(1) = 1
# Fib(0) = 0

def fibI(n):
    if n in (0, 1):
        return n
    x, y = 0, 1
    for _ in range(2, n + 1):
        y, x = y + x, y
    return y
#:

def fibI(n):
    if n in (0, 1):
        return n
    f2, f1 = 0, 1
    for _ in range(2, n + 1):
        fN = f1 + f2
        f2 = f1
        f1 = fN
    return fN
#:

def fibR(n):
    if n in (0, 1):
        return n
    return fibR(n - 1) + fibR(n - 2)
#:

#
# PALINDROMO 

# Exemplo: txt = 'AABAA'
#
#     i ->
#     0     1     2     3     4
#     A  |  A  |  B  |  A  |  A 
#    -5    -4    -3    -2    -1
#                          <- j

def e_palindromoI(txt: str) -> bool:
    i, j = 0, len(txt) - 1
    while i < j:
        if txt[i] != txt[j]:
            return False
        i += 1
        j -= 1
    #:
    return True
#:

def e_palindromoR(txt: str) -> bool:
    if len(txt) <= 1:
        return True
    return txt[0] == txt[-1] and e_palindromoR(txt[1:-1])
#:

# e_palindromoR('ABCBA') = ('A' == 'A' and e_palindromoR('BCB'))
#                        = True and True
#                        = True

# e_palindromoR('BCB') = ('B' == 'B' and e_palindromoR('C'))
#                      = True and True 
#                      = True

# e_palindromoR('C') = True (pq len('B') <= 1)

#
# FLATTEN

nums = [1, 2, [3, [4, 5], 6], 7] 

def flatten(lst: list) -> list:
    if len(lst) == 0:
        return []

    first, rest = lst[0], lst[1:]
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
    return [first] + flatten(rest)
#: 

def flatten(lst: list) -> list:
    def do_flatten(lst: list, pos: int, ret_list: list):
        if pos == len(lst):
            return

        first = lst[pos]
        if isinstance(first, list):
            do_flatten(first, 0, ret_list)
        else:
            ret_list.append(first)
        do_flatten(lst, pos + 1, ret_list)
    #:
    ret_list = []
    do_flatten(lst, 0, ret_list)
    return ret_list
#:

#####################################################
# 
#       FUNÇÕES INTERNAS: CLOSURES
#
#####################################################

# def verde(Z):
#     X = ...    # definir X
#     def vermelha(...):
#         Y = ...
#         # tem acesso a X e a Y e a Z
#         ...
#     ...
#     # tem acesso apenas X 
#     return vermelha 
#
#         ┌─────────────────────────────────┐
#         │              ┌───────────────┐  │
#         │              │               │  │
#         │  VERMELHA    │     VERDE     │  │
#         │              │               │  │
#         │              └───────────────┘  │
#         └─────────────────────────────────┘

def somador(x: int):
    def soma(y: int):
        return x + y
    return soma
#:

def somador(x: int):
    return lambda y: x + y
#:

somaA = somador(10)
somaA(1)        # 11
somaA(10)       # 20

def contador(inicio = 0):
    i = inicio - 1
    def conta():
        nonlocal i
        i += 1
        return i
    return conta
#:

##################

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def month_name(month_num: int) -> str:
    return months[month_num - 1]
#:

def month_name(month_num: int) -> str:
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return months[month_num - 1]
#:

def _make_month_name():
    months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]

    return lambda month_num: months[month_num - 1]
#:

month_name = _make_month_name()

########################

import re
import time

def is_valid_date(date: str) -> bool:
    YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    LEAP_YEARS = ('(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                    '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                    '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                    '|2020|2024|2028|2032|2036|2040|2044|2048)' )
    DD_FEB_LEAP_YEAR = f'(0[1-9]|[12][0-9])/02/{LEAP_YEARS}';
    date_reg_exp = re.compile(
        rf'^({DD_FEB_LEAP_YEAR}|({DD_MM_31}|{DD_MM_30}|{DD_FEB})/{YEAR})$'
    )
    return bool(date_reg_exp.match(date.strip()))
#:

# is_valid_date('10/02/2021')   DD/MM/AAAA

def _make_is_valid_date():
    YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    LEAP_YEARS = ('(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                    '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                    '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                    '|2020|2024|2028|2032|2036|2040|2044|2048)' )
    DD_FEB_LEAP_YEAR = f'(0[1-9]|[12][0-9])/02/{LEAP_YEARS}';
    date_reg_exp = re.compile(
        rf'^({DD_FEB_LEAP_YEAR}|({DD_MM_31}|{DD_MM_30}|{DD_FEB})/{YEAR})$'
    )
    return lambda date: bool(date_reg_exp.match(date.strip()))
#:

is_valid_date = _make_is_valid_date()

def timed_run(fun, *args, **kargs):
    start  = time.time()
    for _ in range(10_000_000):
        fun(*args, **kargs)
    return int(time.time() - start)
#:
