'use strict';

////////////////////////////////////////////////////////////////////////
//
//      EXEMPLOS INTRODUTÓRIOS: CONCAT e SPLICE
//
////////////////////////////////////////////////////////////////////////

// 1a: versão
function concat(items) {
    const itemsTxt = [];
    for (let item of items) {
        itemsTxt.push(item.toString());
    }
    return itemsTxt.join('');
}

// 2a: versão
function concat(...items) {
    const itemsTxt = [];
    for (let item of items) {
        itemsTxt.push(item.toString());
    }
    return itemsTxt.join('');
}

// 3a: versão
function concat(items, sep = '', end = '') {
    const itemsTxt = [];
    for (let item of items) {
        itemsTxt.push(item.toString());
    }
    itemsTxt.push(end);
    return itemsTxt.join(sep);
}

// 4a versão: objecto de especificação
function concat(items, {sep = '', end = ''} = {}) {
    const itemsTxt = [];
    for (let item of items) {
        itemsTxt.push(item.toString());
    }
    itemsTxt.push(end);
    return itemsTxt.join(sep);
}

// SPLICE COM OBJECTO ESPECIFICAÇÃO
// array.splice(start[, deleteCount[, item1[, item2[, ...]]]])

function splice(items, spliceOptions) {    
    const {start, deleteCount, newItems} = spliceOptions;
    const result = deleteCount && newItems ? items.splice(start, deleteCount, ...newItems)
                 : deleteCount             ? items.splice(start, deleteCount)
                 : newItems                ? items.splice(start, 0, ...newItems)
                 : nums.splice(start);
    return result;
}

let nums = [14, 7, 7, 0, 1];
splice(nums, {start: 1, deleteCount: 2, newItems: [8, 8, 8]});

////////////////////////////////////////////////////////////////////////
//
//      LAMBDAS, ARROW FUNCTIONS E FUNÇÕES DE PRIMEIRA ORDEM
//
////////////////////////////////////////////////////////////////////////

const nums = [100, 15, -2, -1, 59, 44, 12, 10, 46, 77, 15, 90, 15];
const nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina'];

function filtra(itens, criterio) {    // função de 1a ordem: função que recebe outras funções
    const seleccionados = [];
    for (let item of itens) {
        if (criterio(item)) {
            seleccionados.push(item);
        }
    }
    return seleccionados;
}

function ePar(num) {
    return num % 2 === 0;
}

function ePositivo(num) {
    return num >= 0;
}

function terminadoEmOh(texto) {
    return texto[texto.length-1] === 'o';
}

function temPeloMenosTresAs(texto) {
    let quantos = 0;
    for (let ch of [...texto]) {
        if (ch === 'a') {
            quantos += 1;
        }
    }
    return quantos >= 3;
}

filtra(nums, ePar);
filtra(nums, function(num) {return num % 2 === 0;});
filtra(nums, ePositivo);
filtra(nums, function(num) {return num > 0;});
filtra(nomes, terminadoEmOh);
filtra(nomes, function(nome) {return nome[nome.length-1] === 'o'});
filtra(nomes, temPeloMenosTresAs);
filtra(nomes, function(texto) {
    let quantos = 0;
    for (let ch of [...texto]) {
        if (ch === 'a') {
            quantos += 1;
        }
    }
    return quantos >= 3;
});

// COM ARROW FUNCTIONS
filtra(nums, (num) => num % 2 === 0);
filtra(nums, (num) => num > 0);
filtra(nomes, (nome) => nome[nome.length-1] === 'o');
filtra(nomes, (texto) => {
    let quantos = 0;
    for (let ch of [...texto]) {
        if (ch === 'a') {
            quantos += 1;
        }
    }
    return quantos >= 3;
});


filtra(nums, (num) => num >= 10 && num <= 20);
filtra(nums, (num) => num === 15);
filtra(nomes, (nome) => nome.length === 7);

function entre(a, b) {
    return (num) => num >= a && num <= b;
}

function fora(a, b) {
    return (num) => num < a || num > b;
}

function tamanhoIgual(tamanho) {
    return (obj) => obj.length === tamanho;
}

filtra(nums, entre(10, 20));
filtra(nums, entre(5, 18));
filtra(nomes, tamanhoIgual(5));

////////////////////////////////////////////////////////////////////////
//
//      FILTER, MAP, FOR-EACH, REDUCE, EVERY, SOME
//
////////////////////////////////////////////////////////////////////////

let nums = [100, -2, -1, 59, 44, 46, 77];
let nomes = ['alberto', 'bruno', 'armando', 'josé', 'albertina'];

nums.filter((num) => num >= 50);
nums.map((num) => 2 * num);

for (let nome of nomes) {
    console.log(nome);
}

nomes.forEach((nome) => console.log(nome));
nomes.forEach(console.log);
nomes.forEach((nome, i) => console.log(`${i} -> ${nome}`));

