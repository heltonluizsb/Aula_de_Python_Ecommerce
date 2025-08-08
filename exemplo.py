import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='user_teste'
    )

def cadastrar_usuario(nome, email):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)
    cursor.execute(sql, valores)
    conn.commit()
    print(f"Usuário {nome} cadastrado com sucesso!")
    cursor.close()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")
    cursor.close()
    conn.close()

def main():
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            cadastrar_usuario(nome, email)
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()