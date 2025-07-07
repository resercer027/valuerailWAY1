def calculate_value_bets(bets):
    filtered = []
    for b in bets:
        try:
            value_percent = (b['odds'] / b['estimated_prob'] - 1) * 100
            if value_percent > 3:
                filtered.append(
                    f"Value Bet Trovata!\n"
                    f"Partita: {b['match']}\n"
                    f"Mercato: {b['market']}\n"
                    f"Quota: {b['odds']}\n"
                    f"Probabilità stimata: {b['estimated_prob']}\n"
                    f"Value stimato: +{round(value_percent, 1)}%\n"
                    f"Bookmaker: {b['bookmaker']}"
                )
        except (ZeroDivisionError, KeyError):
            continue
    return filtered
