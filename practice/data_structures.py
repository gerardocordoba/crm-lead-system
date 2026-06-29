leads_today = ["Carlos Nunez", "Maria Lopez", "Juan Perez", "Ana Torres"]
crm_channels = ("branch", "call_center", "digital", "referral")
lead = {
    "cif": 123,
    "name": "Carlos Nunez",
    "product": "POS",
    "segment": "Micro",
    "score": 87,
    "is_eligible": True,
    "monthly_sales": 10000.00
}
products_applied = {"POS", "personal_loan", "POS", "credit_card"}

print(leads_today)
print(crm_channels)
print(lead)
print(products_applied)

print(type(leads_today))
print(type(crm_channels))
print(type(lead))
print(type(products_applied))