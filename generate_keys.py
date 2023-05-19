from pathlib import Path
import pickle
import streamlit_authenticator as stauth

name = ["Alim", "Sahil", "Devashish"]
username = ["ma", "msk", "dk"]
password = ["AM", "KSM", "KD"]

hashed_passwords = stauth.Hasher(password).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
