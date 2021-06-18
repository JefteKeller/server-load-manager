# **_Simulador de Carga de Servidores_**

## Sobre

> ---
>
> Esta é uma aplicação em Python que gerencia uma simulação de _Criação_, _Alocação_, _Registro de Tarefas_, e _Otimização de utilização de Servidores_.
>
> ---

O script precisa de um arquivo nomeado: `input.txt`, que deve estar localizado na mesma pasta (nível) do `main.py`, com os seguintes parâmetros:

> ---
>
> -   _Primeira Linha_
> -   -   Deve conter o valor de `ttask` (número de ciclo que a tarega leva para ser ﬁnalizada).
> -   _Segunda Linha_
> -   -   Deve conter o valor de `umax` (Máximo de usuários registrados simultaneamente nos servidores).
> -   _Demais Linhas_ devem conter o número de novos usuários para cada ciclo.
>
> ---

O arquivo de saída contendo os _Logs_ de utilização e custos de Servidor é gerado automaticamente com o nome de `output.txt` na mesma pasta em que o script se encontra.

## Utilização

> ---

Já com o arquivo de `input.txt` na raiz do projeto e tendo o Python na versão 3 instalado, execute o seguinte comando em um _Terminal_:

```Shell

python3 main.py

```

O script irá realizar a simulação e gerar o arquivo `output.txt`, contendo os registros de utilização e carga dos servidores por ciclo. <br/>

> ---
>
> A última linha do arquivo conterá os custos estimados de utilização dos servidores para acomodar a demanda de Tarefas.
>
> ---

## Testes

> ---

Para executar os testes da aplicação execute o seguinte código em um _Terminal_:

```Shell

python3 -m unittest

```

Para obter um relatório mais detalhado sobre os testes adicione o parâmetro `-v`:

```Shell

python3 -m unittest -v

```
