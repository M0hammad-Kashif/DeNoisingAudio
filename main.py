import os

from tensorflow.python.ops import io_ops

from utils import *

st.title('Noise Enhancement using noise suppression')

model = tf.keras.models.load_model("Model.h5")
file_uploader = st.sidebar.file_uploader(label="", type=".wav")

st.subheader("")
st.subheader("Input Speech Sample")

if file_uploader is not None:
    with open(os.path.join("./savedFiles", file_uploader.name), "wb") as f:
        f.write(file_uploader.getbuffer())
    handle_uploaded_audio_file(file_uploader)
    st.subheader("")
    st.subheader("")

    out = predict(os.path.join("./savedFiles", file_uploader.name))

    wav_encoder = tf.audio.encode_wav(out, 16000)
    wav_saver = io_ops.write_file('./outputFiles/output.wav', wav_encoder)

    audio_file = open('./outputFiles/output.wav', 'rb')
    audio_bytes = audio_file.read()

    st.subheader("Output Speech Sample")

    st.audio(audio_bytes, format='audio/wav')