def create_account(accounts, name, account_type):
    account_id = len(accounts)
    account = {'id': account_id, 'name': name, 'account_type' : account_type, 'transaction': []}
    accounts.append(account)
    return account_id


#Función para buscar una cuenta por su nombre
def find_account_by_name(accounts, account_name):
    for account in accounts:
        if account ['name'] == account_name:
            return account
        return None
    
#Función para agregar una transacción a una cuenta
def add_transaction(accounts, account_name, description, amount):
    account= find_account_by_name(accounts, account_name)
    if account:
        account['transactions'].append({'Description' : description, 'amount': amount})
    else:
        print("Cuenta no encontrada.")  


#Función para calcular el monto total de transacciones de un tipo especifico (ingreso o egreso)
def calculate_transaction_total(account, transaction_type):
    total = 0
    for transaction in account['transaction']:
        if transaction_type == 'ingreso':
            if transaction['amount']> 0:
                total += transaction['amount']
        elif transaction_type == 'egreso':
            if transaction['amount'] < 0:
                total += transaction ['amount']   

    return total

#Funcion para obtener el saldo de una cuenta
def get_account_balance(accounts, account_name):
    account = find_account_by_name(accounts, account_name)
    if account:
        income = calculate_transaction_total(account, 'ingreso')
        expenses = calculate_transaction_total(account, 'egreso')
        balance = income + expenses
        return balance
    else:
        print("Cuenta no encontrada")
        return 0

def get_total_balance(accounts):
    total_balance = sum(get_account_balance(accounts, account ['name']) for account in accounts)
    return total_balance     
        



