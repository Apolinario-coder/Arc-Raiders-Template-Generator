import os

PASTA = r"C:\Users\lukas\Documents\Phoenix Code\html projects\thumbs"  # <-- ajuste aqui

for nome in os.listdir(PASTA):
    caminho_antigo = os.path.join(PASTA, nome)

    if not os.path.isfile(caminho_antigo):
        continue

    novo_nome = nome

    # Remove "120px-" do começo
    if novo_nome.startswith("120px-"):
        novo_nome = novo_nome[len("120px-"):]

    # Remove ".png" antes da extensão final
    novo_nome = novo_nome.replace(".png.", ".")

    if novo_nome != nome:
        caminho_novo = os.path.join(PASTA, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome} -> {novo_nome}")
