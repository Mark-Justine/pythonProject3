import numpy as np
import streamlit as st
def inverse_matrices(matA, matB):
    try:
        np_matA = np.array(matA, dtype=float)
        np_matB = np.array(matB, dtype=float)

        inv_matA = np.linalg.inv(np_matA)
        inv_matB = np.linalg.inv(np_matB)

        return inv_matA, inv_matB
    except np.linalg.LinAlgError as e:
        st.error("Error: Singular matrix. Cannot invert the matrices.")
        return None, None