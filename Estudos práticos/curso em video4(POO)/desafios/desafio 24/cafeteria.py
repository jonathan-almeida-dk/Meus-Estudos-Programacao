# Simule uma cafetria orientada aobjetos

# BebidaQuente        <----- {abstract}
    # + preparar()
    # + ferver_agua()      
    # + misturar()    <----- {abstract}
    # + servir()      <----- {abstract}

# Cafe
    # + misturar()
    # + servir()

# Cha
    # + misturar()
    # + servir()
    
# Leite
    # + misturar()
    # + servir()

from abc import ABC, abstractmethod
# =====================================

class BebidaQuente:
    def __init__(self,bebida):
        self.nome = bebida

    def preparar(self):
        pass

    def misturar(self):
        pass
    
    @abstractmethod
    def misturar(self):
        pass

    def servir(self):
        pass

# =====================================

class Cafe(BebidaQuente):
    def misturar(self):
        pass

    def servir(self):
        pass

# =================================

class Cha(BebidaQuente):
    def misturar(self):
        pass

    def servir(self):
        pass
# =================================

class Leite(BebidaQuente):
    def misturar(self):
        pass

    def servir(self):
        pass