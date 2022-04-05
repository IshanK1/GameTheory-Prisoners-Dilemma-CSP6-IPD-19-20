# csp6-IPD-19-20

## Ishan Kachroo (Game Theory Project)

This class project is about implementing strategies for the [Prisoner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma) problem. The class is divided into small teams and each team comes up with a strategy on when to betray or collude. **The strategy implemented by my team was:**

```
- Collude, unless there are 2 consecutive betrayals from opponent, in which case, betray.  
- Switch from betray to collude, if there are 2 consecutive colludes from opponent.
```

Some of the other interesting strategies suggested were:

1. Keep colluding until your score is just below the opponent, then start betraying
2. Look at opponent's history; if there are more than 70% collusions, collude, otherwise betray.
