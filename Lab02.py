class perro: 
    Especie="mamifero"


    __raza="Chiguagua"
    __peso=2
    __pelaje="corto"
    __color="Café"
    __genéro=""
    __camina="False"

   def __init__(self,genero,raza):
        self.__raza="Chiguagua"
        self.__peso=3
        self.__color="Café"
        self.__genero= genero
    
    def camina(self,caminar):
        self.__camina=caminar

        if self.__camina:
         return "El perro camina"

        else:
         "El perro no camino"

mi_mascota=perro("macho","Chiguagua")
print(mi_mascota.camina(True))