let sum = 0;
for (let num of nums) {
    sum += num;
}

nums.reduce((acumulador, num) => acumulador + num, 0);
nomes.reduce((acumulador, nome) => acumulador + nome + '/', '');

let todosPositivos = true;
for (let num of nums) {
    if (num <= 0) {
        todosPositivos = false;
        break;
    }
}

function todosPositivos(nums) {
    for (let num of nums) {
        if (num <= 0) {
            return false;
        }
    }
    return true;
}

nums.every((num) => num > 0);
nums.some((num) => num > 0);


////////////////////////////////////////////////////////////////////////
//
//      RECURSIVIDADE
//      FUNCÕES INTERNAS / ANINHADAS
//
////////////////////////////////////////////////////////////////////////

//
// FACTORIAL 

// N! = N x (N-1) x (N-2) x ... x 1
// N! = N x (N-1)!
// 1! = 1
// 0! = 1

function factorialI(n) {
    let res = 1;
    for (let i = n; i > 0; i -= 1) {
        res *= i;
    }
    return res;
}

function factorialR(n) {
    if ([0, 1].includes(n)) {
        return 1;
    }
    return n * factorialR(n - 1);
}

// factorialR(5) = 5 * 24 = 120
// factorialR(4) = 4 * 6 = 24
// factorialR(3) = 3 * 2 = 6
// factorialR(2) = 2 * 1 = 2
// factorialR(1) = 1

//
// FIBONACCI 

// Fib(N) = Fib(N-1) + Fib(N-2)
// Fib(1) = 1
// Fib(0) = 0

function fibI(n) {
    if ([0, 1].includes(n)) {
        return n;
    }
    let [x, y] = [0, 1];
    for (let i = 2; i <= n; i += 1) {
        [y, x] = [y + x, y];
    }
    return y;
}

function fibI(n) {
    if ([0, 1].includes(n)) {
        return n;
    }
    let [f2, f1] = [0, 1];
    let fN;
    for (let i = 2; i <= n; i += 1) {
        fN = f1 + f2;
        f2 = f1;
        f1 = fN;
    }
    return fN;
}

function fibR(n) {
    if ([0, 1].includes(n)) {
        return n;
    }
    return fibR(n - 1) + fibR(n - 2)
}

//
// PALINDROMO 

// Exemplo: txt = 'AABAA'
//
//     i ->
//     0     1     2     3     4
//     A  |  A  |  B  |  A  |  A 
//    -5    -4    -3    -2    -1
//                          <- j

function ePalindromo(txt) {
    let [i, j] = [0, txt.length - 1];
    while (i < j) {
        if (txt[i] != txt[j]) {
            return false;
        }
        i += 1;
        j -= 1;
    }
    return true;
}

//
// FLATTEN

let nums = [1, 2, [3, [4, 5], 6], 7];

function flatten(arr) {
    if (arr.length === 0) {
        return [];
    }
    let [first, rest] = [arr[0], arr.slice(1)];
    if (Array.isArray(first)) {
        return flatten(first).concat(flatten(rest));
    }
    return [first].concat(flatten(rest));
}

function flatten(arr) {
    function doFlatten(arr, pos, retArr) {
        if (pos === arr.length) {
            return;
        }

        let first = arr[pos];
        if (Array.isArray(first)) {
            doFlatten(first, 0, retArr);
        }
        else {
            retArr.push(first);
        }
        doFlatten(arr, pos + 1, retArr);
    }

    let retArr = [];
    doFlatten(arr, 0, retArr);
    return retArr;
}

////////////////////////////////////////////////////////////////////////
//
//      CLOSURES E IIFES
//
////////////////////////////////////////////////////////////////////////

// . Contexto da função interna, ou envolvida, inclui o contexto da função 
//   externa, ou envolvente
// . Este contexto persiste após a função externa ter terminado
// . Contexto de uma função é o âmbito do bloco dessa função (mais o âmbito 
//   global)
// . Âmbito de uma função interna é um âmbito dessa função mais o âmbito da
//   da função externa
//
// NOTA: Termo "contexto" utilizado como sinónimo de "âmbito" ou de 
//       "escopo" (scope)
// 
// Âmbito de bloco (block scope):
//
//  {
//      let X;
//      {
//          let Y;
//          ... temos acesso a X e Y ...
//      }
//      ... temos acesso a apenas a X ...
//  }
//
// O mesmo aplica-se a funções:
// 
//  function verde() {
//      let X;
//      function vermelha() {
//          let Y;
//          ... temos acesso a X e Y ...
//      }
//      ... temos acesso a apenas a X ...
//      return vermelha;    // funcao é um objecto com acesso a X e Y e params de preta
//  }
//
//      ┌─────────────────────────────────┐
//      │              ┌───────────────┐  │
//      │              │               │  │
//      │  VERMELHA    │     VERDE     │  │
//      │              │               │  │
//      │              └───────────────┘  │
//      └─────────────────────────────────┘
//

