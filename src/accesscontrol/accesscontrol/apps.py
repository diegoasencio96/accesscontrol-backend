from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu = (
        ParentItem(
            'Usuarios', children=[
                #ChildItem('Usuarios del sistema', 'users.user'),
                ChildItem('Perfiles de usuarios', 'users.profile'),
                #ChildItem('Grupo de usuarios', 'auth.group'),
            ], icon='fa fa-users'
        ),
        ParentItem(
            'Ingreso', children=[
                ChildItem('Aperturas de la puerta', 'locks.dooropening')
            ], icon='fa fa-unlock'
        ),
        ParentItem(
            'Configuraciones', children=[
                ChildItem('Configuración general', 'configurations.general'),
                ChildItem('Empresas', 'configurations.entity'),
            ], icon='fa fa-cog fa-spin'
        ),
        ParentItem(
            'Créditos', children=[
                ChildItem('Sitio web', url='http://diegoasencio.co', target_blank=True),
            ], icon='fa fa-connectdevelop fa-spin'
        ),
    )
