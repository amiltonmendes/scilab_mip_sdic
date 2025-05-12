import streamlit as st
from classes.mip import MIPCalculator,dict_produtos,dict_setores




def home():
    #Alterar o layout para o modo wide
    st.set_page_config(
        page_title="Protótipo de cálculo de impacto de aumento de impostos",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("Home")
    st.write(
        """
        ## Protótipo de cálculo de impacto de aumento de impostos
        """
    )

    st.write(
        """
        ### Como usar:
        1. Selecione um produto das contas nacionais, que é um agregado de NCM's.
        2. Indique a participação da NCM que terá seu imposto alterado naquele produto (0 a 100%). Isso é necessário para ponderar o aumento no imposto e substituição de importações. As contas nacionais são muito agregadas e não seria razoável propagar o impacto do aumento de imposto de uma NCM para todo o produto.
        3. Escolha o aumento percentual no imposto de importação já existente.
        4. Acrescente a estimativa do percentual do que é importado do produto que será substituído por produto nacional, considerando que o aumento de imposto não direcionará todo o consumo para a produção nacional. 
        5. Clique em "Calcular" para obter o resultado.
        """
    )
    coluna_produto,coluna_participacao,coluna_imposto,coluna_substituicao_importacao = st.columns([3,1,1,1])
    produto_selecionado = coluna_produto.selectbox(
        "1. Selecione um produto",
        options=list(dict_produtos.values()),
        key="produto",
    )
    index_setor_selecionado = list(dict_produtos.keys())[list(dict_produtos.values()).index(produto_selecionado)]
    #Selecionar a paticipação por meio de um slider
    participacao_produto = coluna_participacao.slider(
        "2. Participação da NCM no produto (%)",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
        key="participacao",
    )
    
    alteracao_imposto = coluna_imposto.slider(
        "3. Aumento do imposto de importação(%)",
        min_value=0,
        max_value=400,
        value=0,
        step=1,
        key="imposto",
    )

    percentual_substituicao_importacao = coluna_substituicao_importacao.slider(
        "4. Substituição de importação prevista (%)",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        key="substituicao",
    )
    
    #Calcular o impacto
    if st.button("Calcular"):
        #Verifica se o produto foi selecionado
        if produto_selecionado == "":
            st.warning("Selecione um produto")
        else:
            #Verifica se a participação é maior que 0
            if participacao_produto <= 0:
                st.warning("A participação deve ser maior que 0")
            else:
                #Calcula o impacto
                mip = MIPCalculator()
                #Calcula o impacto
                preco_antes,preco_depois = mip.calcular_precos(index_setor_selecionado,aumento_imposto=alteracao_imposto/100,participacao_produto=participacao_produto/100)
                diferencas = mip.calculate_differences(preco_antes, preco_depois)
                impacto_economia_global = ((preco_depois.sum()/preco_antes.sum())-1) *100


                top_diferencas = mip.show_top_differences(diferencas, 5)
                dict_impacto = mip.calculate_impactos(index_setor_selecionado,participacao_produto/100,percentual_substituicao_importacao/100)
                st.write("### Resultados")
                st.write(f"**1. Variação de preço global após aumento do imposto:** {impacto_economia_global:,.2f}%")
                st.write(f"**2. Variação de preço dos 5 setores mais impactados após aumento do imposto:**")
                #Criar uma lista para cada elemento em top_diferencas
                for i in range(len(top_diferencas)):
                    st.markdown(f" * {top_diferencas.iloc[i]['Setor']}: {top_diferencas.iloc[i]['Diferença']:.2f}%")
                st.write(f"**3. Resultado dos principais efeitos multiplicadores ao substituir {percentual_substituicao_importacao:,.0f}% das importações:**")
                st.write(f'* Geração de {dict_impacto["Aumento Ocupações"]:,.0f} postos de trabalho'.replace(',',"X").replace('.',",").replace("X","."))
                st.write(f'* Aumento de {dict_impacto["Aumento Massa Salarial"]/10**6:,.2f} milhões de reais em massa salarial (remunerações)'.replace(',',"X").replace('.',",").replace("X","."))
                st.write(f'* Aumento de {dict_impacto["Aumento Produção"]/10**6:,.2f} milhões de reais em valor agregado bruto'.replace(',',"X").replace('.',",").replace("X","."))



                #Exibe o gráfico

home()