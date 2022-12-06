import streamlit as st
import pandas as pd

def get_Data(filename):
        data = pd.read_csv(filename)
        return data

def Customer():

    header = st.container()
    inputs = st.container()

    with header:

        st.title("Customer Information")
        st.text("Input and access customer information.")

    with inputs:

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Data input")

            Name = str(st.text_input("Enter customer name: "))
            Address = st.text_input("Enter customer address: ")
            Phone_Number = st.text_input("Enter customer phone number: ")

            customer_input_btn = st.button("Submit")
            if customer_input_btn:

                customers_Dataset = get_Data('customers.csv')
                all_Customers = list(customers_Dataset.iloc[:,0])
                index = 0
                count = int(len(all_Customers) - 1)
                
                if Name != all_Customers[index]:
                    for clients in all_Customers:
                        while Name != all_Customers[index]:
                            if index == count:
                                break
                            else:
                                index += 1

                if Name == all_Customers[index]:

                    current_Customer = Name
                    st.error(f"Known customer: {current_Customer}")

                    def update_Customer_Data():

                        df = get_Data('customers.csv') 

                        df.loc[index, 'NOMBRE   '] = Name
                        df.loc[index, 'DIRECCION   '] = Address
                        df.loc[index, 'CELULAR'] = Phone_Number
                        
                        df.to_csv('customers.csv',index=False)

                    update_Customer_Data()

                else:
                    new_data = [[Name, Address, Phone_Number]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('customers.csv', mode='a', index=False, header=False)

                    current_Customer = Name
                    st.error(f"New customer: {current_Customer}")

        with col2:

            st.subheader("Customer dataset")
            st.text("Table containing customer information: ")

            st.write(customers_Dataset)

def Product():

    header = st.container()
    inputs = st.container()

    with header:

        st.title("Product Information")
        st.text("Input and access product information.")

    with inputs:

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Data input")

            Name = st.text_input("Enter product name: ")
            Stock = st.slider("Enter product stock: ")
            Price = st.number_input("Enter product price: ", step=100)

            product_input_btn = st.button("Submit")
            if product_input_btn:

                products_Dataset = get_Data('products.csv')
                all_Products = list(products_Dataset.iloc[:,0])
                index = 0
                count = int(len(all_Products) - 1)
                
                if Name != all_Products[index]:
                    for clients in all_Products:
                        while Name != all_Products[index]:
                            if index == count:
                                break
                            else:
                                index += 1

                if Name == all_Products[index]:
                    current_Product = Name
                    st.error(f"Known product: {current_Product}")

                    def update_Product_Data():

                        df = get_Data('products.csv') 

                        df.loc[index, 'NOMBRE    '] = Name
                        df.loc[index, 'STOCK'] = Stock
                        df.loc[index, 'PRECIO'] = Price
                        
                        df.to_csv('products.csv',index=False)

                    update_Product_Data()

                else:
                    new_data = [[Name, Stock, Price]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('products.csv', mode='a', index=False, header=False)

                    current_Product = Name
                    st.error(f"New Product: {current_Product}")

        with col2:

            st.subheader("Product dataset")
            st.text("Table containing product information: ")

            st.write(products_Dataset)

def Discount():

    header = st.container()
    inputs = st.container()

    with header:

        st.header("Discount Information")
        st.text("Input and access discount information.")

    with inputs:

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Data Input")

            Name = st.text_input("Enter discount name: ")
            Reason = st.text_input("Enter discount reason: ")
            Percentage = st.slider("Discount", 5, 100, step=5)
            
            discounts_Dataset = pd.read_csv('discounts.csv')
            all_Discounts = list(discounts_Dataset.iloc[:,0])
            index = 0
            count = int(len(all_Discounts) - 1)
            
            if Name != all_Discounts[index]:
                for discount in all_Discounts:
                    while Name != all_Discounts[index]:
                        if index == count:
                            break
                        else:
                            index += 1

            if Name == all_Discounts[index]:

                current_Discount = Name
                st.error(f"Known discount: {current_Discount}")

                def update_Discount_Data():

                    df = get_Data('discounts.csv') 

                    df.loc[index, 'NOMBRE   '] = Name
                    df.loc[index, 'DESCUENTO'] = Percentage
                    df.loc[index, 'MOTIVO'] = Reason
                    
                    df.to_csv('discounts.csv',index=False)

                update_Discount_Data()

            else:
                new_data = [[Name, Percentage, Reason]]
                df = pd.DataFrame(new_data)
                df.to_csv('discounts.csv', mode='a', index=False, header=False)

                current_Customer = Name
                st.error(f"New discount: {current_Customer}")

        with col2:

            st.subheader("Discounts Dataset")
            st.text("Table containing discount infomation:")

            st.write(discounts_Dataset)

def Purchase():

    st.title("Purchase Information")

    columns = st.container()

    with columns:

        col1, col2, col3 = st.columns(3)

        with col1:

            st.subheader("Customer Info.")
            current_Customer = str(st.text_input("Enter customer name: "))

            def get_Customer_Data():

                customers_Dataset = pd.read_csv('customers.csv')
                all_Customers = list(customers_Dataset.iloc[:,0])
                index = 0
                count = int(len(all_Customers) - 1)
                
                if current_Customer != all_Customers[index]:
                    for clients in all_Customers:
                        while current_Customer != all_Customers[index]:
                            if index == count:
                                break
                            else:
                                index += 1

                if current_Customer == all_Customers[index]:

                    def get_Address():

                        all_Addresses = list(customers_Dataset.iloc[:,1])
                        current_Address = all_Addresses[index]
                        st.text("Address: ")
                        st.text(current_Address)

                    get_Address()

                    def get_Phone_Number():

                        all_Phone_Numbers = list(customers_Dataset.iloc[:,2])
                        current_Phone_Number = all_Phone_Numbers[index]
                        st.text(f"Phone Number: {current_Phone_Number}")

                    get_Phone_Number()

                else:
                    st.text("")

            get_Customer_Data()

        with col2:

            st.subheader("Product Info.")
            current_Product = st.text_input("Enter product name: ")
            amount = int(st.slider("Amount", 1, 50))

            def get_Product_Data():

                products_Dataset = pd.read_csv('products.csv')
                all_Products = list(products_Dataset.iloc[:,0])
                index = 0
                count = int(len(all_Products) - 1)
                
                if current_Product != all_Products[index]:
                    for clients in all_Products:
                        while current_Product != all_Products[index]:
                            if index == count:
                                break
                            else:
                                index += 1

                if current_Product == all_Products[index]:

                    def get_Price():

                        all_Prices = list(products_Dataset.iloc[:,2])
                        global current_Price
                        current_Price = int(all_Prices[index])
                        st.text(f"Price: {current_Price}")

                    get_Price()

                    def get_Stock():

                        all_Stocks = list(products_Dataset.iloc[:,1])
                        global current_Stock
                        current_Stock = all_Stocks[index]

                    get_Stock()

                    def update_Stock():

                        stock = int(current_Stock - amount)

                        df = get_Data('products.csv') 
                        df.loc[index, 'STOCK'] = stock
                        df.to_csv('products.csv',index=False)

                    # update_Stock()

                    def calculate_Price():

                        net_price = int(current_Price * amount)
                        st.text(f"Total: {net_price}")

                    calculate_Price()

                else:
                    st.text("")

            get_Product_Data()

        with col3:
            st.subheader("Payment Info.")
            method = st.selectbox("Select payment method", ['cash', 'debit', 'credit'])
            cuotas = st.slider("Cuotas", 1, 12)
            discount = st.selectbox("Select discount", ['None', 'Itau(25%)'])
            
all_Pages = {
    "Customer": Customer,
    "Product": Product,
    "Discount": Discount,
    "Purchase": Purchase
}

st.sidebar.title("Python Website")
st.sidebar.header("Databse structure")

selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
all_Pages[selected_page]()
