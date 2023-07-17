import pickle

#  create a pickle file first (RUN THIS ONCE)
# scores = [('joe', 1), ('bill', 2), ('betty', 100)]


# create a pickle file for length (run ONCE)
# with open("length.dat", 'ab') as f:
  # pickle.dump(3, f)


with open('length.dat', 'rb') as f:
  length = int(pickle.load(f))

print("length:", length)

addscore = input("Enter a name and score eg. ('lauren', 4):\n")
new_length = length+1

with open('high.dat', 'ab') as f:
  pickle.dump(addscore, f)
with open('length.dat', 'wb') as f:
  pickle.dump(new_length, f)

# see if it worked

print("updated high file:")

with open('high.dat', 'rb') as f:
  new_new_scores = [pickle.load(f) for i in range(new_length)]

print(new_new_scores)