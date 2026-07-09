import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Advanced Weather Portal", layout="centered")
st.title("🌦️ 5-Day Interactive Weather Hub")
st.write("Live data feeds featuring visual condition mapping.")

city = st.selectbox("Select a city to inspect:", ["Burbank, CA", "Alexander City, AL", "New Site, AL", "Atlanta, GA"])

coordinates = {
    "Burbank, CA": (34.1808, -118.3090),
    "Alexander City, AL": (32.9440, -85.9539),
    "New Site, AL": (33.0282, -85.7644),
    "Atlanta, GA": (33.7490, -84.3880)
}
lat, lon = coordinates[city]

def get_weather_visuals(code):
    if code == 0:
        return "Clear Sky", "☀️"
    elif code in [1, 2, 3]:
        return "Partly Cloudy", "🌤️"
    elif code in [45, 48]:
        return "Foggy", "🌫️"
    elif code in [51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82]:
        return "Rainy", "🌧️"
    elif code in [71, 73, 75, 77, 85, 86]:
        return "Snowing", "🌨️"
    elif code in [95, 96, 99]:
        return "Thunderstorm", "⛈️"
    else:
        return "Overcast", "☁️"

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": "true",
    "daily": "weathercode,temperature_2m_max,temperature_2m_min",
    "temperature_unit": "fahrenheit",
    "timezone": "auto"
}

try:
    raw_response = requests.get(url, params=params)
    response = raw_response.json()

    current = response["current_weather"]
    current_condition, current_emoji = get_weather_visuals(current["weathercode"])

    st.subheader(f"Current Status for {city}")
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric(label="Temperature", value=f"{current['temperature']}°F")
    with metric_col2:
        st.metric(label="Condition", value=f"{current_emoji} {current_condition}")

    st.markdown("---")

    st.subheader("5-Day Extended Forecast")
    daily_data = response["daily"]

    cols = st.columns(5)

    for i in range(5):
        raw_date = daily_data["time"][i]
        formatted_date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%b %d")

        max_temp = daily_data["temperature_2m_max"][i]
        min_temp = daily_data["temperature_2m_min"][i]
        wmo_code = daily_data["weathercode"][i]

        condition_text, condition_emoji = get_weather_visuals(wmo_code)

        with cols[i]:
            st.markdown(f"**{formatted_date}**")
            st.markdown(f"<h2 style='text-align: center; margin: 0;'>{condition_emoji}</h2>", unsafe_allow_html=True)
            st.caption(f"{condition_text}")
            st.markdown(f"🔺{int(max_temp)}°F")
            st.markdown(f"🔻{int(min_temp)}°F")

    st.markdown("---")
    st.subheader("📈 5-Day Temperature Trend")

    chart_data= pd.DataFrame({
        "Day": [datetime.strptime(d, "%Y-%m-%d").strftime("%a") for d in daily_data["time"]],
        "High Temp (°F)": daily_data["temperature_2m_max"],
        "Low Temp (°F)": daily_data["temperature_2m_min"]
    })

    st.line_chart(chart_data.set_index("Day"))

    st.markdown("---")
    st.subheader("🛰️ Live Interactive Radar Loop")

    radar_url = f"https://rainviewer.com/map.html?loc={lat},{lon},8&o=1&c=1&g=1&s=1&m=1&d=1&v=site&w=100%&h=450&map=1"

    st.components.v1.html(
        f'<iframe src="{radar_url}" width="100%" height="480" style="border:none; border-radius:10px;"></iframe>',
        height=500
    )        

except Exception as e:
    st.error(f"Error details: {e}")                    
        