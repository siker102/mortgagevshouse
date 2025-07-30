import streamlit as st

st.title("Mortgage / House Buying Calculator")

st.header("Input Parameters")

def format_k(n):
    if n >= 1000:
        return f"€{n/1000:.1f}k"
    return f"€{n}"

home_price = st.number_input(
    "Home Price (€)", min_value=0, value=300000, step=1000
)
st.caption(f"Home Price: {format_k(home_price)}")

down_payment = st.number_input("Down Payment Or Starting Investment(€)", min_value=0, value=60000, step=1000)
st.caption(f"Down Payment: {format_k(down_payment)}")

loan_term = st.number_input("Loan Term (years)", min_value=1, value=30, step=1)

interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=3.5, step=0.01, format="%.2f")

property_tax = st.number_input("Annual Property Tax (€)", min_value=0, value=0, step=100)
st.caption(f"Annual Property Tax: {format_k(property_tax)}")

home_insurance = st.number_input("Annual Home Insurance (€)", min_value=0, value=0, step=100)
st.caption(f"Annual Home Insurance: {format_k(home_insurance)}")

house_appreciation_rate = st.number_input(
    "Average House Value Increase (%)", min_value=0.0, value=2.0, step=0.01, format="%.2f"
)
st.caption(f"Average House Value Increase: {house_appreciation_rate:.2f}%")

st.header("Investment Scenario (Instead of Buying)")

monthly_rent = st.number_input("Monthly Rent You Would Pay(€)", min_value=0, value=0, step=10)
st.caption(f"Monthly Rent: {format_k(monthly_rent)}")

rent_increase_rate = st.number_input(
    "Average Rent Increase Rate (%)", min_value=0.0, value=2.0, step=0.01, format="%.2f"
)

investment_return_rate = st.number_input(
    "Average Investment Return Rate (%)", min_value=0.0, value=7.0, step=0.01, format="%.2f"
)
st.caption(f"Average Investment Return Rate: {investment_return_rate:.2f}%")

st.header("Other Parameters")

inflation_rate = st.number_input(
    "Annual Inflation Rate (%)", min_value=0.0, value=2.0, step=0.01, format="%.2f"
)
selling_horizon = st.number_input(
    "Years Before Selling Home", min_value=1, value=30, step=1
)

st.header("Additional Home Ownership Costs")

transaction_costs_buy = st.number_input(
    "Home Purchase Transaction Costs (%)", min_value=0.0, value=5.0, step=0.1, format="%.2f"
)
transaction_costs_sell = st.number_input(
    "Home Selling Transaction Costs (%)", min_value=0.0, value=5.0, step=0.1, format="%.2f"
)
maintenance_cost = st.number_input(
    "Annual Maintenance/Repairs (€)", min_value=0, value=3000, step=100
)
hoa_fee = st.number_input(
    "Annual HOA Fees (€)", min_value=0, value=0, step=100
)
mortgage_insurance = st.number_input(
    "Annual Mortgage Insurance (€)", min_value=0, value=0, step=100
)

st.header("Investment/Renting Costs")

renters_insurance = st.number_input(
    "Annual Renters Insurance (€)", min_value=0, value=0, step=100
)
investment_tax_rate = st.number_input(
    "Investment Tax Rate (%)", min_value=0.0, value=0.0, step=0.01, format="%.2f"
)

st.header("Summary of Inputs")
st.write(f"Home Price: €{home_price:,.2f}")
st.write(f"Down Payment: €{down_payment:,.2f}")
st.write(f"Loan Term: {loan_term} years")
st.write(f"Interest Rate: {interest_rate:.2f}%")
st.write(f"Annual Property Tax: €{property_tax:,.2f}")
st.write(f"Annual Home Insurance: €{home_insurance:,.2f}")
st.write(f"Monthly Rent: €{monthly_rent:,.2f}")
st.write(f"Home Purchase Transaction Costs: {transaction_costs_buy:.2f}%")
st.write(f"Home Selling Transaction Costs: {transaction_costs_sell:.2f}%")
st.write(f"Annual Maintenance/Repairs: €{maintenance_cost:,.2f}")
st.write(f"Annual HOA Fees: €{hoa_fee:,.2f}")
st.write(f"Annual Mortgage Insurance: €{mortgage_insurance:,.2f}")
st.write(f"Annual Inflation Rate: {inflation_rate:.2f}%")
st.write(f"Years Before Selling Home: {selling_horizon}")
st.write(f"Annual Renters Insurance: €{renters_insurance:,.2f}")
st.write(f"Investment Tax Rate: {investment_tax_rate:.2f}%")