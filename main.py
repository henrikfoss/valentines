import streamlit as st
from datetime import date
import time

st.title("Vil du være min Valentine? 💖")

# Yes or No checkboxes
valentine_answer_yes = st.checkbox("Ja, jeg vil gerne være din Valentine!")
valentine_answer_no_container = st.empty()

if valentine_answer_yes:
    st.success("Jubii! Glæder mig til en skøn Valentinsdag sammen med dig! 💑")

    st.title("Hvor skal vi spise?")

    restaurant_options = ["Bones", "steak", "indisk", "hjemmelavet mad"]
    selected_restaurant = st.selectbox("Vælg et sted som du vil spise.", [""] + restaurant_options)

    # Dictionary mapping each restaurant to a custom message
    restaurant_messages = {
        "Bones": "Fantastisk valg! Lad os nyde nogle lækre spareribs! 🍖",
        "steak": "Et klassisk valg! Glæder mig til at nyde en saftig ripeye med dig. 🥩",
        "indisk": "Krydret og smagfuldt! Glæder mig til at spise butter chicken sammen. 🌶️🍛",
        "hjemmelavet mad": "Godt valg! Vi er fandme også gode til at lave mad selv. 🍲"
    }

    if selected_restaurant:
        st.success(f"{restaurant_messages[selected_restaurant]} 🍽️")

    st.title("Hvor og hvornår vil du se Den Grænseløse?")

    # Movie details
    selected_movie = "Den Grænseløse"

    # List of available showtimes
    movie_showtimes = [
        "ATLAS rødovre 20:30",
        "Bio Viften 19:30",
        "Imperial 21:30",
        "Palads 20:00",
        "Palads 21:30"
    ]
    selected_time = st.selectbox("Vælg sted og tidspunkt.", [""] + movie_showtimes)

    if selected_time:
        # Wait for 3 seconds before displaying the sweet message
        st.success(f"Det er hermed booket. Lad os spise {'på' if selected_restaurant == 'Bones' else ''} {selected_restaurant} og se {selected_movie} i {selected_time}. 🎬")
        time.sleep(3)
        st.success("\n Jeg elsker dig uendelig opløftet i uende og jeg glæder mig til Valentinsdag med dig! ❤️")

    # Clear the 'No' container if it exists
    valentine_answer_no_container.empty()

else:
    valentine_answer_no = valentine_answer_no_container.checkbox("Nej 😭")
    if valentine_answer_no:
        st.warning("Prøver igen næste år! 😔")
