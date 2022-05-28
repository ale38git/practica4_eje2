from datetime import datetime as dt
#datetime.today().strftime('%Y-%m-%d %H:%M')
#2021-03-09 15:05

#datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
#Tuesday, March 09, 2021 15:05:55

class Empleado():
    """
    Clase que representa un empleado

    ...

    Atributos:

    e_type : str
        Tipo de empleado
    NIF : str
        NIF del empleado
    name : str
        Nombre del empleado
    birthday : str
        Fecha de nacimiento del empleado
    salary_monthly : float
        Salario mensual del empleado

    Metodos:

    actual_salary()
        Devuelve el salario actual del empleado
    is_birthday()
        Devuelve True si el empleado esta de 
        cumpleaños un mes especifico  
    """

    def  __init__(self,e_type = '', NIF='12345678X', name='', birthday='dd/mm/yyyy', salary_monthly=0,*arg,**kwarg):
        """
        Parametros:

        e_type : str
            Tipo de empleado
        NIF : str
            NIF del empleado
        name : str
            Nombre del empleado
        birthday : str
            Fecha de nacimiento del empleado
        salary_monthly : float
            Salario mensual del empleado
        """

        self.e_type = e_type
        self.NIF = NIF.upper()
        self.name = name
        self.birthday = birthday
        self.salary_monthly = salary_monthly
    
    #Definicion del calculo de salario (Salario Base) de la clase Empleado
    def actual_salary(self):
        """Devuelve el salario actual del empleado"""
        return self.salary_monthly

    #Define si un empleado está de cumpleaños en un mes dado(por defecto coge el mes actual proporcionado por el S.O.)
    def is_birthday(self,month=dt.today().strftime('%m')):
        """Devuelve si el empleado esta de cumpleaños ese mes
        Si el argumento month no se pasa como parametro, toma el mes actual del sistema

        Parametros:
        month : str, (opcional)
            El mes en el que se desea comprobar si esta de cumpleaños el empleado
        """

        if int(month) == int(self.birthday.split('/')[1]):    #dividimos la cadena por separador '/' y nos quedamos con la 2da(trabajamos con enteros para que 01 sea = a 1)
            return True
        else:
            return False
    #Define como se comporta el operador str para la clase Empleado (Clase Padre)
    def __str__(self):
        return str(f"{'NIF:':20}{self.NIF}\n{'Nombre:':20}{self.name}\n{'Cumpleaños:':20}{self.birthday}\n{'Tipo: ':20}{self.e_type}\n{'Sueldo Base:':20}{self.salary_monthly}")       

class EmpleadoFijo(Empleado):
    """
    Clase que representa un empleado fijo, hereda de la clase Empleado

    ...

    Atributos Propios:

    beginning_year : str
        Año de inicio en la empresa del empleado
    annual_supp : float
        Suplemento anual del empleado
    
    Atributos Heredados:

    e_type : str
        Tipo de empleado
    NIF : str
        NIF del empleado
    name : str
        Nombre del empleado
    birthday : str
        Fecha de nacimiento del empleado
    salary_monthly : float
        Salario mensual del empleado

    Metodos:

    actual_salary()
        Devuelve el salario actual del empleado   
    is_birthday()
        Devuelve True si el empleado esta de 
        cumpleaños un mes especifico 
    """

    def __init__(self, *arg, beginning_year='yyyy', annual_supp=0, **kwarg):
        """
        Parametros:

        e_type : str
            Tipo de empleado
        NIF : str
            NIF del empleado
        name : str
            Nombre del empleado
        birthday : str
            Fecha de nacimiento del empleado
        salary_monthly : float
            Salario mensual del empleado
        beginning_year : str
            Año de inicio en la empresa del empleado
        annual_supp : float
            Suplemento anual del empleado
        """

        super().__init__(*arg, **kwarg)
        self.beginning_year = beginning_year
        self.annual_supp = annual_supp
    #Definicion del cálculo del salario mensual de la clase EmpleadoFijo(Difiere de la heredada del padre)
    def actual_salary(self):
        """Devuelve el salario actual del empleado
        
        Calcula el salario actual en base a la antiguedad del empleado
        en la empresa, el salario mensual y el complemento anual
        """

        actual_year = int(dt.today().strftime('%Y'))
        return super().actual_salary() + (actual_year-int(self.beginning_year))*self.annual_supp/12

    #Define como se comporta el operador str para la clase EmpleadoFijo
    def __str__(self):
        return super().__str__() + str(f"\n{'Año de Alta:':20}{self.beginning_year} \n{'Complemento Anual:':20}{self.annual_supp}\n{'Salario mensual:':20}{self.actual_salary():.2f}")
 
