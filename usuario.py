class Usuario:
    def __init__(self, id, nombre, email, contrasena, acceso_gestion):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contrasena = contrasena
        self.acceso_gestion = acceso_gestion
        self.sesion_iniciada = False

    def iniciarSesion(self, email, contrasena, plataforma):
        if plataforma.verificarCredenciales(email, contrasena):
            if plataforma.obtenerUsuario(email) == self:
                self.sesion_iniciada = True
                return f'{self.nombre} ha iniciado sesión con el correo {self.email}'
            else:
                return 'Usuario no registrado'
        else:
            return 'Credenciales incorrectas'

    def cerrarSesion(self):
        if self.sesion_iniciada:
            self.sesion_iniciada = False
            return f'{self.nombre} ha cerrado sesión'
        else:
            return 'No hay sesión iniciada para cerrar'
