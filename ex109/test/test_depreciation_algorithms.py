from libs.module import *

def test_depreciation_algorithms(purchase, transport, install, years):
    original = calculate_original_price(purchase, transport, install)
    annual = calculate_annual_depreciation(original, years)

    print(f"Nguyên giá: {original}")
    print(f"Mức khấu hao năm: {annual}")

    details = calculate_detailed_depreciation(original, annual, years)
    for d in details:
        print(f"Năm {d['year']}, Sau khấu hao còn => {int(d['remaining'])}")

test_depreciation_algorithms(120000000, 5000000, 1000000, 10)