# Let's create an ER diagram based on the prompt provided.
# We'll represent the entities, relationships, and attributes.

from eralchemy import render_er

# Creating a model for the ER diagram in markdown format
er_diagram_code = """
[Customer] {
    user_id (PK)
    password
    mobile_number
    name
    gender
    date_of_birth
    address
    customer_level (Derived)
    mypay_balance
}

[Worker] {
    user_id (PK)
    password
    mobile_number
    name
    gender
    date_of_birth
    address
    bank_name
    account_number
    NPWP
    profile_picture
    completed_orders (Derived)
    rating (Derived)
    mypay_balance
}

[ServiceCategory] {
    category_id (PK)
    category_name
}

[ServiceSubcategory] {
    subcategory_id (PK)
    subcategory_name
    description
    price_per_session
}

[ServiceOrderTransaction] {
    transaction_id (PK)
    order_date
    job_date
    job_time
    service_fee
    discount_code
    worker_name
    admin_fee
    total_cost (Derived)
    payment_method_code (FK)
}

[Voucher] {
    voucher_code (PK)
    voucher_name
    voucher_price
    discount_amount
    min_transaction_value
    usage_limit
    validity_period
}

[Promo] {
    promo_code (PK)
    discount_amount
    min_transaction_value
    offer_expiration_date
}

[PaymentMethod] {
    payment_method_code (PK)
    payment_method_name
}

[MyPayTransaction] {
    transaction_id (PK)
    transaction_date
    amount
    transaction_category (FK)
}

[OrderStatus] {
    status_id (PK)
    status_name
    status_date_time
}

[Testimonial] {
    testimonial_date
    worker_name
    rating
    comments
}

[Customer] ||--o{ [ServiceOrderTransaction]: "places"
[Worker] ||--o{ [ServiceOrderTransaction]: "completes"
[ServiceCategory] ||--o{ [ServiceSubcategory]: "includes"
[ServiceOrderTransaction] ||--o{ [OrderStatus]: "has"
[ServiceOrderTransaction] ||--o{ [Testimonial]: "generates"
[PaymentMethod] ||--o{ [ServiceOrderTransaction]: "used in"
[Customer] ||--o{ [MyPayTransaction]: "performs"
[Worker] ||--o{ [MyPayTransaction]: "receives"
[Worker] ||--o{ [ServiceCategory]: "belongs to"
"""

# Generating the ER diagram
output_path = '/mnt/data/sijarta_er_diagram.png'
render_er(er_diagram_code, output_path)

output_path
