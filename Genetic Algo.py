import random

CHROM_SIZE = 4 #Defines the size of the chromosome.
Pop_SIZE = 2 #Defines the size of the population.
Target_chromosome = [1, 0, 1, 1] #Target chromosome


# This function creates a random chromosome of the specified size, with each gene being either 0 or 1.
def create_chrom():
    chro = []
    for i in range(CHROM_SIZE):
        rand = random.random()
        if rand< 0.5:
            chro.append(1)
        else:
            chro.append(0)
            
    return chro


# This function creates a population of random chromosomes.
def crt_POP():
    pop = []
    for i in range(Pop_SIZE):
        pop.append(create_chrom())
    return pop



# This function calculates the fitness of a chromosome by summing its genes.
def fit_chrom(chrom):
    return sum(chrom)


# This function calculates the fitness of each chromosome in the population.
def fit_Pop(Pop):
    pop_fit = []
    for i in Pop:
        fitness = fit_chrom(i)
        pop_fit.append((i, fitness))
    return pop_fit

# A helper function used for sorting chromosomes based on fitness.
def my(x):
    return x[1]

# Selects the fittest chromosomes from the population based on their fitness values.
def selection(pop):
    a = sorted(pop,key=my,reverse=True)
    return a[:4]

# Performs crossover between selected chromosomes to generate new offspring.
def crosver(Pop):
    nePop = []
    split = 1
    for i in range(0, len(Pop), 2):
        p1, p2 = Pop[i][0], Pop[i+1][0]
        c1 = p1[:split] + p2[split:]
        c2 = p2[:split] + p1[split:]
        nePop.append(c1)
        nePop.append(c2)
        
    return nePop

# Mutates chromosomes by flipping a randomly selected gene.
def mutation(chro):
    
        #print('*'*40)
        #print(i)
        ind = random.randint(0,3)
        #print(ind)
        if chro[ind] == 0:
            chro[ind] = 1
        else:
            chro[ind] = 0
        #print(chro)
        #print('*'*40)
        
        
        return tuple(chro)
        #print('----------------------')


Gen = 1000 # Generations
target_found = False  # Flag to track if the target chromosome is found
for a in range(Gen):
    if a == 0:
        print('Generation no', a+1)
        print("Population of the generation ", a+1)
        population = crt_POP()
        print(population)
    else:
        print('Generation no', a+1)
        print("Population of the generation ", a+1)
        population = mut_pop
        print(population)
    for i in population:
        if i == Target_chromosome:
            print("Target found", i)
            target_found = True
            break  # Break out of the inner loop if target is found
    if target_found:
        print("Target chromosome found. Exiting the loop.")
        break  # Break out of the outer loop if target is found
    
    pop_fit = fit_Pop(population)
    print("Population with fitness of generation ", a+1)
    print(pop_fit)
    print("Selected population of the generation ", a+1)
    sel_pop = selection(pop_fit)
    print(sel_pop)
    print("New population after crossover:")
    new_pop = crosver(sel_pop)
    print(new_pop)
    mut_pop = []
    for i in range(len(new_pop)):
        a=new_pop.pop(0)
        mut_pop.append(list(mutation(a)))
    print("Population after mutation:")
    print(mut_pop)
    
    print(127*"*")
    print()