// EXEMPLO 1: SOMADOR

function somador(n) {
    function somador(x) {
        return x + n;
    }
    return somador;
}
somaA = somador(10)
somaA(1)        // 11
somaA(10)       // 20

// Ou, de forma mais sucinta, utilizando uma lambda:

function somador(n) {
    return function(x) {
        return x + n;
    }
}

// "Arrow functions", que também são lambdas, tornam o código ainda 
// mais sucinto:

function somador(n) {
    return (x) => x + n;
}

// EXEMPLO3: GERADORES COM CLOSURES
//
// Iteradores e geradores são mecanismos para "personalizar" e tornar 
// mais eficiente a iteração em linguagens funcionais. O ES6 trouxe  
// suporte nativo para estes conceitos em JavaScript. Porém, podemos
// utilizar closures para implementar geradores:

function contador() {
    let count = 0;
    return function() {
        return count += 1;
    }
}

conta = contador();
console.log(conta());   // 1
console.log(conta());   // 2
console.log(conta());   // 3

// EXEMPLO4: GERADORES COM CLOSURES

function range(start, end, step=1) {
    let count = start;
    return function() {
        let value = step > 0 && count < end || step < 0 && count > end
                  ? count 
                  : undefined;
        count = count + (value !== undefined) * step;
        return value;
    }
}

r1 = range(0, 3)
console.log(r1());   // 0
console.log(r1());   // 1
console.log(r1());   // 2
console.log(r1());   // undefined

r2 = range(0, 10, 2)
console.log(r2());   // 0
console.log(r2());   // 2
console.log(r2());   // 4
console.log(r2());   // 6
console.log(r2());   // 8
console.log(r2());   // undefined


r3 = range(20, 14, -2)
console.log(r3());   // 20
console.log(r3());   // 18
console.log(r3());   // 16
console.log(r3());   // undefined

// EXEMPLO5: CONVERSOR DE MESES

// Com variável global => mau!
let months = [
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
];

function toMonthName(monthNum) {
    return months[monthNum-1];
}
console.log(toMonthName(4));

// Sem variável global => lento
function toMonthName(monthNum) {
    let months = [
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
        'December',
    ];
    return months[monthNum-1];
}
console.log(toMonthName(4));

// Com closure
function makeToMonthName() {
    let months = [
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
        'December',
    ];    
    return function(monthNum) {
        return months[monthNum-1];
    }
}

toMonthName = makeToMonthName();

const toMonthName = (function() {
    let months = [
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
        'December',
    ];    
    return function toMonthName(monthNum) {
        return months[monthNum-1];
    }
})();    // IIFE : Immediately Invoked Function Expression

// EXEMPLO6: COMPILAÇÃO DE EXPRESSÕES REGULARES FEITA SÓ UMA VEZ EM 
//           VAR. LOCAL DE UMA CLOSURE 

function isValidDate(date) {
    const YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    const DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    const DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    const DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    const LEAP_YEARS = '(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                       + '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                       + '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                       + '|2020|2024|2028|2032|2036|2040|2044|2048)'
                       ;
    const DD_FEB_LEAP_YEAR = `(0[1-9]|[12][0-9])/02/${LEAP_YEARS}`;
    const dateRegExp = new RegExp(
        `^(${DD_FEB_LEAP_YEAR}|(${DD_MM_31}|${DD_MM_30}|${DD_FEB})/${YEAR})$`
    );
    return dateRegExp.test(date.trim());
}

const isValidDate = (function() {
    const YEAR       = '(19[0-9][0-9]|20[0-4][0-9]|2050)';
    const DD_MM_31   = '(0[1-9]|[12][0-9]|30|31)/(0[13578]|1[02])';
    const DD_MM_30   = '(0[1-9]|[12][0-9]|30)/(0[469]|11)';
    const DD_FEB     = '(0[1-9]|1[0-9]|2[0-8])/02';
    const LEAP_YEARS = '(1904|1908|1912|1920|1924|1928|1932|1936|1940|1944'
                       + '|1948|1952|1956|1960|1964|1968|1972|1976|1980'
                       + '|1984|1988|1992|1996|2000|2004|2008|2012|2016'
                       + '|2020|2024|2028|2032|2036|2040|2044|2048)'
                       ;
    const DD_FEB_LEAP_YEAR = `(0[1-9]|[12][0-9])/02/${LEAP_YEARS}`;
    const dateRegExp = new RegExp(
        `^(${DD_FEB_LEAP_YEAR}|(${DD_MM_31}|${DD_MM_30}|${DD_FEB})/${YEAR})$`
    );
    return function isValidDate(date) {
        return dateRegExp.test(date.trim())
    };
})();

function timedRun(fun, ...args) {
    const start = Date.now();
    for (let i = 0; i < 10_000_000; i += 1) {
        fun(...args);
    }
    return (Date.now() - start) / 1000;
}
