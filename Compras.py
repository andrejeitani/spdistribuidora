import pandas as pd
import streamlit as st

#Define o Layout da Pagina para WideScreen
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - Compras')

try:
    #Realiza o upload do arquivo e realiza os devidos tratamentos
    arquivo = st.file_uploader('Faça o Upload do Arquivo Ponto de Compra')
    df = pd.read_excel(arquivo, engine='openpyxl')
    pack = st.file_uploader('Faça o Upload da tabela da Intelbras')
    pack = pd.read_excel(pack)
    df = df.drop(index=[0,1])
    df = df.rename(columns={
    'Período da Consulta 90 dias':'Codigo',
    'Unnamed: 1':'Produto',
    'Unnamed: 2':'Marca',
    'Unnamed: 3':'Vendas',
    'Unnamed: 4':'Excluir 0',
    'Unnamed: 5':'Remessa',
    'Unnamed: 6':'Vendas&Remessas',
    'Unnamed: 7':'Excluir 1',
    'Unnamed: 8':'Media Mensal',
    'Unnamed: 9':'Estoque SJC',
    'Unnamed: 10':'Cobertura em Dias',
    'Unnamed: 11':'Excluir 2',
    'Unnamed: 12':'Comprado',
    'Unnamed: 13':'Excluir 3',
    'Unnamed: 14':'Programado',
    'Unnamed: 15':'Status',
    'Unnamed: 16':'Sugestao 40 Dias',
    'Unnamed: 17':'Excluir 4',
    'Unnamed: 18':'Excluir 5',
    })

    # Excluir as colunas em branco
    df = df.drop(columns=['Excluir 0','Excluir 1','Excluir 2','Excluir 3','Excluir 4','Excluir 5'])

    # Define o tipo de variavel em cada coluna
    df['Sugestao 40 Dias'] = df['Sugestao 40 Dias'].astype(float)
    df['Comprado'] = df['Comprado'].astype(float)
    df['Programado'] = df['Programado'].astype(float)

    # Substitui todos os valores faltantes para o numero 0
    df['Vendas'] = df['Vendas'].fillna(0)
    df['Remessa'] = df['Remessa'].fillna(0)
    df['Vendas&Remessas'] = df['Vendas&Remessas'].fillna(0)
    df['Comprado'] = df['Comprado'].fillna(0)
    df['Programado'] = df['Programado'].fillna(0)

    # Cria a Coluna com o devido calculo de compras
    #df['Comprar'] = (df['Sugestao 40 dias'] - df['Comprado'])

    # Classica as colunas pela sua ordem alfabetica
    df = df.sort_values(by='Marca' , ascending=True)

    # Define o tipo de variavel da coluna, para que a chave seja do mesmo tipo em ambos os dataframes
    pack['Codigo'] = pack['Codigo'].astype(str)

    # Exclui todos os valores faltantes do arquivo que contem o Pack e a Origem
    pack = pack.dropna()

    # Realiza a junção entre os 2 dataframes e Exclui os codigos em duplicidade
    df = df.merge(pack , left_on='Codigo' , right_on='Codigo' , how='outer')
    df = df.drop_duplicates() #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    # Realiza o filtro do arquivo , para produtos com definição de compra maior que 1
    df = df[df['Sugestao 40 Dias'] > 0]
    df['Total'] = (df['PV'] * df['Sugestao 40 Dias']).round(2)

    # Cria a Coluna comprar, ja com o ajuste da multiplicidade dos pack's
    df['Comprar'] = ((df['Sugestao 40 Dias'] / df['Qtd. Multipla']).round(0) * df['Qtd. Multipla'])
    

    # Função de filtro 
    def main():
    # Campo de texto para inserir o critério de filtro
        filtro = st.text_input('Digite uma marca para filtrar:')

        # Aplicar o filtro e mostrar o resultado
        filtered_df = df[df['Marca'].str.contains(filtro, case=False)]
        st.write('Planilha de Compras')
        st.dataframe(filtered_df , use_container_width=True)

        a = len(filtered_df)
        b = filtered_df['Total'].sum().round(2) 
        st.write('Produtos para comprar: ',str(a) ,
            ' - ' ,
            f'Total de intelbras a comprar: R$ {b}'
                )
    if __name__ == '__main__':
        main()
except:
    st.write('SP Distribuidora')
