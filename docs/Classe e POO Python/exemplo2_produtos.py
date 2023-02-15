from datetime import datetime, date
from decimal import Decimal
from typing import Union, Tuple, Dict
from abc import ABC, abstractmethod
from ast import literal_eval
import re


MoneyTypes = Union[Decimal, str]
NumSerie = str


class Produto(ABC):
    csv_delim = ';'

    @abstractmethod
    def __init__(self, id_: str, preco: MoneyTypes, taxa_iva: MoneyTypes):        
        self.id_ = id_
        self.preco = Decimal(preco)
        if self.preco < 0:
            raise ValueError(f'Preço inválido: {preco}')
        self.taxa_iva = Decimal(taxa_iva)
        if self.taxa_iva < 0:
            raise ValueError(f'Taxa de IVA inválida: {taxa_iva}')

    @property
    def iva(self) -> Decimal:
        return self.preco * (self.taxa_iva/100)

    @property
    def preco_final(self) -> Decimal:
        return self.preco + self.iva

    def __repr__(self):
        class_name = type(self).__qualname__
        attrs = self.__dict__
        attrs_repr = ',\n'.join(f'    {attr}={val!r}' for attr, val in attrs.items())
        return f'{class_name}(\n{attrs_repr}\n)'

    def __str__(self):
        class_name = type(self).__qualname__
        return f"{class_name} id: '{self.id_}' preço: {self.preco:.2f} iva: {self.taxa_iva:.2f}%"

    @classmethod 
    def from_csv(cls, csv: str):
        delim = cls.csv_delim
        attrs = [literal_eval_extended(val) for val in csv.strip().split(delim)]
        return cls(*attrs)

    def to_csv(self):
        delim = self.csv_delim
        return delim.join(repr(val) for val in self.__dict__.values())

    def __hash__(self):
        return hash(self.id_)


class Livro(Produto): 
    def __init__(self, titulo: str, isbn: str, autores: Tuple[str,...], *args, **kwargs):
        isbn_sem_tracos = isbn.replace('-', '')
        if not isbn_sem_tracos.isdigit() or len(isbn_sem_tracos) not in (10, 13):
            raise ValueError(f'ISBN inválido: {isbn}')
        self.titulo = titulo
        self.isbn = isbn
        self.autores = autores
        super().__init__(*args, **kwargs)


class JogoComputador(Produto): 
    csv_delim = ':'

    def __init__(self, titulo: str, num_serie: NumSerie, genero: str, *args, **kwargs):
        num_serie_sem_tracos = num_serie.replace('-', '')
        if not num_serie_sem_tracos.isdigit() or len(num_serie_sem_tracos) < 7:
            raise ValueError(f'Número de série inválido: {num_serie}')
        self.titulo = titulo
        self.num_serie = num_serie_sem_tracos
        self.genero = genero
        super().__init__(*args, **kwargs)


class Encomenda:
    def __init__(self, id_: str, prods: Dict[Produto, int]):
        self.id_ = id_  
        self.data_hora = datetime.now()
        self.prods = prods

    @property
    def total(self) -> Decimal:
        return sum(prod.preco_final * quant for prod, quant in self.prods.items())
    
    @property
    def iva(self) -> Decimal:
        return sum(prod.iva for prod in self.prods)

    def __repr__(self):
        class_name = type(self).__qualname__
        prods = ', '.join(f'{prod.id_!r}: {quant}' for prod, quant in self.prods.items())
        return f'{class_name}({self.id_!r}, {self.data_hora!r}, #[{prods}])'


def literal_eval_extended(val: str) -> object:
    extensions = (
        ( r"(decimal\.)?Decimal\(\s*([0-9.']*)\s*\)", 
          lambda g: Decimal(literal_eval(g[2])) if g[2] else Decimal() ),
        ( r"(datetime\.)?date\(([0-9\s.,]+)\)",
          lambda g: date(*literal_eval(g[2])) ),
        ( r"(datetime\.)?datetime\(([0-9\s.,]+)\)",
          lambda g: datetime(*literal_eval(g[2])) )
    )
    for regex, constructor in extensions:
        result = re.match(regex, val)
        if result:
            return constructor(result)
    return literal_eval(val)


# p = Produto(id_='X21', preco='100', taxa_iva='23')
# print(repr(p))
# print('Produto:', p)
# pylint: disable=C0301

liv1 = Livro(
    titulo='Automate the Boring Stuff with Python',
    isbn='978-1593275990',
    autores=('Al Sweigart',),
    id_='LL12', 
    preco='20', 
    taxa_iva='13',
)
liv2 = Livro.from_csv("'Python Cookbook';'978-1-449-34037-7';('David Beazley', 'Brian K. Jones');'LL98';'30';'13'")
liv3 = Livro.from_csv(liv2.to_csv())

jog1 = JogoComputador(
    titulo='Assassins Creed IV',
    num_serie='8561245220',
    genero='FPS',
    id_='JC11', 
    preco='100', 
    taxa_iva='13',
)

jog2 = JogoComputador.from_csv("'Counter-Strike':'8111135910':'FPS':'JC20':Decimal('98'):Decimal('13')")

print('-----')
for p in (liv1, liv2, jog1, jog2):
    print(repr(p))
    print(p)
    print('preço final:', p.preco_final)
    print('-----')

enc1 = Encomenda(id_='12PQ78', prods={liv1: 2, liv2: 1, liv3: 3, jog1: 1, jog2: 1})
print(enc1.total)
print(enc1.iva)


