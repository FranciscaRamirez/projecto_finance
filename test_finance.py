#Importamos las funciones directamente desde el módulo finance
from finance import create_account, add_transaction, get_account_balance, get_total_balance

def main():

# Inicializamos la lista de cuentas
    accounts=[]

# Bucle principal del programa
    while True:
        print("\n1. Crear cuenta")
        print("2. Agregar transaccion")
        print("3. Consultar saldo de cuenta")
        print("4. Consultar saldo total")
        print("5. Salir")
  
  # Leemos la opción seleccionada por el usuario
        option=int(input("\n Seleccione una opción: "))
  
  # Creamos una cuenta
        if option == 1:
  
  # Solicitamos el nombre y el tipo de cuenta         
            name = input("Ingrese el nombre de la cuenta: ")
            account_type = input("Ingrese el tipo de cuenta: ")
  # Llamamos a la función create_account y almacenamos el account_id generado          
            account_id = create_account(accounts, name, account_type)
  # Imprimimos un mensaje informando que la cuenta ha sido creada         
            print(f"Cuenta '{name}' creada con ID {account_id}")
  
  # Agregamos una transacción
        elif option == 2:
  # Solicitamos el account_id, la descripción y el monto de la transacción
            account_id = int(input("Ingrese el ID de la cuenta: "))
            description = input("Ingrese la descripcion de la transaccion: ")
            amount = float(input("Ingrese el monto de la transaccion: "))
      
  # Llamamos a la función add_transaction para agregar la transacción a la cuenta      
            add_transaction(accounts, account_id, description, amount)
         
  # Imprimimos un mensaje informando que la transacción ha sido agregada     
            print("Transaccion fue agregada exitosamente")
 
  # Consultamos el saldo de una cuenta
        elif option == 3:
  
  # Solicitamos el account_id         
            account_id = int(input("Ingrese el ID de la cuenta: "))
 
  # Llamamos a la función get_account_balance para obtener el saldo de la cuenta         
            balance = get_account_balance (accounts,account_id)
  
  # Imprimimos el saldo de la cuenta         
            print(f"El saldo de la cuenta {account_id} es: {balance}") 
  
  # Consultamos el saldo total de todas las cuentas
        elif option == 4:
  
  # Llamamos a la función get_total_balance para obtener el saldo total          
            total_balance = get_total_balance(accounts)  
  
  # Imprimimos el saldo total de todas las cuentas          
            print (f"el saldo total de todas la cuentas es: {total_balance} ")  
  
  # Salimos del programa
        elif option == 5:
  
  # Imprimimos un mensaje de despedida         
            print("Gracias por usar el programa.")  
  
  # Salimos del bucle principal         
            break
  
  # Opción inválida
        else:
  
  # Imprimimos un mensaje informando que la opción es inválida         
            print("Opcion invalida, por favor intente nuevamente")  
  
  #Si este archivo se ejecuta como el script principal, llamamos a la función main
if __name__== "__main__":
    main()

