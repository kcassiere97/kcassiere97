def editDistance(str1, str2):

  rows = len(str1)
  cols = len(str2)
  # dist = [[0 for x in range(cols) + 1] for x in range(rows) + 1]
  dist = [[0 for i in range(cols + 1)] for j in range(rows + 1)]

  for i in range(1, rows):
    dist[i][0] = i

  for j in range(1,cols):
    dist[0][j] = j

  for i in range(1, rows + 1):
    
    for j in range(1, cols + 1):

      if str1[i - 1] == str2[j - 1]:
        dist[i][j] = dist[i - 1][j - 1]
      else:
        # Adding 1 to account for the cost of operation
        insertion = 1 + dist[i][j - 1]
        deletion = 1 + dist[i - 1][j]
        replacement = 1 + dist[i - 1][j - 1]

        # Choosing the best option:
        dist[i][j] = min(insertion, deletion, replacement)

      

  return (dist[len(str1)][len(str2)])

print("Enter String 1")
x = input()
print("Enter String 2")
y = input()

print("Edit Distance: ", editDistance(x,y),"\n")











