from abc import ABC, abstractmethod

# Clase base abstracta
class Membresia(ABC):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        self._correo_suscriptor = correo_suscriptor
        self._numero_tarjeta = numero_tarjeta

    @property
    def correo_suscriptor(self):
        return self._correo_suscriptor

    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia):
        pass

    # Método protegido reutilizable para generar una nueva membresía
    def _crear_nueva_membresia(self, nueva_membresia):
        if nueva_membresia == 1:
            return Basico(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

# Mixin para permitir cancelación a membresía Gratis
class Cancelable:
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

# Mixin para membresías con 7 días de regalo
class ConDiasDeRegalo:
    def __init__(self, correo_suscriptor, numero_tarjeta):
        self._dias_regalo = 7

    @property
    def dias_regalo(self):
        return self._dias_regalo

# Mixin para membresías con 15 días de regalo
class ConDiasDeRegaloExtendido:
    def __init__(self, correo_suscriptor, numero_tarjeta):
        self._dias_regalo = 15

    @property
    def dias_regalo(self):
        return self._dias_regalo

# Mixin para control parental (declarado pero sin lógica)
class ConControlParental:
    def modificar_control_parental(self):
        pass

# Mixin para contenido sin conexión (declarado pero sin lógica)
class ConContenidoOffline:
    def incrementar_contenido_offline(self):
        pass

# Membresía Gratis
class Gratis(Membresia):
    costo = 0
    dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

# Membresía Básica
class Basico(Membresia, Cancelable):
    costo = 3000
    dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [2, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

# Membresía Familiar
class Familiar(Membresia, Cancelable, ConDiasDeRegalo, ConControlParental):
    costo = 5000
    dispositivos = 5

    def __init__(self, correo_suscriptor, numero_tarjeta):
        Membresia.__init__(self, correo_suscriptor, numero_tarjeta)
        ConDiasDeRegalo.__init__(self, correo_suscriptor, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

# Membresía Sin Conexión
class SinConexion(Membresia, Cancelable, ConDiasDeRegalo, ConContenidoOffline):
    costo = 3500
    dispositivos = 2

    def __init__(self, correo_suscriptor, numero_tarjeta):
        Membresia.__init__(self, correo_suscriptor, numero_tarjeta)
        ConDiasDeRegalo.__init__(self, correo_suscriptor, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

# Membresía Pro
class Pro(Membresia, Cancelable, ConDiasDeRegaloExtendido, ConControlParental, ConContenidoOffline):
    costo = 7000
    dispositivos = 6

    def __init__(self, correo_suscriptor, numero_tarjeta):
        Membresia.__init__(self, correo_suscriptor, numero_tarjeta)
        ConDiasDeRegaloExtendido.__init__(self, correo_suscriptor, numero_tarjeta)

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 3]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self
