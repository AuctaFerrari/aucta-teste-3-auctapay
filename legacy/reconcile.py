from datetime import date


def reconcile_records(titles, payments):
    results = []
    for title in titles:
        candidate = next(
            (
                payment
                for payment in payments
                if payment.get("documento") == title.get("documento")
                and abs(payment["valor"] - title["valor"]) <= 5.00
            ),
            None,
        )
        results.append(
            {
                "title_id": title["title_id"],
                "payment_id": candidate["payment_id"] if candidate else None,
                "status": "APPROVED" if candidate else "OPEN",
                "processed_on": date.today().isoformat(),
            }
        )
    return results
