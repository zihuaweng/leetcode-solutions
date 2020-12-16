import os

input = "124. Binary Tree Maximum Path Sum"
website = "// https://leetcode.com/problems/binary-tree-maximum-path-sum/"

surfix = [
  ["java", "leetcode_java"], 
  ["cpp", "leetcode_cpp"], 
  ["go", "leetcode_go"]
  ]

input = input.replace(". ", ".")
input = input.replace(" ", "_") + "."

for s, folder in surfix:
  cur_folder = os.getcwd()
  file_name = os.path.join(cur_folder, folder, input + s)
  with open(file_name, "w") as f:
    f.write(website)
  