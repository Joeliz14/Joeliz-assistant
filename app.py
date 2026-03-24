import streamlit as st
import streamlit.components.v1 as components

# 1. Joeliz Page Setup
st.set_page_config(page_title="Joeliz Assistant", page_icon="🤟", layout="wide")

st.title("🤟 Joeliz Assistant: Live Transcription")
st.markdown("### Instant Communication Support for MUBS Students")

# 2. Helpful instructions
st.info("Click the button and speak. Words appear instantly. If it doesn't write, check the lock icon in your address bar!")

# 3. The Live Engine (Instant Writing with Unique Key Logic)
joeliz_live_html = """
<div id="joeliz-root">
    <button id="mic-btn" style="padding: 20px; background: #007BFF; color: white; border: none; border-radius: 12px; cursor: pointer; font-size: 22px; width: 100%; font-weight: bold; margin-bottom: 20px;">
        🎤 START JOELIZ LIVE LISTENING
    </button>
    <div id="joeliz-output" style="padding: 30px; border: 5px solid #007BFF; border-radius: 20px; font-size: 45px; font-weight: bold; background: white; min-height: 350px; color: black; line-height: 1.4; font-family: sans-serif;">
        Waiting for your voice...
    </div>
</div>

<script>
    const btn = document.getElementById('mic-btn');
    const output = document.getElementById('joeliz-output');
    
    // Using a unique session key for the speech engine
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {
        const recognition = new SpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;
        recognition.lang = 'en-US'; 

        btn.onclick = () => {
            if (btn.innerText.includes("START")) {
                try {
                    recognition.start();
                    btn.innerText = "🛑 STOP JOELIZ LISTENING";
                    btn.style.background = "#D32F2F";
                    output.innerText = "Listening now... talk to me!";
                } catch (e) {
                    console.error(e);
                }
            } else {
                recognition.stop();
                btn.innerText = "🎤 START JOELIZ LIVE LISTENING";
                btn.style.background = "#007BFF";
            }
        };

        recognition.onresult = (event) => {
            let finalString = '';
            for (let i = 0; i < event.results.length; ++i) {
                finalString += event.results[i][0].transcript;
            }
            output.innerText = finalString;
        };

        recognition.onerror = (event) => {
            output.innerText = "Mic Error: " + event.error + ". Click the lock icon 🔒 next to the web address and Allow Microphone.";
        };

    } else {
        output.innerText = "Please use Chrome or Edge browser.";
    }
</script>
"""

# 4. Launch the component
components.html(joeliz_live_html, height=600)

st.caption("Developed by Joeliz - Dedicated to Accessible Education at MUBS.")
