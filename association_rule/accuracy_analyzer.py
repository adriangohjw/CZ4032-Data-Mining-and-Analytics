class AccuracyAnalyzer:

  def __init__(self, data):
    self.data = data

  
  def call(self, attribute):
    correct_guesses = self.data[
      (self.data[attribute] == self.data['guess'])
    ]

    return len(correct_guesses) / len(self.data)
