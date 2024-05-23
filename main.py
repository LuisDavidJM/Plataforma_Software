from plataforma_aprendizaje import PlataformaAprendizaje
from profesor import Profesor
from estudiante import Estudiante
from curso_contenido import CursoContenido

plataforma = PlataformaAprendizaje()
profesor = Profesor(1, 'Prof. Juan', 'juan@correo.com', '1234')
estudiante = Estudiante(2, 'Ana', 'ana@correo.com', '5678')
contenido = CursoContenido('Matemáticas', 'Álgebra básica', 'imagen.png')

# Registrar usuarios
plataforma.registrarUsuario(profesor)
plataforma.registrarUsuario(estudiante)
plataforma.contenidos.append(contenido)

# Inicio de sesión
print(profesor.iniciarSesion('juan@correo.com', '1234', plataforma))
print(estudiante.iniciarSesion('ana@correo.com', '5678', plataforma))

# Gestión de usuarios y acceso a contenido después de iniciar sesión
print(profesor.agregarUsuario(estudiante, plataforma))
print(profesor.listarUsuarios(plataforma))
print(profesor.eliminarUsuario(estudiante, plataforma))

# Intento de acceso a contenido después de eliminar usuario
print(estudiante.solicitarContenido(contenido))
print(estudiante.seleccionarContenido(contenido))

# Cerrar sesión
print(profesor.cerrarSesion())
print(estudiante.cerrarSesion())
