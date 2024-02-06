import xmltodict
import os
import json

def pegar_infos(nome_arquivo):
    print(f"Pegou as informações {arquivo}")
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

    try:
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]['infNFe']
        else:
            infos_nf = dic_arquivo['nfeProc']["NFe"]["infNFe"]
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]
        if "vol" in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Nãi informado"
        print(numero_nota, empresa_emissora, nome_cliente, endereco , peso, sep="\n")
    except Exception as e:
        print(e)
        print(json.dumps(dic_arquivo, indent=4))



lista_arquivos = os.listdir("nfs")
print(lista_arquivos)

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
   # break
    