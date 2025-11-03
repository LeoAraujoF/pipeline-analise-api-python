import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"


try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados_da_api = resposta.json()

        df = pd.DataFrame(dados_da_api)

        posts_do_usuario_7 = df[df["userId"] == 7]

        print("\n--- Posts do Usuário 7 ---")
        print(posts_do_usuario_7)

    else:
        print(f"Erro na API: {resposta.status_code}")


except requests.exceptions.RequestException as e:
    print(f"Erro de conexão: {e}")

print("\nPrograma finalizado.")
