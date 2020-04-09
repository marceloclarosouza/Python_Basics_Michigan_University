#Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners. 
winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.sort()
z_winners = winners[::-1]
print(z_winners)
