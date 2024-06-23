
import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("Multilingual AI Assistant 🤖")
    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text=voice_input()
            response=llm_model_object(text)
            text_to_speech(response)
            
            
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()
            
            
            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")
            
if __name__=='__main__':
    main()
'''
import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    st.title("Multilingual AI Assistant 🤖")
    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()  # Assuming voice_input() handles microphone input
            response = llm_model_object(text)  # Assuming llm_model_object() processes text
            text_to_speech(response)  # Assuming text_to_speech() converts text to speech
            
            # Read audio file for streaming and downloading
            audio_file = open("speech.mp3", "rb")
            audio_bytes = audio_file.read()
            
            # Display response and provide audio streaming and download options
            st.text_area(label="Response:", value=response, height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")
            
if __name__ == '__main__':
    main()
'''