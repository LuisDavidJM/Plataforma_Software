from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, id, nombre, email, contrasena):
        super().__init__(id, nombre, email, contrasena, acceso_gestion=True)

    def gestionarUsuarios(self, plataforma):
        if self.sesion_iniciada:
            return self.listarUsuarios(plataforma)
        else:
            return 'Debe iniciar sesión primero'

    def agregarUsuario(self, usuario, plataforma):
        if self.sesion_iniciada:
            plataforma.registrarUsuario(usuario)
            return f'Usuario {usuario.nombre} agregado.'
        else:
            return 'Debe iniciar sesión primero'

    def listarUsuarios(self, plataforma):
        if self.sesion_iniciada:
            return [(usuario.nombre, usuario.email) for usuario in plataforma.usuarios]
        else:
            return 'Debe iniciar sesión primero'

    def eliminarUsuario(self, usuario, plataforma):
        if self.sesion_iniciada:
            if plataforma.eliminarUsuario(usuario):
                return f'Usuario {usuario.nombre} eliminado.'
            else:
                return 'Usuario no encontrado.'
        else:
            return 'Debe iniciar sesión primero'
