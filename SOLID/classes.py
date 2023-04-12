from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, categoria, descricao, valor):
        self.categoria = categoria
        self.descricao = descricao
        self.valor=valor

    @abstractmethod
    def calc_taxa(self):
        pass

class EletronicoItem(Item):
    def calc_taxa(self):
        return self.valor * 0.5
    
class ImovelItem(Item):
    def calc_taxa(self):
        return self.valor * 0.2
    
class AlimentoItem(Item):
    def calc_taxa(self):
        return self.valor * 0.1
    
class MovelItem(Item):
    def calc_taxa(self):
        return self.valor * 0.7