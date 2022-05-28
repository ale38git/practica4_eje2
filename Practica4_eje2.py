from datetime import datetime as dt
#datetime.today().strftime('%Y-%m-%d %H:%M')
#2021-03-09 15:05

#datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')
#Tuesday, March 09, 2021 15:05:55

class Empleado():
    #Constructor de la clase Empleado
    def  __init__(self,e_type = '', NIF='12345678X', name='', birthday='dd/mm/yyyy', salary_monthly=0,*arg,**kwarg):
        self.e_type = e_type
        self.NIF = NIF.upper()
        self.name = name
        self.birthday = birthday
        self.salary_monthly = salary_monthly
    
    #Definicion del calculo de salario (Salario Base) de la clase Empleado
    def actual_salary(self):
        return self.salary_monthly

    #Define si un empleado está de cumpleaños en un mes dado(por defecto coge el mes actual proporcionado por el S.O.)
    def is_birthday(self,month=dt.today().strftime('%m')):
        if int(month) == int(self.birthday.split('/')[1]):    #dividimos la cadena por separador '/' y nos quedamos con la 2da(trabajamos con enteros para que 01 sea = a 1)
            return True
        else:
            return False
    #Define como se comporta el operador str para la clase Empleado (Clase Padre)
    def __str__(self):
        return str(f"{'NIF:':20}{self.NIF}\n{'Nombre:':20}{self.name}\n{'Cumpleaños:':20}{self.birthday}\n{'Tipo: ':20}{self.e_type}\n{'Sueldo Base:':20}{self.salary_monthly}")       

class EmpleadoFijo(Empleado):
    #Constructor de la clase EmpleadoFijo
    def __init__(self, *arg, beginning_year='yyyy', annual_supp=0, **kwarg):
        super().__init__(*arg, **kwarg)
        self.beginning_year = beginning_year
        self.annual_supp = annual_supp
    #Definicion del cálculo del salario mensual de la clase EmpleadoFijo(Difiere de la heredada del padre)
    def actual_salary(self):
        actual_year = int(dt.today().strftime('%Y'))
        return super().actual_salary() + (actual_year-int(self.beginning_year))*self.annual_supp/12

    #Define como se comporta el operador str para la clase EmpleadoFijo
    def __str__(self):
        return super().__str__() + str(f"\n{'Año de Alta:':20}{self.beginning_year} \n{'Complemento Anual:':20}{self.annual_supp}\n{'Salario mensual:':20}{self.actual_salary():.2f}")
 
class EmpleadoTemp(Empleado):
    #Constructor de la clase EmpleadoTemp
    def __init__(self, *arg, beginning_date='dd/mm/aaaa', termination_date='dd/mm/aaaa',**kwarg):
        super().__init__(*arg, *kwarg)
        self.beginning_date = beginning_date
        self.termination_date = termination_date
    
    #Define como se comporta el operador str para la clase EmpleadoTemp
    def __str__(self):
        return super().__str__() + str(f"\n{'Fecha de Alta:':20}{self.beginning_date} \n{'Fecha de Baja:':20}{self.termination_date}\n{'Salario mensual:':20}{self.actual_salary():.2f}")

#Añade un empleado al diccionario
def add_employee(db_user):
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
    key = input("Introduce el NIF del empleado que desea eliminar: ").upper()
    if key in db_user:
        print(f"{db_user[key].name} con NIF: {key} ha sido eliminado de su base de datos")
        del db_user[key]
    else:
        print(f"{key} no concuerda con ningun empleado en la base de datos")
    return db_user

#Muestra los empleados almacenados en el diccionario
def show_staff(db_user):
    if not db_user:
        print("Su base de datos de empleados está vacía")
    else:
        print("Lista del personal de la empresa :\n")
        for key, val in db_user.items():
            print(f"{key:15} {val.name:30} {val.e_type}")

#Muestra los detalles de un empleado
def emp_details(db_user):
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


if __name__ =="__main__":
        #Se empieza con un diccionario con elementos para depurar más rapido el código
    db_staff = {}
    '''
            "00000001X": EmpleadoFijo('Fijo', '00000001X', 'Alejandro González Norat',  salary_monthly=2000, birthday='04/12/1994', beginning_year='2011',annual_supp=200),
            "00000002X": EmpleadoFijo('Fijo', '00000002X', 'Roberto Martínez Martínez', '14/03/1994', 1000, beginning_year='2001', annual_supp=200),       
            "00000003X": EmpleadoTemp('Temporal', '00000003X', 'Panchito Gómez Pérez', '04/03/1994', 2000, beginning_date='15/1/2022', termination_date='15/1/2023'),
            "00000004X": EmpleadoTemp('Temporal', '00000004X', 'Armando Mesas Rojas', '14/12/1994', 1000, beginning_date='15/1/2022', termination_date='15/1/2024')
           ''' 

    #me quedo ejecutando la funcion mientras no termine el usuario(se encuesta el retorno de la funcion hasta que sea verdadero)
    while not Menu(db_staff):
        print("")
