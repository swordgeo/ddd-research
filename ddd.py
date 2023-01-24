import itertools





def fourDieChoiceSpread(die_set_list):

  nested_pairs_list = []

  #I've tried cheesing this but don't know how.
  #We'll do this manually for four dice and cry when it comes to five.
  for die_set in die_set_list:
    #1+2 3+4
    roll_one = die_set[0] + die_set[1]
    roll_two = die_set[2] + die_set[3]
    #1+3 2+4
    roll_three = die_set[0] + die_set[2]
    roll_four = die_set[1] + die_set[3]
    #1+4 2+3
    roll_five = die_set[0] + die_set[3]
    roll_six = die_set[1] + die_set[2]

    nested_pairs_list.append(((roll_one, roll_two), (roll_three, roll_four), (roll_five, roll_six)))

  return nested_pairs_list

def fiveDieChoiceSpread(die_set_list):

  nested_pairs_list = []

  #I've tried cheesing this but don't know how.
  #We'll do this manually for four dice and cry when it comes to five.
  for die_set in die_set_list:
    
    roll_one_two = die_set[0] + die_set[1]
    roll_one_three = die_set[0] + die_set[2]
    roll_one_four = die_set[0] + die_set[3]
    roll_one_five = die_set[0] + die_set[4]

    roll_two_three = die_set[1] + die_set[2]
    roll_two_four = die_set[1] + die_set[3]
    roll_two_five = die_set[1] + die_set[4]

    roll_three_four = die_set[2] + die_set[3]
    roll_three_five = die_set[2] + die_set[4]

    roll_four_five = die_set[3] + die_set[4]
    
    nested_pairs_list.append(((roll_one_five, roll_two_three), (roll_one_five, roll_two_four),  (roll_one_five, roll_three_four), (roll_two_five, roll_one_three), (roll_two_five, roll_one_four), (roll_two_five, roll_three_four), (roll_three_five, roll_one_two), (roll_three_five, roll_one_four), (roll_three_five, roll_two_four), (roll_four_five, roll_one_two), (roll_four_five, roll_one_three), (roll_four_five, roll_two_three), (roll_one_two, roll_three_four),(roll_one_three, roll_two_four), (roll_one_four, roll_two_three)))

  return nested_pairs_list


def oddsIndividual(x, nested_pairs_list):

  # Initialize a variable to store the count of the value x
  count = 0

  # Initialize a variable to store the total number of values
  total = 0

  break_out_flag = False

  # Iterate over the outermost level of the nested list
  for outer in nested_pairs_list:
    # Iterate over the second level of the nested list
    total += 1
    for inner in outer:
      #reset flag
      break_out_flag = False

      # Iterate over each number of the pair
      for number in inner:
        #if the number is the target, break out (we don't care if both numbers are the target)
        if number == x:
            break_out_flag = True
            break
      if break_out_flag:
        count += 1
        break
  # Calculate the odds by dividing the count by the total
  odds = count / total
  print(f"count {count} total {total}")
  # Print the resulting odds
  return odds

def oddsDoubles(die_set_list):

  # Initialize a variable to store the count of the value 8
  count = 0
  # Initialize a variable to store the total number of values
  total = 0

  for quad in die_set_list:
    break_out_flag = False
    total += 1
    for die in quad:
      if quad.count(die) > 1:
        break_out_flag = True
        break
    if break_out_flag:
      count += 1
      
  # Calculate the odds by dividing the count by the total
  odds = count / total
  #print(f"count {count} total {total}")
  # Print the resulting odds
  return odds

def oddsConditional(x, y, nested_pairs_list):

  # Initialize a variable to store the count of the value x
  count = 0

  # Initialize a variable to store the total number of values
  total = 0

  break_out_flag = False

  # Iterate over the outermost level of the nested list
  for outer in nested_pairs_list:
    # Iterate over the second level of the nested list
    
    for inner in outer:
      #reset flag
      break_out_flag = False

      # Iterate over each number of the pair
      for number in inner:
        #if the number is the target, break out (we don't care if both numbers are the target)
        if number == x:
            total += 1

          #is this the first die or second die?
          







            break_out_flag = True
            break
      if break_out_flag:
        count += 1
        break
  # Calculate the odds by dividing the count by the total
  odds = count / total
  print(f"count {count} total {total}")
  # Print the resulting odds
  return odds

    

# Create a list of all possible outcomes for each dice
outcomes = [1, 2, 3, 4, 5, 6]

#fake list for verification
#die_set_list = ((1, 2, 3, 4), (1, 1, 2, 3), (1, 1, 3, 3), (5, 6, 1, 3), (5, 6, 1, 3), (5, 1, 2, 5), (6, 2, 3, 4), (6, 3, 4, 5), (2, 3, 2, 5))

#fake list for verificiation
#nested_pairs_list = (((8, 6), (7, 7), (11, 3)), ((8, 7), (7, 8), (12, 3)), ((8, 3), (8, 3), (7, 4)), ((8, 4), (8, 4), (8, 4)), ((8, 5), (8, 5), (9, 4)), ((8, 6), (8, 6), (10, 4)), ((8, 7), (8, 7), (11, 4)), ((8, 8), (8, 8), (12, 4)), ((8, 4), (9, 3), (7, 5)), ((8, 5), (9, 4), (8, 5)), ((8, 6), (9, 5), (9, 5)))

