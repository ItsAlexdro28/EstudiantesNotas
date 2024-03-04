import modules.studentGestor as st
import tabulate

def menu():
    print("""
    MENU PRINCIPAL

    1. Agregar estudiante
    2. Buscar estudiante
    3. Listar estudiantes
    4. Eliminar estudiante por ID
    5. Eliminar estudiante por nombre
    6. Agregar calificaciones
    7. Salir
    """)
    option = input("Seleccione una opción: ")

    match option:
        case '1':
            st.addstudent(student)
        case '2':
            st.searchStudent(student)
        case '3':
            st.listData(student)
        case '4':
            st.delStudent(student)
        case '5':
            st.delByName(student)
        case '6':
            st.addGrades(student)
        case '7':
            exit()
        case _:
            print("La opción ingresada no es válida.")

if __name__ == '__main__':
    student = {}
    
    while True:
        menu()
