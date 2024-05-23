class PlataformaAprendizaje:
    def __init__(self):
        self.usuarios = []
        self.contenidos = []

    def registrarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminarUsuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            usuario.sesion_iniciada = False
            return True
        return False

    def verificarCredenciales(self, email, contrasena):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.contrasena == contrasena:
                return True
        return False

    def obtenerUsuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def solicitarListaContenido(self, usuario):
        if usuario.sesion_iniciada:
            return [contenido.devolverListaContenido() for contenido in self.contenidos]
        else:
            return 'Debe iniciar sesión primero'

    def mostrarListaContenido(self, usuario):
        if usuario.sesion_iniciada:
            return [contenido.devolverListaContenido() for contenido in self.contenidos]
        else:
            return 'Debe iniciar sesión primero'

    def solicitarContenido(self, usuario, contenido):
        if usuario.sesion_iniciada:
            return contenido.devolverContenido()
        else:
            return 'Debe iniciar sesión primero'

    def mostrarContenido(self, usuario, contenido):
        if usuario.sesion_iniciada:
            return contenido.devolverContenido()
        else:
            return 'Debe iniciar sesión primero'
