import pandas as pd
import os

def reduzir_e_salvar_arquivo(origem, destino, colunas, chunksize=1000):
    dados_reduzidos = pd.DataFrame()
    for chunk in pd.read_csv(origem, usecols=colunas, chunksize=chunksize, delimiter=';', encoding='latin1'):
        dados_reduzidos = pd.concat([dados_reduzidos, chunk])
    dados_reduzidos.to_csv(destino, index=False, sep=';', encoding='latin1')

def main():
    caminho = '/users/edilton/desktop/DADOS14'  # Caminho atualizado
    
    colunas_arq1 = ['NU_ANO', 'CO_CURSO', 'CO_IES', 'CO_GRUPO']
    colunas_arq3 = ['NU_ANO', 'CO_CURSO', 'TP_PRES', 'TP_PR_GER', 'TP_PR_OB_FG', 'TP_PR_DI_FG', 'TP_PR_OB_CE', 'TP_PR_DI_CE', 'TP_SFG_D1', 'TP_SFG_D2', 'TP_SCE_D1', 'TP_SCE_D2', 'TP_SCE_D3']
    colunas_arq4 = ['NU_ANO', 'CO_CURSO', 'QE_I27', 'QE_I28', 'QE_I29', 'QE_I30', 'QE_I31', 'QE_I32', 'QE_I33', 'QE_I34', 'QE_I35', 'QE_I36', 'QE_I37', 'QE_I38', 'QE_I39', 'QE_I40', 'QE_I41', 'QE_I42', 'QE_I43', 'QE_I44', 'QE_I45', 'QE_I46', 'QE_I47', 'QE_I48', 'QE_I49', 'QE_I50', 'QE_I51', 'QE_I52', 'QE_I53', 'QE_I54', 'QE_I55', 'QE_I56', 'QE_I57', 'QE_I58', 'QE_I59', 'QE_I60', 'QE_I61', 'QE_I62', 'QE_I63', 'QE_I64', 'QE_I65', 'QE_I66', 'QE_I67', 'QE_I68']

    origem_arq1 = os.path.join(caminho, 'microdados2014_arq1.txt')
    origem_arq3 = os.path.join(caminho, 'microdados2014_arq3.txt')
    origem_arq4 = os.path.join(caminho, 'microdados2014_arq4.txt')

    destino_arq1 = os.path.join(caminho, 'reduzido_arq1.csv')
    destino_arq3 = os.path.join(caminho, 'reduzido_arq3.csv')
    destino_arq4 = os.path.join(caminho, 'reduzido_arq4.csv')

    reduzir_e_salvar_arquivo(origem_arq1, destino_arq1, colunas_arq1)
    reduzir_e_salvar_arquivo(origem_arq3, destino_arq3, colunas_arq3)
    reduzir_e_salvar_arquivo(origem_arq4, destino_arq4, colunas_arq4)

if __name__ == '__main__':
    main()
