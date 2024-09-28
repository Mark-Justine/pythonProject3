import streamlit as st
import Adding_matrices as am
import Multiplying_matrices as mm
import Inverse_matrices as im
import Determenant_matrices as dm
import Transpose_matrices as tm

st.set_page_config(
    page_title="Matrix Operator",
    page_icon="https://m.media-amazon.com/images/I/813dE2pH7XL._UF1000,1000_QL80_.jpg",
    layout="centered",
    initial_sidebar_state="expanded")

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/free-vector/matrix-style-binary-code-digital-falling-numbers-blue-background_1017-37387.jpg?w=996&t=st=1710938727~exp=1710939327~hmac=fae5c9a802bb01ccf4e8fa25479ef347f6b1db21f5dce37d1a1a777c6125cac9");
    background-size: 60vw 100vh;  #This sets the size to cover 100% of the viewport width and height
    background-position: center;  
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center">
        Enter the size of the matrices:
        </h1>
    """, unsafe_allow_html=True)
with col2:
    row = st.number_input("ROW:", min_value=1, max_value=None, key='row')
with col3:
    column = st.number_input("COLUMN:", min_value=1, max_value=None, key='column')

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue;">
            Matrix A
            </h1>
        """, unsafe_allow_html=True)
    for row_index in range(row):
        columns = st.columns(column)
        for col_index, col in enumerate(columns):
            with col:
                st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')

with col5:
    st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue;">
                Matrix B
                </h1>
            """, unsafe_allow_html=True)
    for row_index in range(row):
        columns = st.columns(column)
        for col_index, col in enumerate(columns):
            with col:
                st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
matA = []
matB = []
for i in range(row):
    rowElement = []
    for j in range(column):
        for value in st.session_state:
            if value == f"Arow{i+1}Acol{j+1}":
                rowElement.append(st.session_state[value])
    matA.append(rowElement)
print(matA)
for i in range(row):
    rowElementB = []
    for j in range(column):
        for value in st.session_state:
            if value == f"Brow{i+1}Bcol{j+1}":
                rowElementB.append(st.session_state[value])
    matB.append(rowElementB)
print(matB)
print(st.session_state)
option = st.selectbox("What would you like to do?", ("Addition of Matrices", "Multiplication of Matrices", "Inverse of Matrices",
                                                     "Determenant of Matrices", "Transpose of Matrices"), index=None, placeholder="Select Matrix Operation...")
calculateMatrix = st.button("Calculate", key='cal')

if calculateMatrix:
    if option == "Addition of Matrices":
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue; align: 'Center';">
                        Matrix Result
                        </h1>
                    """, unsafe_allow_html=True)
        matrix_Result = am.get_sumOfMatrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:

            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                      key=f'Rrow{row_index + 1}Rcol{col_index + 1}')



    if option == "Multiplication of Matrices":
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue; align: 'Center';">
                        Matrix Result
                        </h1>
                    """, unsafe_allow_html=True)
        matrix_Result = mm.multiplying_matrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:

            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                      key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

    if option == "Determenant of Matrices":
        st.markdown("""
                                <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; align: 'Center';">
                                Matrix Result
                                </h1>
                            """, unsafe_allow_html=True)
        if len(matA[0]) != len(matB):
            st.error("Cannot perform calculation. The matrices must be squared.")
        else:
            matrixA, matrixB = dm.determinant_matrices(matA, matB)
            col6, col7 = st.columns(2)
            with col6:
                st.markdown("""
                                <h1 style="font-size: 24px; text-align: center; color: blue;">
                                Determinant of Matrix A</h1>
                                """, unsafe_allow_html=True)
                st.text_input("", value=str(matrixA))
            with col7:
                st.markdown("""
                                <h1 style="font-size: 24px; text-align: center; color: blue;">
                                Determinant of Matrix B
                                 </h1>
                                """, unsafe_allow_html=True)
                st.text_input("", value=str(matrixB))

    if option == "Inverse of Matrices":
        st.markdown("""
                        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; align: 'Center';">
                        Matrix Result
                        </h1>
                    """, unsafe_allow_html=True)

        matrixA, matrixB = im.inverse_matrices(matA, matB)
        col6, col7 = st.columns(2)
        with col6:
            st.markdown("""
                                    <h1 style="font-size: 24px; text-align: center; color: blue;">
                                    Inverse of Matrix A</h1>
                                    """, unsafe_allow_html=True)
            for row_index in range(len(matrixA)):
                for col_index in range(len(matrixA[row_index])):
                    st.text_input("", value=str(matrixA[row_index][col_index]))
        with col7:
                st.markdown("""
                                    <h1 style="font-size: 24px; text-align: center; color: blue;">
                                    Inverse of Matrix B
                                     </h1>
                                    """, unsafe_allow_html=True)
                for row_index in range(len(matrixB)):
                    for col_index in range(len(matrixB[row_index])):
                        st.text_input("", value=str(matrixB[row_index][col_index]))


    if option == "Transpose of Matrices":
        st.markdown("""
                                <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; align: 'Center';">
                                Matrix Result
                                </h1>
                            """, unsafe_allow_html=True)

        matrixA, matrixB = tm.transpose_matrices(matA, matB)
        col6, col7 = st.columns(2)
        with col6:
            st.markdown("""
                                    <h1 style="font-size: 24px; text-align: center; color: blue;">
                                    Transpose of Matrix A</h1>
                                    """, unsafe_allow_html=True)
            st.text_input("", value=str(matrixA))
        with col7:
            st.markdown("""
                                    <h1 style="font-size: 24px; text-align: center; color: blue;">
                                    Transpose of Matrix B
                                     </h1>
                                    """, unsafe_allow_html=True)
            st.text_input("", value=str(matrixB))
