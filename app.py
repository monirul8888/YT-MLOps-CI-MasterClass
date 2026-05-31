import streamlit as st

# Page config
st.set_page_config(
    page_title="Power Calculator",
    page_icon="🧮",
    layout="centered"
)

# Streamlit UI
st.title("🧮 Power Calculator")
st.write("Enter an integer to calculate its square, cube, and fifth power.")

# User input
n = st.number_input(
    "Enter an integer",
    value=1,
    step=1,
    format="%d"
)

# Calculate button
if st.button("Calculate"):
    square = n ** 2
    cube = n ** 3
    fifth_power = n ** 5

    st.success("Calculation completed!")

    st.write(f"**Number:** {n}")
    st.write(f"**Square:** {square}")
    st.write(f"**Cube:** {cube}")
    st.write(f"**Fifth Power:** {fifth_power}")

    # Optional table view
    st.subheader("Result Summary")

    result_data = {
        "Power Type": ["Square", "Cube", "Fifth Power"],
        "Formula": [f"{n}²", f"{n}³", f"{n}⁵"],
        "Result": [square, cube, fifth_power]
    }

    st.table(result_data)