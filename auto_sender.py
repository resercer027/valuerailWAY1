from flashscore_scraper import get_flashscore_bets
from oddsportal_scraper import get_oddsportal_bets
from value_calc import calculate_value_bets

def run_combined_scrapers():
    bets = get_flashscore_bets() + get_oddsportal_bets()
    return calculate_value_bets(bets)
