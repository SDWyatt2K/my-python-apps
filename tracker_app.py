import streamlit as st
import pandas as pd

st.set_page_config(page_title="Private Subscription Audit Tool", layout="centered")
st.title("🛡️ Subscription & Fee Audit Tracker")
st.write("Track forgotten charges, analyze bill spikes, and protect your cash.")

if "expenses" not in st.session_state:
    st.session_state["expenses"] = [
        {"Service": "Netflix", "Category": "Streaming", "Monthly Cost": 15.49},
        {"Service": "Gym Membership", "Category": "Fitness", "Monthly Cost": 45.00},
        {"Service": "Cloud Storage", "Category": "Software", "Monthly Cost": 2.99}
    ]

st.subheader("➕ Log a Monthly Bill or Subscription")
col1, col2, col3 = st.columns(3)

with col1:
    new_service = st.text_input("Service Name (e.g. Spotify):")
with col2:
    new_category = st.selectbox("Category:", ["Streaming", "Fitness", "Software", "Utilities", "Insurance"])
with col3:
    new_cost = st.number_input("Monthly Cost ($):", min_value=0.00, step=1.00)

if st.button("Add Subscription to Audit"):
    if new_service:
        st.session_state["expenses"].append({
            "Service": new_service,
            "Category": new_category,
            "Monthly Cost": float(new_cost)
        })
        st.success(f"Successfully added {new_service} to your tracker log!")

df = pd.DataFrame(st.session_state["expenses"])

st.markdown("---")
st.subheader("📋 Active Monthly Expenses Log")
st.dataframe(df, use_container_width=True)

total_monthly = df["Monthly Cost"].sum()
total_yearly = total_monthly * 12

metric_col1, metric_col2 = st.columns(2)
with metric_col1:
    st.metric(label="Total Monthly Overhead", value=f"${total_monthly:,.2f}")
with metric_col2:
    st.metric(label="Projected Yearly Bleed", value=f"${total_yearly:,.2f}")