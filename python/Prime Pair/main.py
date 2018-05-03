import operator

def is_prime(num):
	if num == 1:
		return True
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	for i in range(3, int(num**0.5) + 1, 2):
		if num % i == 0:
			return False
	return True

def get_next_prime(num):
	i = num + 1
	while(not is_prime(i)):
		i = i + 1
	return i

def print_prime_pair_stat(prime_pair):
	for i in sorted(prime_pair):
		for j in sorted(prime_pair[i]):
			print i, j, ' = ', prime_pair[i][j]

def get_last_digit(num):
	return num % 10

def add_tally(prime_pair, i, j):
	if i == 0 or j == 0:
		return
	i = get_last_digit(i)
	j = get_last_digit(j)
	if i not in prime_pair:
		prime_pair[i] = {}
		if j not in prime_pair[i]:
			prime_pair[i][j] = 1
			return
	elif j not in prime_pair[i]:
		prime_pair[i][j] = 1
	else:
		prime_pair[i][j] = prime_pair[i][j] + 1

def get_prob(prime_pair):
	new_prime = {}
	for i in prime_pair:
		new_prime[i] = {}
		sum = 0
		for j in prime_pair[i]:
			sum = sum + prime_pair[i][j]
		for j in prime_pair[i]:
			new_prime[i][j] = (float(prime_pair[i][j]) / sum) * 100
	return new_prime

def get_prob(prime_pair, max_prime):
	new_prime = {}
	for i in prime_pair:
		new_prime[i] = {}
		for j in prime_pair[i]:
			new_prime[i][j] = (float(prime_pair[i][j]) / max_prime) * 100
	return new_prime

def flat_prime_pair(prime_pair):
	new_pair = {}
	for i in prime_pair:
		for j in prime_pair[i]:
			s = str(i) + ' -> ' + str(j)
			new_pair[s] = prime_pair[i][j]
	return new_pair

def print_sorted_values(prime_pair):
	flat_pair = flat_prime_pair(prime_pair)
	sorted_pair = reversed(sorted(flat_pair.items(), key=operator.itemgetter(1)))
	for i in sorted_pair:
		print '%s = %-3.2f %%' % (i[0], i[1])

if __name__ == '__main__':
	prime_pair = {}
	MAX_PRIME = 100000
	INTERVAL = MAX_PRIME / 100
	percent = 0
	prev_prime = 0
	curr_prime = 1
	num_prime = 0
	with open('list prime.txt', 'r+') as f:
		line_list = f.readlines()
		num_prime = len(line_list)
		if line_list:
			for (first, second) in zip(line_list[:-1], line_list[1:]):
				i = int(first.strip('\n\t\r '))
				j = int(second.strip('\n\t\r '))
				add_tally(prime_pair, i, j)
			s = line_list[-1]
			prev_prime = int(s.strip('\n\r '))
			print 'last prime in file:', prev_prime
		for count in range(MAX_PRIME):
			curr_prime = get_next_prime(prev_prime)
			add_tally(prime_pair, prev_prime, curr_prime)
			f.write('%s\n' % curr_prime)
			prev_prime = curr_prime
			if count % INTERVAL == 0 and MAX_PRIME > INTERVAL:
				print percent, '% :', curr_prime
				percent = percent + 1
			elif MAX_PRIME < INTERVAL:
				print count, ':', curr_prime

	if MAX_PRIME > INTERVAL:
		print MAX_PRIME, ':', curr_prime
	num_prime = num_prime + MAX_PRIME

	print_prime_pair_stat(prime_pair)
	prob_pair = get_prob(prime_pair, num_prime - 1)
	print
	print_prime_pair_stat(prob_pair)
	print
	print_sorted_values(prob_pair)
	print
	print 'number of pairs:', num_prime - 1