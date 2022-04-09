# given a list of salaries, take the bonus and increase the salaries by the amount 
# solution 1 using for in racket
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input("what is the bonus?"))
salaries = [x+bonus for x in salaries]
print(salaries)
# solution 2 use map function
salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input("what is the bonus?"))
def add_bonus(x):
    return x + bonus
result = list(map(add_bonus, salaries))
print(result)