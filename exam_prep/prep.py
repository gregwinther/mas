from random import shuffle
import sys

question_list = [
    "0.1: Could you describe an agent?",
    "0.2: What is a multiagent system?",
    "0.3: How would you define swarm intelligence?",
    "0.4: What is stigmergy?",
    "0.5: What do we mean by emergence in SI?",
    "1.1: Could you classify the different types of game theory?",
    "1.2: Explain what we mean by self-interested agents",
    "1.3: How do we model utility?\n"
    + " a) Name a few properties of the preference orderings\n"
    + " b) Discuss the relation between utility and money",
    "1.4: What do we mean by strategic interaction?",
    "1.5: Could you name a few solution concepts for solving a 2x2 game on strategic form?",
    "1.6: Could you explain the Prisoner’s Dilemma?\n"
    + " a) Why is it a dilemma?\n"
    + " b) Name a few important real-world PDs",
    "1.7: How does repeating the PD game affect the outcome?",
    "1.8: What do we mean by competitive games and zero-sum games?",
    "2.1: Explain what we mean by social choice theory",
    "2.2: Explain Plurality voting, its strengths and weaknesses",
    "2.3: Explain Simple majority voting, its strengths and weaknesses",
    "2.4: Explain Sequential majority election, its strengths and weaknesses",
    "2.5: Explain the Borda count",
    "2.6: Explain the Slater rule",
    "2.7: Explain dictatorship",
    "2.8: What does Arrow’s theorem say?",
    "2.9: Explain the majority graph\n"
    + " a) What is a possible winner?\n"
    + " b) What is a Condorcet winner?",
    "2.10: What is Condorcet’s paradox?",
    "2.11: What do we mean by tactical voting and strategic manipulation?",
    "2.12: Could you give an interpretation of the Gibbard-Satterthwaite theorem?",
    "2.13: Why could the Second-order Copeland be an advantageous election scheme in terms of strategic manipulation?",
    "3.1: Classify the different types of game theory",
    "3.2: Explain what we mean by cooperative game theory, especially in relation to non- cooperative game theory",
    "3.3: Describe and explain the formal description of a cooperative game",
    "3.4: What is the core?",
    "3.5: In relation to cooperative games, what is the Shapley value?",
    "3.6: Explain marginal contribution net",
    "3.7: What are simple games?",
    "3.8: What are weighted voting games?",
    "3.9: What is coalitional structure formation?",
    "4.1: What are auctions?\n"
    + " a) In what way are auctions thought to be efficient?\n"
    + " b) What two main types of auctions are there?",
    "4.2: Explain the English auction and motivate optimal strategy",
    "4.3: Explain the Dutch auction",
    "4.4: Explain the first-price, sealed-bid auction and motivate optimal strategy",
    "4.5: Explain the Vickrey auction and motivate optimal strategy",
    "4.6: What is winner’s curse?",
    "4.7: What do we mean by combinatorial auctions?\n"
    + " a) How do we solve this combinatorial problem?\n"
    + " b) How do we represent complex bids?",
    "4.8: Explain the VCG-mechanism",
    "5.1: Explain what we mean by bargaining",
    "5.2: What is the conflict deal?",
    "5.3: Explain the alternating offer bargaining model, assuming some simplifying assumptions.",
    "5.4: Explain the ultimatum game\n"
    + " a) What is the Nash equilibrium in one-shot ultimatum?\n"
    + " b) What is the Nash equilibrium in two-shot ultimatum?\n"
    + " c) What is the Nash equilibrium in unlimited round ultimatum?",
    "5.5: What happens when the players get impatient in the ultimatum game?\n"
    + " a) What is the Nash equilibrium in impatient one-shot ultimatum?\n"
    + " b) What is the Nash equilibrium in impatient two-shot ultimatum?\n"
    + " c) What is the Nash equilibrium in impatient unlimited round ultimatum?",
    "5.6: Explain the negotiation decision function as shown in the figure 15.3",
    "5.7: Explain the bargaining for task allocation in relation to figure 15.4\n"
    + " a) Describe the monotonic concession protocol\n"
    + " b) Describe the Zeuthen strategy",
    "5.8: What is the basis for many-to-many negotiations of exchanging already endowed goods?",
    "6.1: What is arguing?",
    "6.2: What different modes of arguing exist?",
    "6.3: What types of argumentation system exist?",
    "6.4: Could you explain a Dung style argumentation system?",
    "6.5: Which arguments to accept in a Dung style argumentation system?",
    "6.6: Which arguments to choose if multiple preferred extensions?",
    "6.7: Could you describe deductive argumentation?\n"
    + " a) What is a rebuttal and an undercut?",
    "7.1: Explain the binary bridge experiment",
    "7.2: Explain the Ant Colony Optimization metaheuristic algorithm\n"
    + " a) What type of problems are ACO especially applicable to? Could you name one?",
    "7.3: Explain the pheromone update rule in AS",
    "7.4: Explain the transition rule (the probability of going to node j) in AS",
    "7.5: Explain the Canonical Particle Swarm Optimization metaheuristic algorithm\n"
    + " a) What type of problems are PSO especially applicable to?",
    "7.6: What is taxis?\n"
    + " a) Could you explain how taxis could be an inspiration for swarm robotics?",
    "7.7: What is Artificial Potential Field?",
    "8.1: Could you explain the inspiration behind response thresholds in task allocation?",
    "8.2: How do we model response thresholds in task allocation?",
    "8.3: Could you describe and explain the stimulus dynamics (assuming one task)?",
    "8.4: Could you describe and explain the transition probabilities (assuming one task)?",
    "8.5: How would you alter this transition dynamics (continuous-time) to allow for more than one task?",
    "8.6: How would you alter this transition dynamics (continuous-time) to account for specialization through learning?",
    "9.1: What is swarm robotics?",
    "9.2: Could you characterize swarm performance as a function of robots?\n"
    + "a) What processes affect performance in the inference region?\n"
    + "b) Could you model this general swarm performance?",
    "9.3: Could you explain swarm modelling as a series of mappings?",
    "9.4: When is it appropriate to use rate equations for modelling swarm dynamics?",
    "9.5: Could you explain the Langevin equation?",
    "9.6: Could you explain the Fokker-Planck equation?",
    "10.1: Could you explain the voter model for decision-making in a swarm system?",
    "10.2: Could you explain the majority rule?",
    "10.3: Could you explain how urn models function?",
    "10.4: Could you explain the Hegselmann and Krause decision-making model?",
    "10.5: We want to find the warmest, lightest or most radioactive spot in a search area. Could you name a few types of models for solving this problem?",
    "10.6: Could you sketch the Beeclust algorithm?",
    "10.7: Could you explain the Langevin equation in relation to the Beeclust algorithm?",
    "10.8: Could you explain the Fokker-Planck equation in relation to the Beeclust algorithm?",
]

# Sanity check.
# for question in question_list:
#     print(question)
# 
# vat

shuffle(question_list)

i = 0
n = len(question_list)

instruction_string = "1: Next question\n" + "0: Quit\n"

def next_question():
    global i
    if i >= n:
        print("Thats all folks!")
        print("Goodbye!")
        sys.exit()
    print(question_list[i])
    i += 1

def input_handler():
    print(f"{n-i} questions left.")
    arg = input(instruction_string)
    try: 
        arg = int(arg)
    except:
        print("Invalid argument.")
        input_handler()
    if int(arg) == 1:
        print()
        next_question()
        print()
        input_handler()
    if int(arg) == 0:
        print("Goodbye!")
        sys.exit() 
    else:
        print("Invalid argument.")
        input_handler()

if __name__ == "__main__":
    input_handler()
