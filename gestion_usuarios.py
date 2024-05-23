class GestionUsuarios:
    def confirmacionCreacion(self, usuario):
        return f'Confirmación de creación del usuario {usuario.nombre}'

    def mostrarUsuarios(self, profesor, plataforma):
        return profesor.listarUsuarios(plataforma)

    def confirmacionEliminacion(self, usuario):
        return f'Confirmación de eliminación del usuario {usuario.nombre}'
