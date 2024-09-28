import streamlit as st
import numpy as np
from LE_solver import lu_decomposition

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://www.pixelstalk.net/wp-content/uploads/2016/06/Free-Download-Abstract-Backgrounds-HD.jpg");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def solve_lu_decomposition(L, U, B):
    n = len(B)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = B
    for i in range(n):
        y[i] = B[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x

st.sidebar.title('LINEAR EQUATION CALCULATOR')
choices = st.sidebar.selectbox('Select Option', ('Home', 'Linear Equations Calculator', 'About app'))

if choices == 'Home':
    st.markdown("""
                <h2 style="font-size: 60px; font-weight: bold; font-family: ' Arial, serif'; text-align: center">
                LINEAR EQUATIONS CALCULATOR
                </h2>
                <p style='text-align: center; font-size: 14px;'> By LU Decomposition.</p>
            """, unsafe_allow_html=True)
elif choices == 'Linear Equations Calculator':

    def main():
        st.markdown(
            "<h1 style='text-align: center; font-size: 44px; font-weight: bold; color: maroon ;'>LINEAR EQUATIONS CALCULATOR🧮</h1>",
            unsafe_allow_html=True)
        st.write("---")
        st.markdown("""
                            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center; color: black">
                            Input number of Linear Equations:
                            </h1>
                        """, unsafe_allow_html=True)
        num_equations = st.number_input("", min_value=2, max_value=5)

        A = np.zeros((num_equations, num_equations))
        B = np.zeros(num_equations)

        st.markdown(f"<h2 style='color: black; font-size: 25px;'> Enter Coefficients in each Equations:",
                    unsafe_allow_html=True)
        equation_columns = st.columns(num_equations)
        for i in range(num_equations):
            with equation_columns[i]:
                st.markdown(f"<h2 style='color: blue; font-size: 25px;'>EQUATION {i + 1}:</h2>",
                            unsafe_allow_html=True)
                for j in range(num_equations):
                    coeff_title = f"Coefficient {i + 1},{j + 1}"
                    A[i, j] = st.number_input(coeff_title, format="%f", key=f"A_{i}_{j}")

        st.markdown(f"<h2 style='color: black; font-size: 25px;'> Enter Constants:",
                    unsafe_allow_html=True)
        for i in range(num_equations):
            const_title = f"Constant {i + 1}"
            B[i] = st.number_input(const_title, format="%f", key=f"b_{i}")

        if st.button("Calculate"):
            L, U = lu_decomposition(A)
            roots = solve_lu_decomposition(L, U, B)

            st.markdown("""
                                        <h1 style="font-size: 25px; font-family: 'Arial, sans-serif'; text-align: center; color: black">
                                        STEP-BY-STEP SOLUTION:
                                        </h1>
                                        """, unsafe_allow_html=True)
            st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"<h2 style='color: blue; font-size: 26px;'> LOWER TRIANGULAR MATRIX (L):",
                            unsafe_allow_html=True)
                st.write(np.round(L, 2))
            with col2:
                st.markdown(f"<h2 style='color: blue; font-size: 26px;'> UPPER TRIANGULAR MATRIX (U):",
                            unsafe_allow_html=True)
                st.write(np.round(U, 2))
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(f"<h2 style='color: black; font-size: 26px;'> SOLUTIONS:",
                        unsafe_allow_html=True)
            for i, root in enumerate(roots):
                st.markdown(f"<h3 style='color: brown;'>X<sub>{i + 1}</sub>: {root}</h3>", unsafe_allow_html=True)


    if __name__ == "__main__":
            main()
else:
    st.sidebar.info("This app first performs LU decomposition of the equation 1, then solves the linear equations using"
                    " the LU factors. You can replace the coefficients in each equations with your own values to solve"
                    " different linear equations.")
    st.markdown("""
        ### You can contact us via ff:
        - Email: johnmarksolindom@gmail.com
        - Phone: 09518235460

        ### Connect with us via Facebook
        - https://www.facebook.com/johnmarksolindom


        For more inquiries, Please visit us on DME . Arigatou!!!.
        """)
