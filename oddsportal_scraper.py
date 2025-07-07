import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_oddsportal_bets():
    # URL reale omesso: struttura simulata
    # Per scraping reale serve parsing avanzato o API
    raw_data = [
        {
            'match': 'Roma - Milan',
            'market': '1',
            'bookmaker_odds': 2.20,
            'avg_odds': 2.05,
            'date_raw': '10 Jul 2025, 20:45',
            'bookmaker': 'Snai'
        },
        {
            'match': 'Inter - Napoli',
            'market': '2',
            'bookmaker_odds': 3.40,
            'avg_odds': 3.10,
            'date_raw': '11 Jul 2025, 21:00',
            'bookmaker': 'Bet365'
        },
        {
            'match': 'Atalanta - Salernitana',
            'market': '2',
            'bookmaker_odds': 8.00,
            'avg_odds': 100.0,
            'date_raw': '11 Jul 2025, 15:00',
            'bookmaker': 'Unibet'
        }
    ]

    bets = []

    for b in raw_data:
        try:
            avg_prob = 1 / b['avg_odds']
            value = (b['bookmaker_odds'] * avg_prob - 1) * 100

            if avg_prob < 0.01 or value <= 3:
                continue  # scarta match non giocabili o con value basso

            dt = datetime.strptime(b['date_raw'], "%d %b %Y, %H:%M")
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
