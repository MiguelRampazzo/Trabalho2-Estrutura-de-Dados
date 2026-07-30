TRAB ED.py: Implementação principal das estruturas de dados de Árvore Binária de Busca (ABB) e Árvore AVL. Contém as classes de nós e os algoritmos de inserção, busca, remoção e percursos (pré-ordem, em-ordem e pós-ordem).

teste.py: Módulo de testes e experimentos de interface gráfica (criado com tkinter) para visualização interativa do balanceamento e rotações da árvore AVL.

EspecificacaoSegundoTrabalho.pdf: Documento com os requisitos do trabalho, detalhando as assinaturas dos métodos exigidos e as regras de implementação.
Explicação Geral do Projeto

Este projeto consiste no desenvolvimento e na simulação de Árvores Binárias de Busca (ABB) e Árvores Autobalanceadas (AVL) em Python para a disciplina de Estrutura de Dados:
Árvore Binária de Busca (ABB):
Organiza os dados em uma estrutura hierárquica onde elementos menores que a raiz ficam na subárvore esquerda e elementos maiores ficam na subárvore direita.
Suporta operações fundamentais: inserção, busca de nós, remoção com troca por sucessor/antecessor e percursos organizados

Balanceamento AVL:
Garante que a diferença de altura entre a subárvore esquerda e a subárvore direita de qualquer nó (fator de balanceamento) seja de no máximo 1.
Implementa rotações simples (à esquerda e à direita) e rotações duplas para manter a árvore balanceada, otimizando o tempo de busca para $O(\log n)$.

Visualização Gráfica (teste.py):Utilitário desenvolvido com a biblioteca tkinter para renderizar visualmente a árvore na tela, permitindo observar as rotações e o rebalanceamento dinâmico à medida que novos valores são inseridos.
