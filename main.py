from classes import Menu

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