
-- Old School Runescape League HighScores table 
CREATE TABLE league_hiscores (
    rank integer,
    name text primary key,
    level integer,
    exp integer
);

COMMENT ON TABLE league_hiscores IS 'This table contains the highschore rankings of "League" mode on Old School Runescape';

COMMENT ON COLUMN league_hiscores.rank IS 'The players numerical rank on the leaderboard.';

COMMENT ON COLUMN league_hiscores.name IS 'A unique name of a player.';

COMMENT ON COLUMN league_hiscores.level IS 'The level achieved by a player.';

COMMENT ON COLUMN league_hiscores.exp IS 'The experienced earned by a player.';

