# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part One
player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = player_one + ' ' + str(goal_0) + ', ' + player_two + ' ' + str(goal_1)
report = f'{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute'

# Part Two
player = 'Hans van Breukelen'
first_name = player[0:player.find(' ')]
last_name_len = len(player[player.find(' ') + 1:])
name_short = str(player[0] + '. ' + player[player.find(' ') + 1:])
chant = (first_name + '! ') * (len(first_name) - 1) + (first_name + '!')
good_chant = chant[-1] != ''