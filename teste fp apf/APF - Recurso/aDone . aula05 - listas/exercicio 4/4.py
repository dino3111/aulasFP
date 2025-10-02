def allMatches(teams):
   assert len(teams) >= 2, "Requires two or more teams!"
   games = []
   for team1 in teams:
      for team2 in teams:
         if team1 != team2:
            games.append((team1,team2))
   return games

x = allMatches(["A", "B", "C", "D"])
print(x)
y = allMatches(["FCP", "SCP", "SLB"])
print(y)
