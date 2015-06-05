# GameRank
Implement a restful API that given a new score, add the score to the score database and return the percentage of the scores beaten by the new score.

You can try this api by running
curl -X POST -H "Content-Type: application/json" {base_url}/game/rank/{score}/

e.g.
curl -X POST -H "Content-Type: application/json" https://game-rank-gudu.c9.io/game/rank/25/

You can view all the existing score by running
curl {base_url}/game/rank/scores/

e.g. curl https://game-rank-gudu.c9.io/game/rank/scores