class EmpleadoTemp(Empleado):
    """
    Clase que representa un empleado temperal, hereda de la clase Empleado

    ...

    Atributos Propios:

    beginning_date : str
        Fecha de inicio del contrato del empleado
    termination_date : str
        Fecha de finalizacion del contrato del empleado
    
    Atributos Heredados:

    e_type : str
        Tipo de empleado
    NIF : str
        NIF del empleado
    name : str
        Nombre del empleado
    birthday : str
        Fecha de nacimiento del empleado
    salary_monthly : float
        Salario mensual del empleado

    Metodos:

    actual_salary()
        Devuelve el salario actual del empleado   
    is_birthday()
        Devuelve True si el empleado esta de 
        cumpleaños un mes especifico 
    """

    #Constructor de la clase EmpleadoTemp
    def __init__(self, *arg, beginning_date='dd/mm/aaaa', termination_date='dd/mm/aaaa',**kwarg):
        """
        Parametros:

        e_type : str
            Tipo de empleado
        NIF : str
            NIF del empleado
        name : str
            Nombre del empleado
        birthday : str
            Fecha de nacimiento del empleado
        salary_monthly : float
            Salario mensual del empleado
        beginning_year : str
            Año de inicio en la empresa del empleado
        annual_supp : float
            Suplemento anual del empleado
        beginning_date : str
            Fecha de inicio del contrato del empleado
        termination_date : str
            Fecha de finalizacion del contrato del empleado
        """

        super().__init__(*arg, *kwarg)
        self.beginning_date = beginning_date
        self.termination_date = termination_date
    
    #Define como se comporta el operador str para la clase EmpleadoTemp
    def __str__(self):
        return super().__str__() + str(f"\n{'Fecha de Alta:':20}{self.beginning_date} \n{'Fecha de Baja:':20}{self.termination_date}\n{'Salario mensual:':20}{self.actual_salary():.2f}")

#Añade un empleado al diccionario
def add_employee(db_user):
    """Funcion que añade un empleado nuevo
    
    Añade un empleado al diccionario pasado como parametro, se le
    preguntan los datos del nuevo empleado al usuario, asi como el
    tipo de contrato

    Parametros
    db_user : dic
        Base de datos(diccionario) con los empleados actuales

    Returns
    db_user : dic
        Base de datos actualizada
    """

    type_employee = input("Introduce los datos del empleado\nTipo de empleado (fijo/temporal): ").lower()
    while not (type_employee == 'fijo' or type_employee == 'temporal'):
        print("El tipo de empleado no es válido, solo admite (fijo o temporal)")
        type_employee = input("Introduce los datos del empleado\nTipo de empleado (fijo/temporal): ").lower()
    
    if type_employee=='fijo':
        employee = EmpleadoFijo('Fijo')
    elif type_employee == 'temporal':
        employee = EmpleadoTemp('Temporal')        

    employee.name = input("Introduce el nombre: ")
    employee.NIF = input("Introduce el NIF: ").upper()
    if employee.NIF in db_user:
        print(f" El NIF no. {employee.NIF} ya se encuentra en la base de datos como empleado {employee.e_type}")
        print("Si quieres cambiar su tipo de contrato, elimínalo y agregalo nuevamente con el nuevo tipo de contrato")
        return db_user
    employee.birthday = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")
    employee.salary_monthly = int(input("Introduce el sueldo base mensual: "))

    if type_employee=='fijo':
        employee.beginning_year = input("Introduce el año de alta en la empresa: ")
        employee.annual_supp = int(input("Introduce el complemento anual: "))
    elif type_employee == 'temporal':
        employee.beginning_date = input("Introduce la fecha de inicio del contrato (dd/mm/aaaa): ")
        employee.termination_date = input("Introduce la fecha de fin del contrato (dd/mm/aaaa): ")
    db_user.update({employee.NIF:employee})
    return db_user

