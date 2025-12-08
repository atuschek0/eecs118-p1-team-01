# valueIterationAgents.py
# -----------------------
# Based on valueIterationAgents.py from the UC Berkeley Pacman AI Projects.
# Original authors: John DeNero, Dan Klein, Brad Miller, Nick Hay, Pieter Abbeel.
# Original project link: http://ai.berkeley.edu
#
# Modifications for UCI EECS 118 by Mahmoud Elfar, 2025.
# This version includes Catman's detailed comments for educational purposes.
#
# Licensing: You may use or extend this file for educational purposes
# provided that (1) solutions are not distributed or published,
# (2) this notice is retained, and (3) clear attribution to UC Berkeley is kept.
#--------------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp: mdp.MarkovDecisionProcess, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        """
          Run the value iteration algorithm. Note that in standard
          value iteration, V_k+1(...) depends on V_k(...)'s.
        """
        # util.raiseNotDefined()
        #------------------------------------------
        # Catman here for the rescue! Some hints:
        # You will need to loop for the number of iterations specified.
        # In each iteration, you will need to update the value of each state
        # based on the Bellman equation:
        # V(s) = max_a Q(s,a)
        # where Q(s,a) is computed as:
        # Q(s,a) = sum_{s'} P(s'|s,a) * [R(s,a,s') + gamma * V(s')]
        # You can use mdp.getStates() to get all states,
        # mdp.getPossibleActions(state) to get possible actions,
        # mdp.getTransitionStatesAndProbs(state, action) to get next states and their probabilities,
        # and mdp.getReward(state, action, nextState) to get the reward.
        # Remember to use a temporary copy of the values to update
        # all states simultaneously. Otherwise, you will be using updated values
        # in the same iteration, which is not correct.
        # Catman out!
        #------------------------------------------
        # Catman here! Here is the summary of the steps to follow:
        # 1. Loop for the number of iterations (given by self.iterations).
        # 2. In each iteration, create a temporary copy of the current values (self.values).
        # 3. For each state in the MDP (use self.mdp.getStates()):
        #    a. If the state is terminal (use self.mdp.isTerminal(state)), skip to the next state.
        #    b. Otherwise, for each possible action in that state (use self.mdp.getPossibleActions(state)):
        #       i. Compute the Q-value for that state-action pair (call self.computeQValueFromValues(state, action)).
        #    c. Update the temporary values for that state to be the maximum Q-value computed.
        # 4. After processing all states, update self.values to be the temporary values.
        # Catman out!
        #------------------------------------------
        for _ in range(self.iterations):
            # Starting from fresh container so all updates based on previous iteration
            new_values = util.Counter()

            for state in self.mdp.getStates():
                # Terminal states keep (or default to) 0
                if self.mdp.isTerminal(state):
                    new_values[state] = self.values[state]
                    continue

                actions = self.mdp.getPossibleActions(state)
                if not actions:
                    # No legal actions; treat them terminal-ish
                    new_values[state] = self.values[state]
                    continue

                # Computing all Q(s, a) using OLD values, then taking max_a
                q_values = [
                    self.computeQValueFromValues(state, action)
                    for action in actions
                ]
                new_values[state] = max(q_values)

            # Committing entire sweep
            self.values = new_values
        #------------------------------------------

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action: str) -> float:
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        # util.raiseNotDefined()
        #------------------------------------------
        # Catman here for the rescue! Some hints:
        # To compute the Q-value of the given state-action pair,
        # you need three things from the MDP:
        # 1. List of possible next states
        # 2. The transition probabilities to those next states
        # 3. The rewards for those transitions
        # Use mdp.getTransitionStatesAndProbs(state, action) to get
        # the list of (nextState, prob) pairs.
        # Then, for each nextState, get the reward using
        # mdp.getReward(state, action, nextState).
        # Finally, use the Bellman equation to compute the Q-value:
        # Q(s,a) = sum_{s'} P(s'|s,a) * [R(s,a,s') + gamma * V(s')]
        # where P(s'|s,a) is the transition probability,
        # R(s,a,s') is the reward, gamma is the discount factor,
        # and V(s') is the value of the next state.
        # Catman out!
        #------------------------------------------
        # Catman here! Here are the summary of the steps to follow:
        # 1. Initialize Q-value to 0.
        # 2. Get the list of (nextState, prob) pairs using mdp.getTransitionStatesAndProbs(state, action).
        # 3. For each (nextState, prob) pair:
        #    a. Get the reward for the transition using mdp.getReward(state, action, nextState).
        #    b. Get the value of the next state using self.values[nextState].
        #    c. Update the Q-value using the Bellman equation.
        # 4. Return the computed Q-value.
        # Catman out!
        #------------------------------------------
        q_value = 0.0

        transitions = self.mdp.getTransitionStatesAndProbs(state, action)
        for next_state, prob in transitions:
            if prob == 0:
                continue # skipping impossible branch

            reward = self.mdp.getReward(state, action, next_state)

            # Bellman
            future = self.values[next_state]
            q_value += prob * (reward + self.discount * future)

        return q_value
        #------------------------------------------

    def computeActionFromValues(self, state: str) -> str:
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        # util.raiseNotDefined()
        #------------------------------------------
        # Catman here for the rescue! Some hints:
        # First, make sure there are legal actions available for this state.
        # How? Use mdp.getPossibleActions(state), it returns a list of actions.
        # Then, for each action, compute its Q-value using computeQValueFromValues.
        # Finally, return the action with the highest Q-value.
        # Catman out!
        #------------------------------------------
        # Catman here! Here are the summary of the steps to follow:
        # 1. Get possible actions for the state.
        # 2. If no actions, return None.
        # 3. For each action, compute Q-value of the state-action pair (state is given as input).
        # 4. Find the action with the maximum Q-value (i.e., the action with the highest quality).
        # 5. Return that action.
        # Catman out!
        #------------------------------------------
        actions = self.mdp.getPossibleActions(state)
        if not actions:
            # No legal actions (terminal state)
            return None

        # Building list of (action, Q-value) pair, then picking the best.
        best_action = None
        best_value = float('-inf')

        for action in actions:
            q_val = self.computeQValueFromValues(state, action)
            # Strict > so that first max encoutered is kept on ties
            if q_val > best_value:
                best_value = q_val
                best_action = action
        return best_action
        #------------------------------------------

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
