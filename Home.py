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
        1. Selecione um produto.
        2. Selecione a participação da NCM que terá seu imposto alterado naquele produto (0 a 100%).
        3. Selecione a alteração no imposto de importação a ser aplicada.
        4. Clique em "Calcular" para obter o resultado.
        """
    )
    coluna_produto,coluna_participacao,coluna_imposto = st.columns([3,1,1])
    produto_selecionado = coluna_produto.selectbox(
        "Selecione um produto",
        options=list(dict_produtos.values()),
        key="produto",
    )
    index_setor_selecionado = list(dict_produtos.keys())[list(dict_produtos.values()).index(produto_selecionado)]
    #Selecionar a paticipação por meio de um slider
    participacao_setor = coluna_participacao.slider(
        "Participação da NCM no produto (%)",
        min_value=0,
        max_value=100,
        value=100,
        step=1,
        key="participacao",
    )
    
    alteracao_imposto = coluna_imposto.slider(
        "Percentual de alteração do imposto (%)",
        min_value=-400,
        max_value=400,
        value=0,
        step=1,
        key="imposto",
    )
    
    #Calcular o impacto
    if st.button("Calcular"):
        #Verifica se o produto foi selecionado
        if produto_selecionado == "":
            st.warning("Selecione um produto")
        else:
            #Verifica se a participação é maior que 0
            if participacao_setor <= 0:
                st.warning("A participação deve ser maior que 0")
            else:
                #Calcula o impacto
                mip = MIPCalculator(index_setor_selecionado,participacao_setor,alteracao_imposto)
                diferencas = mip.calculate_differences()
                #Cria um dataframe com os resultados
                st.write(diferencas)
                st.balloons()

home()