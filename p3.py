def get_score(low,high):
  score=float(input(f'enter the student score (between {low} and {high}:)'))
  if low <= score <= high:
    return score
  else:
    print(f'enter a value between {low} and {high}')
    return get_score(low,high)