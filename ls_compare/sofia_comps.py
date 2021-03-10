import re
import pandas as pd
import streamlit as st

import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

#st.set_page_config(layout="wide")

#input data obtained from Sofia website
sofia_table = st.text_input("Ingresa campos de Sofia")
#split sofia input by "space" and then search for underscore
sofia_table_split = sofia_table.split(" ")
#if underscore is present then it is added to list "sofia_item_list"
sofia_item_list = [word for word in sofia_table_split if "_" in word]
#print length of sofia_item_list which is the number of fields
st.write("Cantidad de elementos: {}".format(len(sofia_item_list)))


#input list of fields obtained from PR
pr_lista = st.text_input("Ingresa campos de la PR")
no_space_colons = pr_lista.replace(" ","").replace('"','')
pr_item_list = no_space_colons.split(",")

#button to show filtered sofia contents
if st.button("Mostrar elementos de Sofia"):
    if st.button("Ocultar elementos de Sofia"):
        pass
    st.write(pr_item_list)
    
#button to show filtered pull request contents
if st.button("Mostrar elementos de Pull Request"):
    if st.button("Ocultar elementos de Pull Request"):
        pass
    st.write(sofia_item_list)

#button to compare both lists
if st.button("Comparar listas"):
    if st.button("Ocultar comparación"):
        pass
    else:
        st.write("Parece que los soguientes elementos de la PR no están en Sofia:")
        for i in pr_item_list:
            if i not in sofia_item_list:
                st.markdown("**{}**".format(i))





#footer code obtained from:
# https://discuss.streamlit.io/t/st-footer/6447

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " for ",
        image('https://upload.wikimedia.org/wikipedia/commons/0/05/BBVA_2019.svg',
              width=px(35), height=px(30)),
        " by ",
        link('https://bluetab.com/', 'Bluetab'),
        br()
    ]
    layout(*myargs)


if __name__ == "__main__":
    footer()
