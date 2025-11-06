class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.produccion = []

    def registrar_produccion(self, semana, huevos):
        for i, (s, _) in enumerate(self.produccion):
            if s == semana:
                self.produccion[i] = (semana, huevos)
                return "ok"
        self.produccion.append((semana, huevos))
        return "ok"

    def produccion_semanal(self, semana):
        for s, h in self.produccion:
            if s == semana:
                return h
        return 0

    def produccion_total(self):
        t = 0
        for _, h in self.produccion:
            t += h
        return t


class BaseDatos:
    def __init__(self):
        self.animales = []

    def buscar(self, codigo):
        for a in self.animales:
            if a.codigo == codigo:
                return a
        return None

    def crear(self, codigo, raza, edad):
        if self.buscar(codigo):
            return "ya existe"
        self.animales.append(Animal(codigo, raza, edad))
        return "creado"

    def listar(self):
        if not self.animales:
            return "sin datos"
        r = []
        for a in self.animales:
            r.append(f"{a.codigo} | {a.raza} | {a.edad} | regs:{len(a.produccion)}")
        return "\n".join(r)

    def actualizar(self, codigo, raza, edad):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        a.raza = raza
        a.edad = edad
        return "actualizado"

    def eliminar(self, codigo):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        self.animales.remove(a)
        return "eliminado"

    def reg_prod(self, codigo, semana, huevos):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        return a.registrar_produccion(semana, huevos)

    def cons_sem(self, codigo, semana):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        return a.produccion_semanal(semana)

    def cons_tot(self, codigo):
        a = self.buscar(codigo)
        if not a:
            return "no existe"
        return a.produccion_total()
