class CursoContenido:
    def __init__(self, titulo, descripcion, imagen):
        self.titulo = titulo
        self.descripcion = descripcion
        self.imagen = imagen

    def devolverListaContenido(self):
        return [self.titulo, self.descripcion, self.imagen]

    def devolverContenido(self):
        return self.titulo
