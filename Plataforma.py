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
            self.sesion_iniciada = True
            print(f'{self.nombre} ha iniciado sesión con el correo {self.email}')
        else:
            print('Credenciales incorrectas')

    def cerrarSesion(self):
        if self.sesion_iniciada:
            self.sesion_iniciada = False
            print(f'{self.nombre} ha cerrado sesión')
        else:
            print('No hay sesión iniciada para cerrar')


class Estudiante(Usuario):
    def __init__(self, id, nombre, email, contrasena):
        super().__init__(id, nombre, email, contrasena, acceso_gestion=False)

    def solicitarContenido(self, cursoContenido):
        if self.sesion_iniciada:
            print(f'El estudiante {self.nombre} solicita contenido: {cursoContenido.titulo}')
            return cursoContenido.devolverContenido()
        else:
            print('Debe iniciar sesión primero')

    def seleccionarContenido(self, cursoContenido):
        if self.sesion_iniciada:
            contenido = self.solicitarContenido(cursoContenido)
            print(f'El estudiante {self.nombre} selecciona el contenido: {contenido}')
        else:
            print('Debe iniciar sesión primero')


class Profesor(Usuario):
    def __init__(self, id, nombre, email, contrasena):
        super().__init__(id, nombre, email, contrasena, acceso_gestion=True)
        self.usuarios = []

    def gestionarUsuarios(self):
        if self.sesion_iniciada:
            print(f'El profesor {self.nombre} gestiona usuarios')
            self.mostrarUsuarios()
        else:
            print('Debe iniciar sesión primero')

    def agregarUsuario(self, usuario):
        if self.sesion_iniciada:
            self.usuarios.append(usuario)
            print(f'Usuario {usuario.nombre} agregado.')
        else:
            print('Debe iniciar sesión primero')

    def listarUsuarios(self):
        if self.sesion_iniciada:
            print('Lista de usuarios:')
            for usuario in self.usuarios:
                print(f'Usuario: {usuario.nombre}, Email: {usuario.email}')
        else:
            print('Debe iniciar sesión primero')

    def eliminarUsuario(self, usuario):
        if self.sesion_iniciada:
            self.usuarios.remove(usuario)
            print(f'Usuario {usuario.nombre} eliminado.')
        else:
            print('Debe iniciar sesión primero')


class CursoContenido:
    def __init__(self, titulo, descripcion, imagen):
        self.titulo = titulo
        self.descripcion = descripcion
        self.imagen = imagen

    def devolverListaContenido(self):
        print(f'Lista de contenidos: {self.titulo}, {self.descripcion}, {self.imagen}')
        return [self.titulo, self.descripcion, self.imagen]

    def devolverContenido(self):
        print(f'Devolviendo contenido: {self.titulo}')
        return self.titulo


class GestionUsuarios:
    def confirmacionCreacion(self, usuario):
        print(f'Confirmación de creación del usuario {usuario.nombre}')

    def mostrarUsuarios(self, profesor):
        profesor.listarUsuarios()

    def confirmacionEliminacion(self, usuario):
        print(f'Confirmación de eliminación del usuario {usuario.nombre}')


class PlataformaAprendizaje:
    def __init__(self):
        self.usuarios = []
        self.contenidos = []

    def solicitarListaContenido(self, usuario):
        if usuario.sesion_iniciada:
            for contenido in self.contenidos:
                contenido.devolverListaContenido()
        else:
            print('Debe iniciar sesión primero')

    def mostrarListaContenido(self, usuario):
        if usuario.sesion_iniciada:
            for contenido in self.contenidos:
                print(contenido.devolverListaContenido())
        else:
            print('Debe iniciar sesión primero')

    def solicitarContenido(self, usuario, contenido):
        if usuario.sesion_iniciada:
            return contenido.devolverContenido()
        else:
            print('Debe iniciar sesión primero')

    def mostrarContenido(self, usuario, contenido):
        if usuario.sesion_iniciada:
            print(contenido.devolverContenido())
        else:
            print('Debe iniciar sesión primero')

    def verificarCredenciales(self, email, contrasena):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.contrasena == contrasena:
                return True
        return False


# Ejemplo de uso
plataforma = PlataformaAprendizaje()
profesor = Profesor(1, 'Prof. Juan', 'juan@correo.com', '1234')
estudiante = Estudiante(2, 'Ana', 'ana@correo.com', '5678')
contenido = CursoContenido('Matemáticas', 'Álgebra básica', 'imagen.png')

plataforma.usuarios.append(profesor)
plataforma.usuarios.append(estudiante)
plataforma.contenidos.append(contenido)

# Inicio de sesión
profesor.iniciarSesion('juan@correo.com', '1234', plataforma)
estudiante.iniciarSesion('ana@correo.com', '5678', plataforma)

# Gestión de usuarios y acceso a contenido después de iniciar sesión
profesor.agregarUsuario(estudiante)
profesor.listarUsuarios()
profesor.eliminarUsuario(estudiante)

estudiante.solicitarContenido(contenido)
estudiante.seleccionarContenido(contenido)

# Cerrar sesión
profesor.cerrarSesion()
estudiante.cerrarSesion()

estudiante.solicitarContenido(contenido)
estudiante.seleccionarContenido(contenido)