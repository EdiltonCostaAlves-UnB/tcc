# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys

# Definições de constantes
COLUNAS_DE_INTERESSE = [
    'NU_ANO', 'CO_CURSO', 'CO_IES', 'CO_GRUPO',
    'QE_I28', 'QE_I29', 'QE_I30', 'QE_I34',
    'QE_I37', 'QE_I41', 'QE_I43', 'QE_I44',
    'QE_I47', 'QE_I48', 'QE_I49', 'QE_I57',
    'QE_I61', 'QE_I62', 'QE_I63'
]
CURSOS_SELECIONADOS = [4003, 5710, 5806, 5814, 5902, 6008, 6208, 6307, 6405]
ANOS = [2014, 2017, 2019]

# Função para tratar caracteres especiais do LaTeX
def escape_latex(s):
    return s.replace('%', '\\%').replace('_', '\\_')

# Função para ler dados dos arquivos CSV
def ler_dados(caminho):
    dados_concatenados = pd.DataFrame()
    for ano in ANOS:
        arquivo = os.path.join(caminho, f"merge_{ano}.csv")
        if os.path.isfile(arquivo):
            dados = pd.read_csv(arquivo, usecols=COLUNAS_DE_INTERESSE)
            dados['Ano'] = ano
            dados_concatenados = pd.concat([dados_concatenados, dados], ignore_index=True)
    return dados_concatenados

# Função para gerar o documento LaTeX
def gerar_latex_modificado(df, x, arquivo_saida):
    with open(arquivo_saida, 'w') as f:
        f.write("\\begin{table}[H]\n")
        f.write("\\centering\n")
        f.write(f"\\caption{{Percepções dos estudantes na questão QE\\_{x}}}\n")
        f.write("\\begin{tabular}{|l|c|ccc|ccc|cc|}\n")
        f.write("\\hline\n")
        f.write("\\toprule\n")
        f.write("Ano & Participantes & Discordo totalmente & Discordo & Discordo parcialmente & Concordo parcialmente & Concordo & Concordo totalmente & Não sei responder & Não Respondeu \\\\\n")
        f.write("\\midrule\n")
        
        for curso in CURSOS_SELECIONADOS:
            f.write("\\hline\n")
            f.write(f"\\multicolumn{{10}}{{|c|}}{{{curso}}}\\\\\n")
            f.write("\\hline\n")
            for ano in ANOS:
                ano_df = df[(df['CO_GRUPO'] == curso) & (df['Ano'] == ano)]
                participantes = len(ano_df)
                if participantes > 0:
                    percentuais = " & ".join([f"{ano_df[f'QE_I{x}'].value_counts(normalize=True).get(i, 0) * 100:.2f}\\%" for i in range(1, 9)])
                    f.write(f"{ano} & {participantes} & {percentuais}\\\\\n")
                else:
                    # Imprime apenas o ano, sem mais dados
                    f.write(f"{ano} & & & & & & & & & \\\\\n")
            f.write("\\hline\n")
        
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")

# Função principal para executar o script
def main(suffix_coluna):
    caminho = "/Users/edilton/Desktop/DADOS"
    df = ler_dados(caminho)
    arquivo_saida = os.path.join(caminho, f"relatorio_QE_I{suffix_coluna}.tex")
    gerar_latex_modificado(df, suffix_coluna, arquivo_saida)

# Ponto de entrada do script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 tex.py <number>")
        sys.exit(1)
    suffix_coluna_desejada = sys.argv[1]
    main(suffix_coluna_desejada)

# Execute este script com:
# python3 tex.py 28
