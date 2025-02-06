import pandas as pd
import streamlit as st
import plotly.express as px
import datetime

#Define o Layout da Pagina para WideScreen
st.set_page_config(layout='wide', 
                   page_title='SP Distribuidora - Contas a Receber em Aberto')

try:
    #Realiza o upload dos arquivos
    arquivo_sicoob = st.file_uploader('Faça o Upload do Arquivo do Sicoob em Excel')
    sicoob = pd.read_excel(arquivo_sicoob)
    arquivo_santander = st.file_uploader('Faça o Upload do Arquivo do Santander em Excel')
    santander = pd.read_excel(arquivo_santander)

    # Renomeia as Colunas
    sicoob = sicoob.rename(columns={
        'Unnamed: 0':'Excluir1','Unnamed: 1':'Cliente','Unnamed: 2':'Excluir2','Unnamed: 3':'Excluir3', 'Unnamed: 4':'Excluir4',
        'Unnamed: 5':'Excluir5','Unnamed: 6':'Excluir6','Unnamed: 7':'Excluir7','Unnamed: 8':'Nosso Numero','Unnamed: 9':'Excluir9',
        'Unnamed: 10':'Excluir10','Unnamed: 11':'Excluir11','Unnamed: 12':'Seu Numero','Unnamed: 13':'Excluir13','Unnamed: 14':'Excluir14',
        'Unnamed: 15':'Excluir15','Unnamed: 16':'Excluir16','Unnamed: 17':'Excluir17','Unnamed: 18':'Excluir18','Unnamed: 19':'Excluir19',
        'Unnamed: 20':'Vencimento','Unnamed: 21':'Excluir21','Unnamed: 22':'Excluir22','Unnamed: 23':'Excluir23','Unnamed: 24':'Excluir24',
        'Unnamed: 25':'Excluir25','Unnamed: 26':'Valor', 'Unnamed: 27':'Excluir27'        
    })
    # Excluir as Colunas Desnecessárias
    sicoob = sicoob.drop(columns=[
        'Excluir1','Excluir2', 'Excluir3','Excluir4','Excluir5','Excluir6','Excluir7','Excluir9','Excluir10','Excluir11',
        'Excluir13','Excluir14','Excluir15','Excluir16','Excluir17','Excluir18','Excluir19','Excluir21','Excluir22',
        'Excluir23','Excluir24','Excluir25','Excluir27'
    ])
    # Apaga as células vázias (NA) e o Cabeçalho da planilha (Index == 'sacado') e inclui o nome do banco
    sicoob = sicoob.dropna()
    Excluir_index = sicoob[sicoob['Cliente'] == 'Sacado'].index
    sicoob = sicoob.drop(index=Excluir_index)
    sicoob['Banco'] = 'Sicoob'

    # Excluir as celulas vazias (NA) , Exclui o Cabeçalho  , renomeia e excluir Colunas e inclui o nome do banco
    santander = santander.dropna()
    santander = santander.drop(index=5)
    santander = santander.rename(columns={'Cod. Beneficiário':'Seu Numero',
                                        'Empresa':'Nosso Numero',
                                        'Agência/Conta Centralizadora':'Valor',
                                        'Unnamed: 3':'Vencimento',
                                        'Unnamed: 4':'Cliente',
                                        'Unnamed: 5':'Excluir1',
                                        'Unnamed: 6':'Excluir2',
                                        })
    santander = santander.drop(columns=['Excluir1','Excluir2'])
    santander = santander[['Cliente','Nosso Numero','Seu Numero','Vencimento','Valor']]
    santander['Banco'] = 'Santander'

    # Junta as tabelas dos 2 bancos e traz em formato final (formatada)
    tabela_final = pd.concat([sicoob,santander])         
    tabela_final = tabela_final.sort_values(by='Cliente' , ascending=True)
    tabela_final['Valor'] = tabela_final['Valor'].replace('.',',')
    tabela_final['Valor'] = tabela_final['Valor'].round(2)

    # Cria os campos e os filtros para pesquisar Clientes e/ou nota fiscais e imprimi a tabela filtrada
    def filtro_cliente():
        coluna1,coluna2 = st.columns(2)
        with coluna1:
            filtro_nome = st.text_input('Digite um Cliente para filtrar:')
        with coluna2:
            filtro_nf = st.text_input('Digite o número da nota fiscal para filtrar:') 
        global tabela_filtrada , tabela_filtrada2
        tabela_filtrada = tabela_final[tabela_final['Cliente'].str.contains(filtro_nome, case=False)]
        tabela_filtrada2 = tabela_filtrada[tabela_filtrada['Seu Numero'].str.contains(filtro_nf, case=False)]
        st.title('Total de Boletos em Aberto')
        tabela_filtrada2['Vencimento'] = pd.to_datetime(tabela_filtrada2['Vencimento']).dt.date
        st.dataframe(tabela_filtrada2 , use_container_width=True , hide_index=True)
        total_em_aberto = tabela_filtrada2['Valor'].sum()
        total_em_aberto = round(total_em_aberto , 2)
        devedores = len(tabela_filtrada2['Cliente'].unique())
        st.info(f'Existe um total de {devedores} clientes em atraso, devendo o total de R${total_em_aberto:,} na data de hoje!')
    filtro_cliente() 


    # Agrupa a tabela por clientes e traz a quantidade de clientes inadimplentes
    st.title('Total Em Aberto Por Cliente')
    total_agregado_por_cliente = tabela_final.drop(columns=['Nosso Numero', 'Seu Numero', 'Vencimento','Banco'])
    total_agregado_por_cliente = total_agregado_por_cliente.groupby(by='Cliente').sum()
    total_agregado_por_cliente['%'] = (total_agregado_por_cliente['Valor'] / total_agregado_por_cliente['Valor'].sum() * 100)
    total_agregado_por_cliente = total_agregado_por_cliente.sort_values(by='Cliente' , ascending=False)
    st.dataframe(total_agregado_por_cliente, use_container_width=True)
    devedores = len(tabela_final['Cliente'].unique())
    st.info(f'Existe um total de {devedores} Clientes em atraso')

    # Agrupa a tabela por Banco e traz o total em aberto
    st.title('Total Em Aberto Por Banco')
    total_agregado_por_banco = tabela_final.drop(columns=['Nosso Numero', 'Seu Numero', 'Vencimento','Cliente'])
    total_agregado_por_banco = total_agregado_por_banco.groupby('Banco').sum()
    total_agregado_por_banco['%'] = (total_agregado_por_banco['Valor'] / total_agregado_por_banco['Valor'].sum() ) * 100
    total_agregado_por_banco['%'] = total_agregado_por_banco['%'].round(2)
    total_agregado_por_banco_sem_perc = total_agregado_por_banco['Valor']
    st.dataframe(total_agregado_por_banco_sem_perc , use_container_width=True )

    # Cria e imprimi um grafico de pizza com a representação percentual dos boletos em aberto por banco
    total_agregado_por_banco = total_agregado_por_banco.reset_index()
    grafico = px.pie(total_agregado_por_banco, values='%',
                        labels='Banco', 
                        title='Montante por Banco', 
                        names='Banco',
                        color='Banco')
    st.plotly_chart(grafico)
except: # Evita mostrar codigos de erros ao usuario final, caso existe algum erro , apresenta o texto "SP Distribuidora"
    st.text('SP Distribudiora')
