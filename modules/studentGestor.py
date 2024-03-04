from tabulate import tabulate

students  = {
    'id':'',
    'nombre':'',
    'edad':'',
    'email':'',
    'calificaciones':{
        'parciales':[],
        'quices':[],
        'trabajos':[]
    }
}
def addstudent(students:dict):
    id = input('ingrese el id: ')
    nombre = input('ingrese el nombre: ')
    edad = input(f'ingrese la edad de {nombre}: ')
    email = input(f'ingrese el email de {nombre}: ')
    student = {
        'id':id,
        'nombre':nombre,
        'edad':edad,
        'emai':email
    }
    students.update({str(len(students)+1).zfill(4):student})
    print(student)
    
def searchStudent(students: dict):
    print(students)
    id = input('Ingrese el Id del estudiante: ')
    dta = students.get(id,False)
    if(type(dta) == dict):
            print(dta)
    if((type(dta) == bool) and (dta == False)):        
        print('el estudiante no se encunetra registrado')
        
def listData(students: dict):
    info = []
    for key,value in students.items():
        info.append(value)
    print(tabulate(info, headers='keys',tablefmt='grid'))
    
def validStudent(students: dict,id) -> bool:
    return bool(students.get(id,''))

def delStudent(students: dict):
    id = input('ingrese Nro Id del estudiante: ')
    if (validStudent(students,id)):
        students.pop(id)
    else:
        print(f'El estudiante con id {id} no esta registrado')
        
def delByName(students: dict):
    nombre = input('ingrese Nro id del estudiante: ')
    for llave,valor in students.items():
        if (nombre in valor['nombre']):
            students.pop(llave)
            break
        
def addGrades(students: dict):

    for student_id, student_info in students.items():
        print(f"Ingrese las calificaciones para el estudiante con ID {student_info['nombre']}")
        notas = {
            'parciales': [],
            'quices': [],
            'trabajos': []
        }
        if 'calificaciones' not in student_info:
            student_info['calificaciones'] = {}

        for category in notas.keys():
            grades_input = input(f"Ingrese las calificaciones de {category} separadas por comas: ").split(',')
            grades = [float(grade.strip()) for grade in grades_input]
            notas[category].extend(grades)
        
        student_info['calificaciones'] = notas

    print(students)