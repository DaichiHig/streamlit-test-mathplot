import streamlit as st
import matplotlib.pyplot as plt
import math

def graphplot(f, low, high, n=100):
    d = (high-low)/n
    xL = [low+d*i for i in range(n)]
    yL = [f(low+d*i) for i in range(n)]
    plt.plot(xL, yL)
    plt.axhline(0,c='black')
    plt.axvline(0,c='black')
    #plt.show()
    st.pyplot(plt)

low, high = -5, 5

inp = st.text_input('f(x)=')

if st.button('Plot'):
    func = lambda x: eval(inp)
    graphplot(func, low, high)
