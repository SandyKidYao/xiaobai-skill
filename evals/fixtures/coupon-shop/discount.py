"""简易优惠券计算模块。"""

# 券码 -> (满足金额, 减免金额)
COUPONS = {
    "FULL100_10": (100, 10),
    "FULL200_30": (200, 30),
    "FULL500_80": (500, 80),
}


def apply_coupon(total: float, code: str) -> float:
    """对订单金额应用满减券,返回应付金额。"""
    if code not in COUPONS:
        raise ValueError("invalid coupon")
    threshold, off = COUPONS[code]
    if total > threshold:
        return total - off
    return total
