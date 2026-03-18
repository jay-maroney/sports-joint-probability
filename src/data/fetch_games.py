import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder

def get_games(season = '2024-25'):
    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable = season
    )
    games = gamefinder.get_data_frames()[0]
    
    games = games[[
        'GAME_ID',
        'TEAM_ID',
        'TEAM_ABBREVIATION',
        'GAME_DATE',
        'MATCHUP',
        'WL',
        'PTS',
        'REB',
        'AST'
    ]]

    return games

def add_game_features(games_df):
    merged = games__df.merge(
        games_df,
        on = 'GAME_ID',
        suffixes = ('', '_opp')
    )

    merged = merged[merged['TEAM_ID'] != merged['TEAM_ID_opp']]

    merged = merged['point_diff'] = merged['PTS'] - merged['PTS_opp']
    merged['blowout'] = (merged['point_diff'] > 15).astype(int)

    return merged
