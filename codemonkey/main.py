"""
There is a garden and it has 100 trees. In one of the trees there is a monkey.

This monkey is destroying the fruits on the trees.

Objective: Design an algorithm that can guarantee to find this monkey in one of the trees and catch him.

Catch: Every time you search a tree, the monkey jumps to the tree either to the right or the left.

"""

import random

class Monkey:
  def __init__(self, start_position, trees):
    self.pos = start_position
    trees[self.pos].has_monkey = True

  def jump_tree(self, trees):
    """
    The monkey will jump either one tree to the left or one tree to the right
    If there is no tree on the left, the monkey will always jump right and similarly
    if there is no tree on the right, the monkey will always jump left.
    """
    if self.pos == 0:
      jump_direction = 1
    elif self.pos == 99:
      jump_direction = -1
    else:
      jump_direction = random.choice([-1,1])

    trees[self.pos].has_monkey = False
    self.pos += jump_direction
    trees[self.pos].has_monkey = True


class Tree:
  def __init__(self):
    self.has_monkey = False

  def search_tree(self):
    if self.has_monkey == True:
      return True
    return False


class Garden:
  def __init__(self):
    self.trees = []
    for i in range(100):
      self.trees.append(Tree())
    self.monkey = Monkey(random.randint(0, 100), self.trees)

  def search_tree(self, index):
    print("Searching tree at index: {}".format(index))
    found = self.trees[index].search_tree()
    if not found:
      # The monkey will jump if it is not found
      self.monkey.jump_tree(self.trees)
    return found

def main():
  garden = Garden()
  # Implement your logic here.



  # End your logic here


main()
