import streamlit as st
import pandas as pd
import datetime
import requests


def send_to_server(user_text, user_date, user_reminder):
    try:

        requests.get('http://127.0.0.1:5000/reminder', params={"user_text": user_text,
                                                               "user_date": user_date,
                                                               "user_reminder": user_reminder})

        print("Mission Accomplished")
        return True

    except ConnectionError as error:
        print(f'Server error. message - {error}')
        return "Mission Unaccomplished"


if 'reminder' not in st.session_state:
    st.session_state["reminder"] = pd.DataFrame(
        [
            {"Write your reminder": "", "Date": datetime.datetime.now(), "Interested in a reminder?": False}
        ],

    )
new_reminder = {"Write your reminder": pd.DataFrame,
                "Date": datetime.datetime.now(),
                "Interested in a reminder?": False}


edited_df = st.data_editor(

    st.session_state["reminder"],
    width=1000,
    use_container_width=True,
    hide_index=True,
    num_rows="dynamic",

    column_config={
        "Date": st.column_config.DatetimeColumn(
            format="D MMM YYYY, HH:mm a",
            step=60,
        ),
    },

)


for index, row in edited_df.iterrows():
    text = row["Write your reminder"]
    date = row["Date"]
    reminder = row["Interested in a reminder?"]
    if text and send_to_server(text, date, reminder):
        print(f"{text}, {date}, {reminder}")
