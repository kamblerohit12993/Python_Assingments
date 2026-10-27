#  Mobile Data Plan Bill

customer_name = input("Enter customer name: ")
plan_type = input("Enter plan type (Basic/Standard/Premium): ").lower()
extra_data = float(input("Enter extra data used in GB: "))

if extra_data < 0:
    print("Invalid data usage!")

elif plan_type not in ["basic", "standard", "premium"]:
    print("Invalid plan type!")

else:
    if plan_type == "basic":
        base_charge = 299

    elif plan_type == "standard":
        base_charge = 499

    else:
        base_charge = 799

    extra_data_charge = extra_data * 20

    if extra_data > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base_charge + extra_data_charge + surcharge

    print("\n----- Mobile Data Bill -----")
    print("Customer Name:", customer_name)
    print("Plan Type:", plan_type.capitalize())
    print("Base Plan Charge: Rs.", base_charge)
    print("Extra Data Used:", extra_data, "GB")
    print("Extra Data Charge: Rs.", extra_data_charge)
    print("Surcharge: Rs.", surcharge)
    print("Final Bill: Rs.", final_bill)
