def build_sales_report(raw: str) -> str:
    header = f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"
    rows = []
    grand_total = 0.0
    bytes_total = 0

    for line in raw.splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        fields = line.split(",")

        if len(fields) != 3:
            continue

        item, quantity, price = [field.strip() for field in fields]

        if not quantity.isdigit():
            continue

        quantity = int(quantity)
        price = float(price)

        item = item.title()[:12]
        line_total = quantity * price

        bytes_total += len(item.encode("utf-8"))
        grand_total += line_total

        row = (
            f"{item:<12}"
            f"{quantity:>4}"
            f"{price:>10.2f}"
            f"{line_total:>12,.2f}"
        )

        rows.append(row)

    separator = "-" * 38
    total_line = f"{'TOTAL':<26}{grand_total:>12,.2f}"
    summary = f"Rows: {len(rows)} | UTF-8 bytes in items: {bytes_total}"

    return "\n".join([header] + rows + [separator, total_line, summary])
