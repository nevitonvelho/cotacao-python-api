from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

def obter_cotacao_dolar():
    try:
        # Aqui estou fazendo a requisição a api do awesomeapi que fornece a cotação do dólar
        response = requests.get("https://economia.awesomeapi.com.br/json/daily/USD-BRL")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # valor da cotação do dólar
        cotacao_dolar = response.json()[0]["bid"]

        # Retorna a cotação para ser utilizada em outros lugares, se necessário
        return cotacao_dolar

    except requests.exceptions.RequestException as e:
        # Trata erros de requisição (por exemplo, conexão falha)
        print(f"Erro ao obter cotação do dólar: {e}")
        return None

@app.route('/cotacao-dolar')
def cotacao_dolar():
    cotacao = obter_cotacao_dolar()
    
    if cotacao is not None:
        return jsonify({"cotacao_dolar": cotacao})
    else:
        return jsonify({"erro": "Erro ao obter cotação do dólar"}), 500

if __name__ == "__main__":
    # vai executar o código a cada 30 minutos
    while True:
        app.run(debug=True)
        time.sleep(1800)  # 1800 segundos = 30 minutos
