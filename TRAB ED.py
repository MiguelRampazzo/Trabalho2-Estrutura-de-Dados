from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    valor: str | int | float

@dataclass
class No:
    elemento: Item
    filhoEsq: No | None = None
    filhoDir: No | None = None

class ABB:
    def __init__(self):
        self.raiz: No | None = None

    def vazia(self):
        return self.raiz == None
     
    def insere(self, elem: Item) -> None:
        self.raiz = self.insereNo(elem, self.raiz)

    def insereNo(self, elem: Item, raiz: No) -> No | None:
        if raiz == None:
            raiz = No(elem)
        else:
            if elem.valor < raiz.elemento.valor:
                raiz.filhoEsq = self.insereNo(elem, raiz.filhoEsq)            
            elif elem.valor > raiz.elemento.valor:
                raiz.filhoDir = self.insereNo(elem, raiz.filhoDir)
        return raiz
     
    def busca(self, elem: Item) -> No | None:
        return self.buscaNo(elem, self.raiz)
    
    def buscaNo(self, elem: Item, raiz: No) -> No | None:
        if raiz != None:
            if elem.valor == raiz.elemento.valor:
                return raiz
            elif elem.valor < raiz.elemento.valor:
                return self.buscaNo(elem, raiz.filhoEsq)
            else:
                return self.buscaNo(elem, raiz.filhoDir)
        else:
            return None
    
    def remove(self, elem: Item) -> None:
        self.raiz = self._removeNo(elem, self.raiz)

    def _removeNo(self, elem: Item, raiz: No) -> No | None:
        if raiz != None:
            if elem.valor < raiz.elemento.valor:
                raiz.filhoEsq = self._removeNo(elem, raiz.filhoEsq)
            elif elem.valor > raiz.elemento.valor:
                raiz.filhoDir = self._removeNo(elem, raiz.filhoDir)
            else:
                if raiz.filhoEsq != None and raiz.filhoDir != None:
                    self._trocaSucessor(raiz)
                    raiz.filhoDir = self._removeNo(elem, raiz.filhoDir)
                else:
                    if raiz.filhoEsq != None:
                        raiz = raiz.filhoEsq
                    else:
                        raiz = raiz.filhoDir
        return raiz   
    
    def _trocaSucessor(self, no: No) -> None:
        sucessor = no.filhoDir
        while sucessor.filhoEsq != None:
            sucessor = sucessor.filhoEsq    
        no.elemento, sucessor.elemento = sucessor.elemento, no.elemento

    def exibe(self) -> None:
        self.exibeNo(self.raiz)
        print()
    
    def exibeNo(self, no: No) -> None:
        if no != None:
            print('(', end='')
            self.exibeNo(no.filhoEsq)
            print(' ', no.elemento.valor, ' ', end='')
            self.exibeNo(no.filhoDir)
            print(')', end='')

    def k_esimo_maior(self, k: int) -> Item | None:
        """
        Retorna o k-ésimo maior elemento da árvore.
        """
        
        contador = 0

        def _percorre(no: No, k: int, contador: int) -> tuple[Item | None, int]:
            if no == None:
                return None, contador
            
            resultado, contador = _percorre(no.filhoDir, k, contador)
            

            if resultado != None:
                return resultado, contador
            
            contador += 1
            if contador == k:
                return no.elemento, contador
            
            return _percorre(no.filhoEsq, k, contador)

        resultado, _ = _percorre(self.raiz, k, contador)
        return resultado



arvore = ABB()

elementos = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 9, 11, 14, 17, 20]
for item in elementos:
    arvore.insere(Item(item))
arvore.exibe()

print(arvore.k_esimo_maior(13))
