from flask import Flask, render_template
import pymysql
 
app = Flask(__name__)
 
 
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'loja_makeup'
}
 
@app.route('/')
def home():
    # ERRO: não fechar conexão
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
 
    # ERRO: nome da tabela errado na query
    cursor.execute("SELECT * FROM produtos")
 
    produtos = cursor.fetchall()

    cursor.close()
    conn.close()
 
    
 
    return render_template('index.html', produtos=produtos)
 
if __name__ == '__main__':
    app.run(debug=True)