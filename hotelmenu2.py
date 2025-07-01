import streamlit as st

# ----------------------------
# 1. Data: the restaurant menu
# ----------------------------
MENU = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80,
}

# ----------------------------
# 2. Page configuration
# ----------------------------
st.set_page_config(page_title="SK Restaurant", page_icon="🍕")

# ----------------------------
# 3. Header
# ----------------------------
st.title("Welcome to **SK Restaurant**")
st.caption("Select your items below and see the running total in real time.")

# ----------------------------
# 4. Show the menu
# ----------------------------
st.subheader("Menu")
for item, price in MENU.items():
    st.markdown(f"- **{item.capitalize()}** &nbsp;—&nbsp; Rs {price}")

st.divider()

# ----------------------------
# 5. Ordering interface
# ----------------------------
st.subheader("Place Your Order")

# Let the user pick any number of items
selected_items = st.multiselect(
    "Choose one or more items:",
    options=list(MENU.keys()),
    format_func=lambda x: x.capitalize(),
)

# (Optional) — add quantities for each selected item
quantities = {}
if selected_items:
    st.write("#### Quantities")
    for item in selected_items:
        quantities[item] = st.number_input(
            f"{item.capitalize()} (Rs {MENU[item]} each)",
            min_value=1,
            step=1,
            key=f"qty_{item}",
        )

# ----------------------------
# 6. Calculate the total
# ----------------------------
total = sum(MENU[item] * quantities.get(item, 1) for item in selected_items)

# Display the running total
st.markdown(f"### Total to Pay: **Rs {total}**")

# ----------------------------
# 7. Confirm button
# ----------------------------
if st.button("Confirm Order"):
    if not selected_items:
        st.warning("Please select at least one item before confirming.")
    else:
        summary = ", ".join(
            f"{item.capitalize()} × {quantities.get(item,1)}"
            for item in selected_items
        )
        st.success(f"Thank you! You ordered {summary} for a total of Rs {total}.")
        st.balloons()
