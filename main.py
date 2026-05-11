import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Welcome to the house of krishiv", layout="wide")
st.logo("images/logo/logo.jpeg",size="large")
# 2. Initialize Session State for Cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 3. Product Data (Example)
products = [
    {"id": 1, "name": "Elegant Ethnic Wear Kurti", "price": 25.00, "image": "images/elegant_ethnic_wear_kurti.jpg"},
    {"id": 2, "name": "Blue Embroidered Cotton Anarkali", "price": 50.00, "image": "images/blue_embrodered_connon_anarkali.jpg"},
    {"id": 3, "name": "Cotton Suite With Duppatta", "price": 120.00, "image": "images/contton_suit_set_with_duppatta.jpg"},
    {"id": 4, "name": "Cotton Suite With Duppatta", "price": 85.00, "image": "images/elegant_cotton_suit_with_duppata.jpg"},
]

# 4. Helper Functions
def add_to_cart(product):
    st.session_state.cart.append(product)
    st.toast(f"Added {product['name']} to cart!")

# 5. Sidebar - Shopping Cart View
with st.sidebar:
    st.header("🛒 Your Cart")
    if not st.session_state.cart:
        st.write("Your cart is empty.")
    else:
        total = 0
        for item in st.session_state.cart:
            st.write(f"{item['name']} - ${item['price']}")
            total += item['price']
        st.divider()
        st.subheader(f"Total: ${total:.2f}")
        if st.button("Clear Cart"):
            st.session_state.cart = []
            st.rerun()

# 6. Main Gallery Section
st.title("🛍️ Krishiv Mini Shop")
st.markdown("Welcome to our store! Browse products below.")

# Display products in a grid (using columns)
cols = st.columns(len(products))

for i, product in enumerate(products):
    with cols[i]:
        st.image(product['image'], use_container_width=True,caption="Click this image to visit Streamlit",
    link=f"/gallery?id={product['id']}&product={product['name']}")
        st.subheader(product['name'])
        st.write(f"Price: **${product['price']}**")
        if st.button(f"Add to Cart", key=f"btn_{product['id']}"):
            add_to_cart(product)


# 7. Checkout Section
st.divider()
if st.session_state.cart:
    st.header("Checkout")
    with st.expander("Finalize Order"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        if st.button("Complete Purchase"):
            if name and email:
                st.success(f"Thank you, {name}! Your order is being processed.")
                st.session_state.cart = [] # Reset cart after purchase
            else:
                st.error("Please fill in your details.")
