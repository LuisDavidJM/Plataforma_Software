import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QInputDialog, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from plataforma_aprendizaje import PlataformaAprendizaje
from profesor import Profesor
from estudiante import Estudiante
from curso_contenido import CursoContenido
from estilos import login_styles, contenido_styles, gestion_styles
from Contenido.contenido import matematicas, ciencias

class LoginWindow(QWidget):
    def __init__(self, plataforma):
        super().__init__()
        self.plataforma = plataforma
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inicio de Sesión')
        self.setGeometry(700, 400, 1500, 1000)
        self.setStyleSheet(login_styles)
        
        layout = QVBoxLayout()

        self.title = QLabel('Inicio de Sesión')
        self.title.setObjectName('title')
        layout.addWidget(self.title)

        self.email_label = QLabel('Correo:')
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QLabel('Contraseña:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton('Iniciar Sesión')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        email = self.email_input.text()
        contrasena = self.password_input.text()
        usuario = self.plataforma.obtenerUsuario(email)

        if usuario and usuario.iniciarSesion(email, contrasena, self.plataforma) == f'{usuario.nombre} ha iniciado sesión con el correo {email}':
            QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso')
            self.close()
            if isinstance(usuario, Profesor):
                self.gestion_window = GestionUsuariosWindow(self.plataforma, usuario)
                self.gestion_window.show()
            elif isinstance(usuario, Estudiante):
                self.contenido_window = ContenidoWindow(self.plataforma, usuario)
                self.contenido_window.show()
        else:
            QMessageBox.warning(self, 'Error', 'Credenciales incorrectas o usuario no registrado')


class GestionUsuariosWindow(QWidget):
    def __init__(self, plataforma, profesor):
        super().__init__()
        self.plataforma = plataforma
        self.profesor = profesor
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Usuarios')
        self.setGeometry(700, 400, 1500, 1000)
        self.setStyleSheet(contenido_styles)

        layout = QVBoxLayout()

        self.usuarios_list = QListWidget()
        self.updateUsuariosList()
        layout.addWidget(self.usuarios_list)

        self.agregar_button = QPushButton('Agregar Usuario')
        self.agregar_button.clicked.connect(self.agregarUsuario)
        layout.addWidget(self.agregar_button)

        self.eliminar_button = QPushButton('Eliminar Usuario')
        self.eliminar_button.clicked.connect(self.eliminarUsuario)
        layout.addWidget(self.eliminar_button)

        self.cerrar_sesion_button = QPushButton('Cerrar Sesión')
        self.cerrar_sesion_button.clicked.connect(self.cerrarSesion)
        layout.addWidget(self.cerrar_sesion_button)

        self.setLayout(layout)

    def updateUsuariosList(self):
        self.usuarios_list.clear()
        usuarios = self.profesor.listarUsuarios(self.plataforma)
        for nombre, email in usuarios:
            self.usuarios_list.addItem(f'{nombre} - {email}')

    def agregarUsuario(self):
        email, ok = QInputDialog.getText(self, 'Agregar Usuario', 'Ingrese el correo del nuevo usuario:')
        if ok:
            nombre, ok = QInputDialog.getText(self, 'Agregar Usuario', 'Ingrese el nombre del nuevo usuario:')
            if ok:
                contrasena, ok = QInputDialog.getText(self, 'Agregar Usuario', 'Ingrese la contraseña del nuevo usuario:')
                if ok:
                    nuevo_usuario = Estudiante(len(self.plataforma.usuarios) + 1, nombre, email, contrasena)
                    mensaje = self.profesor.agregarUsuario(nuevo_usuario, plataforma)
                    QMessageBox.information(self, 'Información', mensaje)
                    self.updateUsuariosList()

    def eliminarUsuario(self):
        email, ok = QInputDialog.getText(self, 'Eliminar Usuario', 'Ingrese el correo del usuario a eliminar:')
        if ok:
            usuario = self.plataforma.obtenerUsuario(email)
            if usuario:
                mensaje = self.profesor.eliminarUsuario(usuario, plataforma)
                QMessageBox.information(self, 'Información', mensaje)
                self.updateUsuariosList()
            else:
                QMessageBox.warning(self, 'Error', 'Usuario no encontrado')

    def cerrarSesion(self):
        self.profesor.cerrarSesion()
        QMessageBox.information(self, 'Información', 'Sesión cerrada')
        self.close()
        self.login_window = LoginWindow(self.plataforma)
        self.login_window.show()


class ContenidoWindow(QWidget):
    def __init__(self, plataforma, estudiante):
        super().__init__()
        self.plataforma = plataforma
        self.estudiante = estudiante
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Contenido')
        self.setGeometry(600, 200, 1700, 1400)
        self.setStyleSheet(gestion_styles)

        layout = QVBoxLayout()

        self.contenido_list = QListWidget()
        self.updateContenidoList()
        self.contenido_list.setFixedHeight(self.calculateListHeight())
        layout.addWidget(self.contenido_list)

        self.ver_contenido_button = QPushButton('Ver Contenido')
        self.ver_contenido_button.clicked.connect(self.verContenido)
        layout.addWidget(self.ver_contenido_button)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        self.contenido_detalle = QLabel('')
        self.contenido_detalle.setObjectName('contenido_detalle')
        self.contenido_detalle.setAlignment(Qt.AlignTop)
        self.contenido_detalle.setWordWrap(True)

        self.contenido_imagen = QLabel()
        self.contenido_imagen.setObjectName('contenido_imagen')
        self.contenido_imagen.setAlignment(Qt.AlignCenter)
        self.contenido_imagen.setWordWrap(True)

        content_layout.addWidget(self.contenido_detalle)
        content_layout.addWidget(self.contenido_imagen)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area)

        self.cerrar_sesion_button = QPushButton('Cerrar Sesión')
        self.cerrar_sesion_button.clicked.connect(self.cerrarSesion)
        layout.addWidget(self.cerrar_sesion_button)

        self.setLayout(layout)

    def updateContenidoList(self):
        self.contenido_list.clear()
        contenidos = self.plataforma.solicitarListaContenido(self.estudiante)
        if isinstance(contenidos, list):
            for contenido in contenidos:
                self.contenido_list.addItem(f'{contenido[0]}')
        self.contenido_list.setFixedHeight(self.calculateListHeight()*2)
    
    def calculateListHeight(self):
        row_count = self.contenido_list.count()
        row_height = self.contenido_list.sizeHintForRow(0)
        return row_count * row_height + 2 * self.contenido_list.frameWidth()

    def verContenido(self):
        selected_item = self.contenido_list.currentItem()
        if selected_item:
            contenido_titulo = selected_item.text()
            for contenido in self.plataforma.contenidos:
                if contenido.titulo == contenido_titulo:
                    self.contenido_detalle.setText(f'{contenido.descripcion}')
                    self.contenido_imagen.setPixmap(QPixmap(contenido.imagen))
                    break
        else:
            QMessageBox.warning(self, 'Error', 'Seleccione un contenido para ver')

    def cerrarSesion(self):
        self.estudiante.cerrarSesion()
        QMessageBox.information(self, 'Información', 'Sesión cerrada')
        self.close()
        self.login_window = LoginWindow(self.plataforma)
        self.login_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    plataforma = PlataformaAprendizaje()
    profesor = Profesor(1, 'Prof. Juan', 'juan@correo.com', '1234')
    estudiante = Estudiante(2, 'Ana', 'ana@correo.com', '5678')
    contenido1 = CursoContenido('Matemáticas', matematicas, 'Contenido/matematicas.jpg')
    contenido2 = CursoContenido('Ciencias', ciencias, 'Contenido/ciencias.jpg')

    plataforma.registrarUsuario(profesor)
    plataforma.registrarUsuario(estudiante)
    plataforma.contenidos.append(contenido1)
    plataforma.contenidos.append(contenido2)

    login_window = LoginWindow(plataforma)
    login_window.show()

    sys.exit(app.exec_())
