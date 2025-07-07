from datetime import datetime

def get_flashscore_bets():
    raw_data = [
        {
            'match': 'Juventus - Napoli',
            'market': 'Over 2.5',
            'bookmaker_odds': 2.10,
            'avg_odds': 1.95,
            'date_raw': '07.07. 20:45',
            'bookmaker': 'Bet365'
        },
        {
            'match': 'Lakers - Celtics',
            'market': '1X',
            'bookmaker_odds': 1.85,
            'avg_odds': 1.84,
            'date_raw': '07.07. 23:30',
            'bookmaker': 'Snai'
        },
        {
            'match': 'Napoli - Torino',
            'market': '2',
            'bookmaker_odds': 20.0,
            'avg_odds': 101.0,
            'date_raw': '09.07. 21:00',
            'bookmaker': 'GoldBet'
        }
    ]

    bets = []

    for b in raw_data:
        try:
            avg_prob = 1 / b['avg_odds']
            value = (b['bookmaker_odds'] * avg_prob - 1) * 100

            if avg_prob < 0.01 or value <= 3:
                continue  # scarta probabilità < 1% o value troppo basso

            dt = datetime.strptime(b['date_raw'], "%d.%m. %H:%M").replace(year=datetime.now().year)
            date_str = dt.strftime("%Y-%m-%d %H:%M")

            bets.append({
                'match': b['match'],
                'market': b['market'],
                'odds': b['bookmaker_odds'],
                'estimated_prob': round(avg_prob, 2),
                'value': round(value, 1),
                'bookmaker': b['bookmaker'],
                'date': date_str
            })
        except:
            continue

    return bets
