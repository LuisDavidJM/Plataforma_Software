from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, id, nombre, email, contrasena):
        super().__init__(id, nombre, email, contrasena, acceso_gestion=False)

    def solicitarContenido(self, cursoContenido):
        if self.sesion_iniciada:
            return cursoContenido.devolverContenido()
        else:
            return 'Debe iniciar sesión primero'

    def seleccionarContenido(self, cursoContenido):
        if self.sesion_iniciada:
            contenido = self.solicitarContenido(cursoContenido)
            return contenido
        else:
            return 'Debe iniciar sesión primero'
