from  abc import ABC 

class office (ABC):
  def scores(self):
    pass


class developer(office):
  def scores(self):
    hiddeninfo = 92
    print("score is excellent ")  

class testing(office):
  def scores(self):
    hiddeninfo = 97
    print("score is great ")   


class digital(office):
  def scores(self):
    hiddeninfo = 90
    print("score is very awesome ")           


a= developer()
a.scores()

b = digital()
b.scores()

c = testing()
c.scores()


