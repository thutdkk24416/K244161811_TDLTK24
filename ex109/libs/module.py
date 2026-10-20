# libs/module.py

def calculate_original_price(purchase_price, transport_fee, install_fee):
    """Tính Nguyên giá TSCĐ"""
    return purchase_price + transport_fee + install_fee


def calculate_annual_depreciation(original_price, years):
    """Tính Mức trích khấu hao năm"""
    if years <= 0:
        return 0
    return original_price / years


def calculate_monthly_depreciation(annual_depreciation):
    """Tính Mức trích khấu hao tháng"""
    return annual_depreciation / 12


def calculate_detailed_depreciation(original_price, annual_depreciation, years):
    """Tính chi tiết khấu hao từng năm"""
    details = []
    remaining_value = original_price

    for year in range(1, int(years) + 1):
        remaining_value -= annual_depreciation
        # Đảm bảo năm cuối cùng giá trị còn lại bằng 0 để thuật toán chính xác theo yêu cầu
        if year == int(years) or remaining_value < 0:
            remaining_value = 0

        details.append({
            "year": year,
            "remaining": remaining_value
        })
    return details