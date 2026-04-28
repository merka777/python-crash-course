n_voo = 1
voo_price = 656.47

n_amzn = 0.94488
amzn_price = 264.20

n_v = 0.41908
v_price = 309.39

n_meta = 0.18075
meta_price = 675.18 

cash = 57.32

voo_value = (n_voo*voo_price)
amzn_value = (n_amzn*amzn_price)+cash
v_value = (n_v*v_price)
meta_value = (n_meta*meta_price)
total = (voo_value+amzn_value+v_value+meta_value)

print(f"VOO:  ${voo_value}")
print(f"AMZN: ${amzn_value}")
print(f"V:    ${v_value}")
print(f"META: ${meta_value}")

print("-----------------------")

print(f"TOTAL BALANCE: ${total}")