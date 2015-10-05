class RockPaperScissors

  # Exceptions this class can raise:
  class NoSuchStrategyError < StandardError ; end

  def self.winner(player1, player2)
    # YOUR CODE HERE
    p1=player1[1]
    p2=player2[1]
    if p1==p2
      return player1
    elsif (p1=="P" and p2=="R") or (p1=="R"and p2=="S") or (p1=="S"and p2=="P")
      return player1
    elsif (p2=="P" and p1=="R") or (p2=="R"and p1=="S") or (p2=="S"and p1=="P")
      return player2
    else
      raise RockPaperScissors::NoSuchStrategyError ,"Strategy must be one of R,P,S"
    end
  end

  def self.tournament_winner(tournament)
    # YOUR CODE HERE
    if tournament[0][0].is_a?(String)
      return self.winner(tournament[0],tournament[1])
    else
      return self.winner(self.tournament_winner(tournament[0][0]), self.tournament_winner(tournament[0][1]))
    end

  end
end
