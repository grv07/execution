import itertools

class Furui:

  def __init__(self):
    # Object constants
    self.student = "John"
    self.mue = 0.48
    self.nul = 0.08
    self.possible_a_b_val = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9, 1]

  def get_a_b_pc(self):
    return itertools.permutations(self.possible_a_b_val, 2)

  def get_threshold(self, c):
    p =  ((c[0]*(self.mue + self.nul)) + c[1])
    print('for permutation: ', c)
    print('threshold is: ', p)
    return p

  def get_min_threshold(self):
    #alpha_beta_combinations
    a_b_permutation = self.get_a_b_pc()
    min_temp = self.get_threshold(a_b_permutation.next())
    for c in a_b_permutation:
      new_x = self.get_threshold(c)
      print(new_x, min_temp)
      if new_x < min_temp:
        min_temp = new_x
    return min_temp

if __name__ == "__main__":
   p = Furui()
   print('Min. threshold is: ',p.get_min_threshold())