# Use itertools.product to generate all possible combinations of the outcomes
four_die_list = list(itertools.product(outcomes, repeat=4))
four_pairs_list = fourDieChoiceSpread(four_die_list)

five_die_list = list(itertools.product(outcomes, repeat=5))
five_pairs_list = fiveDieChoiceSpread(five_die_list)

print(f"Four die stats:")
print(f"2: {oddsIndividual(2, four_pairs_list)*100:.2f}%")
print(f"3: {oddsIndividual(3, four_pairs_list)*100:.2f}%")
print(f"4: {oddsIndividual(4, four_pairs_list)*100:.2f}%")
print(f"5: {oddsIndividual(5, four_pairs_list)*100:.2f}%")
print(f"6: {oddsIndividual(6, four_pairs_list)*100:.2f}%")
print(f"7: {oddsIndividual(7, four_pairs_list)*100:.2f}%")
print(f"8: {oddsIndividual(8, four_pairs_list)*100:.2f}%")
print(f"9: {oddsIndividual(9, four_pairs_list)*100:.2f}%")
print(f"10: {oddsIndividual(10, four_pairs_list)*100:.2f}%")
print(f"11: {oddsIndividual(11, four_pairs_list)*100:.2f}%")
print(f"12: {oddsIndividual(12, four_pairs_list)*100:.2f}%")
print(f"Doubles: {oddsDoubles(four_die_list)*100:.2f}%")

print("")

print(f"Five die stats:")
print(f"2: {oddsIndividual(2, five_pairs_list)*100:.2f}%")
print(f"3: {oddsIndividual(3, five_pairs_list)*100:.2f}%")
print(f"4: {oddsIndividual(4, five_pairs_list)*100:.2f}%")
print(f"5: {oddsIndividual(5, five_pairs_list)*100:.2f}%")
print(f"6: {oddsIndividual(6, five_pairs_list)*100:.2f}%")
print(f"7: {oddsIndividual(7, five_pairs_list)*100:.2f}%")
print(f"8: {oddsIndividual(8, five_pairs_list)*100:.2f}%")
print(f"9: {oddsIndividual(9, five_pairs_list)*100:.2f}%")
print(f"10: {oddsIndividual(10, five_pairs_list)*100:.2f}%")
print(f"11: {oddsIndividual(11, five_pairs_list)*100:.2f}%")
print(f"12: {oddsIndividual(12, five_pairs_list)*100:.2f}%")
print(f"Doubles: {oddsDoubles(five_die_list)*100:.2f}%")

#print(f"{oddsIndividual(2, nested_pairs_list)+oddsIndividual(3, nested_pairs_list)+oddsIndividual(4, nested_pairs_list)+oddsIndividual(5, nested_pairs_list)+oddsIndividual(6, nested_pairs_list)+oddsIndividual(7, nested_pairs_list)+oddsIndividual(8, nested_pairs_list)+oddsIndividual(9, nested_pairs_list)+oddsIndividual(10, nested_pairs_list)+oddsIndividual(11, nested_pairs_list)+oddsIndividual(12, nested_pairs_list)}")




# #query
# #Now, in each pair of numbers in which one of the numbers is 8, what is it's corresponding partner most likely to be?

# # Assign the nested list to a variable
# nested_list = (((7, 6), (8, 5), (10, 3)), ((7, 7), (8, 6), (11, 3)), ((7, 8), (8, 7), (12, 3)), ((7, 4), (9, 2), (7, 4)))

# # Initialize a dictionary to store the count of each number that appears as a partner of an 8 in a tuple
# partner_counts = {}

# # Iterate over the outermost level of the nested list
# for outer in nested_list:
#   # Iterate over the second level of the nested list
#   for middle in outer:
#     # Iterate over the innermost level of the nested list
#     for inner in middle:
#       # If the inner value is 8, increment the count of its partner in the dictionary
#       if inner == 8:
#         partner = [x for x in middle if x != 8][0]
#         if partner not in partner_counts:
#           partner_counts[partner] = 1
#         else:
#           partner_counts[partner] += 1

# # Find the number with the highest count in the dictionary
# most_common_partner = max(partner_counts, key=partner_counts.get)

# # Print the most common partner of an 8
# #print(most_common_partner)


# #query
# #For every pair of values that contains an 8, what are the odds for every other value partnered with that 8?

# # Assign the nested list to a variable
# nested_list = (((7, 6), (8, 5), (10, 3)), ((7, 7), (8, 6), (11, 3)), ((7, 8), (8, 7), (12, 3)), ((7, 4), (9, 2), (7, 4)))

# # Initialize a dictionary to store the count of each number that appears as a partner of an 8 in a tuple
# partner_counts = {}

# # Initialize a variable to store the total number of values that are 8
# total_count = 0

# # Iterate over the outermost level of the nested list
# for outer in nested_list:
#   # Iterate over the second level of the nested list
#   for middle in outer:
#     # Iterate over the innermost level of the nested list
#     for inner in middle:
#       # If the inner value is 8, increment the count of its partner in the dictionary and the total count
#       if inner == 8:
#         partner = [x for x in middle if x != 8][0]
#         if partner not in partner_counts:
#           partner_counts[partner] = 1
#         else:
#           partner_counts[partner] += 1
#         total_count += 1

# # Calculate the odds for each number by dividing its count by the total count
# odds = {key: value / total_count for key, value in partner_counts.items()}

# # Print the odds for each number
# print(odds)