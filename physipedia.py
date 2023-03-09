import streamlit as st
import elect
import proto


st.title('PHYSIPEDIA')
st.markdown("**Welcome to Physipedia**")
st.header('INDEX')
electron = "http://localhost:8502"
proton = "http://localhost:8504"
#st.write("[electron] %s" % electron)
t = st.text_input('Enter your topic')

if(st.button('submit')):
    if(t == 'electron'):
        st.markdown("[electron](%s)" % electron)
    elif(t == "proton"):
        st.markdown("[proton](%s)" % proton)
    else:
        st.write('topic is not there')