#Elimina un empleado del diccionario
def del_employee(db_user):
    """Elimina un empleado de la base de datos
    
    Para eliminar el empleado se le pide al usuario el NIF del
    empleado que se desea eliminar, y luego lo borra del diccionario
    pasado como parametro

    Parametros
    db_user : dic
        Base de datos(diccionario) con los empleados actuales

    Returns
    db_user : dic
        Base de datos actualizada
    """

    key = input("Introduce el NIF del empleado que desea eliminar: ").upper()
    if key in db_user:
        print(f"{db_user[key].name} con NIF: {key} ha sido eliminado de su base de datos")
        del db_user[key]
    else:
        print(f"{key} no concuerda con ningun empleado en la base de datos")
    return db_user

#Muestra los empleados almacenados en el diccionario
def show_staff(db_user):
    """Muestra los empleados de la base de datos

    Parametros
    db_user : dic
        Base de datos(diccionario) con los empleados actuales
    """

    if not db_user:
        print("Su base de datos de empleados está vacía")
    else:
        print("Lista del personal de la empresa :\n")
        for key, val in db_user.items():
            print(f"{key:15} {val.name:30} {val.e_type}")

#Muestra los detalles de un empleado
def emp_details(db_user):
    """Imprime los datos de un empleado de la base de datos
    
    Para imprimir los datos del empleado se le pide al usuario el NIF del
    empleado que se desea conocer sus datos, y luego lo busca en el diccionario
    pasado como parametro. Si no existe o la base de datos esta vacia, se muestra
    un mensaje en pantalla

    Parametros
    db_user : dic
        Base de datos(diccionario) con los empleados actuales
    """

    key = input("Introduce el NIF del empleado (Intro para salir): ").upper()
    while not key in db_user:
        if not db_user:
            print("Su base de datos de empleados está vacía")
            return None
        elif key =='':
            return None
        key = input("El NIF introducido no corresponde a ningún empleado de la empresa\nIntroduce un NIF válido (Intro para salir): ").upper()
    print()
    print(db_user[key])

#Ejecuta la busqueda de empleados de cumpleaños
def emps_birthday(db_user):
    """Busca los empleados que estan de cumpleaños un mes especifico
    
    Se le pide al usuario que introduzca el mes y se imprimen
    todos los empleados de la base de datos pasada como parametro
    que esten de cumpleaños.

    Parametros
    db_user : dic
        Base de datos(diccionario) con los empleados actuales
    """

    month = input("Introduce el mes que desea ver los empleados de cumpleaños(1-12) (Intro para mostrar los del mes actual): ")
    print()
    anyone = False
    for emp in db_user.values():
        if not month:
            if emp.is_birthday():
                print(f"{emp.name:30} {emp.birthday}")
                anyone =True
        else:
            if emp.is_birthday(month):
                print(f"{emp.name:30} {emp.birthday}")
                anyone =True
    if not anyone:
        print("No existe nadie de cumpleaños en este mes")

#Ejecuta el menu de opciones
def Menu(db_user):
    """Ejecuta el menu de la aplicacion
    
    Se le pasa como parametro la base de datos de la empresa
    y se encarga del flujo de la aplicacion

    Parametros
    db_user : dic
        Base de datos(diccionario) con los empleados actuales
    """

    print("Menú de opciones:\n\n(1) Añadir empleado\n(2) Eliminar empleado \n(3) Mostrar lista de empleados\n(4) Mostrar detalle de un empleado")
    print("(5) Mostrar empleados de cumpleaños\n(6) Terminar\n")
    x = input("Elige una opción: ")
    print()
    
    if   x=='1':
            db_user = add_employee(db_user)
    elif x=='2':
            db_user = del_employee(db_user)
    elif x=='3':
            show_staff(db_user)
    elif x=='4':
            emp_details(db_user)
    elif x=='5':
            emps_birthday(db_user)
    elif x=='6':
            return True
    else:
            print("La opción introducida no es válida")
