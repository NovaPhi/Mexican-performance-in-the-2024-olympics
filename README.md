
Página
1
de 6
# Parcial
0. Escribe en Elixir una **función** que reciba una lista de números enteros, y
que regrese una nueva lista de listas. Cada sublista contiene 3 elementos:
el número original, el número en negativo y el inverso del número. El
inverso de $n$ es $1/n$. Ejemplo:
Entrada: `[3, 7, -2, -1]`
Salida: `[[3, -3, 0.333], [7, -7, 0.1428], [-2, 2, -0.5], [-1, 1, -1.0]]`
0. Realiza la demostración por inducción de la siguiente propiedad para valores de
$n \ge 1$:
$\sum_{i=1}^n (i \cdot i!) = (n + 1)! - 1$
**SOLUTION**
**I. Basis** if $n = 1$
$\sum_{i=1}^1 (i \cdot i!) = (1 + 1)! - 1$
$1 \cdot 1! = (1 + 1)! - 1$
$1 \cdot 1 = (1 + 1)! - 1$
$1 = (1 + 1)! - 1$
$1 = (2)! - 1$
$1 = 2 - 1$
$1 = 2 - 1$
$1 = 1$
**II. Inductive Hypothesis** if $n = k$
$\sum_{i=1}^k (i \cdot i!) = (k + 1)! - 1$
**II. Inductive Step** if $n = (k + 1)$
$\sum_{i=1}^{k+1} (i \cdot i!) = ((k + 1) + 1)! - 1$
$\sum_{i=1}^k (i \cdot i!) + (k + 1)\cdot (k + 1)! = ((k + 1) + 1)! - 1$
$(k + 1)! - 1 + (k + 1)\cdot (k + 1)! = ((k + 1) + 1)! - 1$
$(1 + (k + 1))(k + 1)! - 1 = ((k + 1) + 1)! - 1$
$((k + 1) + 1)(k + 1)! - 1 = ((k + 1) + 1)! - 1$
$((k + 1) + 1)! - 1 = ((k + 1) + 1)! - 1$
$\square$
0. Define **(de manera recursiva | usando expresiones regulares | mediante un
DFA)**
el lenguaje en $\Sigma = \{a, b, c\}$ que contiene $abc$, y dónde las $c$
sólo pueden aparecer después de otra $c$.
**SOLUTION**
Recursive definition:
- I. Basis: $abc \in L$
- II. Recursive Step: If $u \in L$ then $au \in L$, $bu \in L$, $ua \in L$,
$ub \in L$. If $u = xc$, then $uc \in L$
- III. Closure: $u \in L$ only if it can be obtained from the basis using
a finite number of applications of the recursive step.
Regex: $\{a, b\}*abc\{c\}*\{a, b\}*$
State diagram:
```mermaid
flowchart LR
%% Indicator of start state
0(( ))
A((A))
B((B))
C((C))
D(((D)))
E(((E)))
ERR([ERR])
0:::start emy@==> A
A emy@==a==> B
A emy@==b==> A
A emy@==c==> ERR
B emy@==a==> B
B emy@==b==> C
B emy@==c==> ERR
C emy@==a==> B
C emy@==b==> A
C emy@==c==> D
D emy@==a,b==> E
D emy@==C==> D
E emy@==a,b==> E
E emy@==c==> ERR
ERR emy@==a,b,c==> ERR
%% Class definitions for the nodes
classDef start fill:#FFF,stroke:#FFF,stroke-width:0px;
%% Apparently the node class is already used, so no ned to assign it to the
nodes
classDef node fill:#888,stroke:#FFF,stroke-width:3px;
%% Class definition for the lines
%%eb@{ curve: basis }
%%ebx@{ curve: bumpX }
%%eby@{ curve: bumpY }
%%eca@{ curve: cardinal }
%%ecr@{ curve: catmullRom }
%%emx@{ curve: monotoneX }
%%emy@{ curve: monotoneY }
%%el@{ curve: linear }
%%en@{ curve: natural }
%%es@{ curve: step }
%%esa@{ curve: stepAfter }
%%esb@{ curve: stepBefore }
```
```mermaid
stateDiagram-v2
direction LR
[*] --> A
A --> B : a
A --> A : b
A --> ERR : c
B --> B : a
B --> C : b
B --> ERR : c
C --> B : a
C --> A : b
C --> D : c
D --> E : a,b
D --> D : c
E --> E : a,b
E --> ERR : c
ERR --> ERR : a,b,c
```
Transition table:
State | a | b | c
:-----:|:---:|:---:|:---:
A |B|A|ERR
B |B|C|ERR
C |B|A|D
D |E|E|D
E |E|E|ERR
ERR |ERR|ERR|ERR
# Final
1. En base al siguiente **autómata finito deterministico**, evalua si los
siguientes strings son aceptados o no: `02`, `120210`, `012012`
$M = ($ { $A, B, C, D$ }$, $ { $0, 1, 2$ }$, \delta, A, $ { $D$ }$)$
State | 0 | 1 | 2
:-----:|:-----:|:-----:|:-----:
A |{C}|{B, C}|-
B |{A, D}|{C}|{B}
C |-|-|{D}
D |-|{A, B}|{A, C}
**SOLUTION** Derivation tree `02`
```mermaid
flowchart TD
A((A))
C((C))
D(((D)))
A ==0==> C
C ==2==> D
%% Class definitions for the nodes
classDef node fill:#888,stroke:#FF0,stroke-width:3px;
```
**SOLUTION** Derivation tree `120210`
```mermaid
flowchart TD
A0((A)) ==1==> B1((B))
A0 ==1==> C1((C))
B1 ==2==> B2((B))
C1 ==2==> ERR2((Err))
B2 ==0==> A3((A))
B2 ==0==> D3((D))
A3 ==2==> ERR3((Err))
D3 ==2==> A4((A))
D3 ==2==> C4((C))
A4 ==1==> B5((B))
A4 ==1==> C5((C))
C4 ==1==> ERR5((Err))
B5 ==0==> A6((A))
B5 ==0==> D6(((D)))
C5 ==0==> ERR6((Err))
%% Class definitions for the nodes
classDef node fill:#888,stroke:#FF0,stroke-width:3px;
```
0. Converte el anterior **autómata finito no-deterministico** en su equivalente
**deterministico**.
**SOLUTION** State diagram
```mermaid
flowchart LR
0(( ))
A((A))
B((B))
C((C))
D(((D)))
0:::start ==> A
A ==0==> C
A ==1==> B
A ==1==> C
B ==0==> A
B ==0==> D
B ==1==> C
B ==2==> B
C ==2==> D
D ==1==> A
D ==1==> B
D ==2==> A
D ==2==> C
%% Class definitions for the nodes
classDef start fill:#FFF,stroke:#FFF,stroke-width:0px;
%% Apparently the node class is already used, so no ned to assign it to the
nodes
classDef node fill:#888,stroke:#FFF,stroke-width:3px;
```
**SOLUTION** DFA
State | 0 | 1 | 2
:-----:|:-----:|:-----:|:-----:
A | C | BC | ERR
C | ERR | ERR | D
BC | AD | C | BD
D | ERR | AB | AC
AD | C | ABC | AC
BD | AD | ABC | ABC
AB | ACD | BC | B
AC | C | BC | D
ABC | ACD | BC | BD
ACD | C | ABC | ACD
B | AD | C | B
**SOLUTION** State diagram
```mermaid
flowchart LR
0(( ))
A((A))
B((B))
C((C))
D(((D)))
BC((BC))
AD(((AD)))
BD(((BD)))
AB((AB))
AC((AC))
ABC((ABC))
ACD(((ACD)))
ERR([ERR])
0:::start ==> A
A ==0==> C
A ==1==> BC
A ==2==> ERR
C ==0,1==> ERR
C ==2==> D
BC ==0==> AD
BC ==1==> C
BC ==2==> BD
D ==0==> ERR
D ==1==> AB
D ==2==> AC
AD ==0==> C
AD ==1==> ABC
AD ==2==> AC
BD ==0==> AD
BD ==1,2==> ABC
AB ==0==> ACD
AB ==1==> BC
AB ==2==> B
AC ==0==> C
AC ==1==> BC
AC ==2==> D
ABC ==0==> ACD
ABC ==1==> BC
ABC ==2==> BD
ACD ==0==> C
ACD ==1==> ABC
ACD ==2==> ACD
B ==0==> AD
B ==1==> C
B ==2==> B
%% Class definitions for the nodes
classDef start fill:#FFF,stroke:#FFF,stroke-width:0px;
%% Apparently the node class is already used, so no ned to assign it to the
nodes
classDef node fill:#888,stroke:#FFF,stroke-width:3px;
```
0. Escribe una **expresión regular** para identificar placas del DF o del estado de
méxico.
https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_M%C3%A9xico#
Nueva_denominaci%C3%B3n
**SOLUTION**
DF: antes: `\d{3}-[A-Z]{3}`, ahora: `[A-Z]-\d{3}-[A-Z]{3}`
Estados: `[A-Z]{3}-\d{3}-[A-Z]`
0. Escribe la sintaxis de la estructura **switch en C/C++** en **BNF** y **EBNF**.
**SOLUTION**
```xml
<switch> ::=
```
```bash
SWITCH ::=
