#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

class GameState:

  def __init__(self):
    self.player = {
      "hp": 50,
      "mana": 500,
      "def": 0
    }

    self.boss = {
      "hp": 71,
      "atk": 10
    }

    self.shield_timer = 0
    self.poison_timer = 0
    self.recharge_timer = 0
    self.mana_used = 0
    self.previous_moves = []

  # spells
  def magic_missile(self):
    self.previous_moves.append("magic_missile")
    self.player["mana"] -= 53
    self.mana_used += 53
    self.boss["hp"] -= 4

  def drain(self):
    self.previous_moves.append("drain")
    self.player["mana"] -= 73
    self.mana_used += 73
    self.boss["hp"] -= 2
    self.player["hp"] += 2

  def shield(self):
    self.previous_moves.append("shield")
    self.player["mana"] -= 113
    self.mana_used += 113
    self.shield_timer = 6

  def poison(self):
    self.previous_moves.append("poison")
    self.player["mana"] -= 173
    self.mana_used += 173
    self.poison_timer = 6

  def recharge(self):
    self.previous_moves.append("recharge")
    self.player["mana"] -= 229
    self.mana_used += 229
    self.recharge_timer = 5

  spells = {
    "shield": shield,
    "poison": poison,
    "recharge": recharge,
    "magic_missile": magic_missile,
    "drain": drain,
  }

  def cast_spell(self, spell):
    self.spells[spell](self)

  # effects
  def shield_effect(self):
    if self.shield_timer > 0:
      self.player["def"] = 7
      self.shield_timer -= 1
    else:
      self.player["def"] = 0

  def poison_effect(self):
    if self.poison_timer > 0:
      self.boss["hp"] -= 3
      self.poison_timer -= 1

  def recharge_effect(self):
    if self.recharge_timer > 0:
      self.player["mana"] += 101
      self.recharge_timer -= 1

  def resolve_effects(self):
    self.shield_effect()
    self.poison_effect()
    self.recharge_effect()

  # boss
  def boss_attack(self):
    self.player["hp"] -= (10 - self.player["def"])

  # checks
  def skip_branch(self, spell):
    if len(self.previous_moves) == 6 and "recharge" not in self.previous_moves:
      return True
    else:
      return False 

  def lost(self):
    if self.player["hp"] <= 0 or self.player["mana"] <= 0:
      # print self.previous_moves
      return True
    else:
      return False

  def won(self):
    if self.player["hp"] > 0 and self.player["mana"] > 0 and self.boss["hp"] <= 0:
      return True
    else:
      return False

best_mana_usage = 1000000
wins = 0
losses = 0
prunes = 0
def simulate_turn(game_state, spell_to_cast):
  global best_mana_usage, wins, losses, prunes
  # print game_state.previous_moves
  # hard mode
  game_state.player["hp"] -= 1
  if game_state.lost():
    losses += 1
    return
  # Check if this branch is worth following
  if game_state.mana_used >= best_mana_usage:
    prunes += 1
    return
  # Do the player turn and check if we won
  game_state.resolve_effects()
  if game_state.won():
    # Check mana used against current best
    wins += 1
    print "Won!"
    print game_state.previous_moves
    print game_state.mana_used
    if game_state.mana_used < best_mana_usage:
      best_mana_usage = game_state.mana_used
      return
  game_state.cast_spell(spell_to_cast)
  if game_state.lost():
    # print "Lost."
    losses += 1
    return
  if game_state.won():
    wins += 1
    # Check mana used against current best
    if game_state.mana_used < best_mana_usage:
      best_mana_usage = game_state.mana_used
      print game_state.previous_moves
      print best_mana_usage
    return
  # Do the enemy turn (if required)
  game_state.resolve_effects()
  if game_state.won():
    # Check mana used against current best
    wins += 1
    print "Won!"
    print game_state.previous_moves
    print game_state.mana_used
    if game_state.mana_used < best_mana_usage:
      best_mana_usage = game_state.mana_used
      return
  game_state.boss_attack()
  if game_state.lost():
    losses += 1
    # print "Lost."
    return
  if game_state.won():
    # Check mana used against current best
    wins += 1
    print "Won!"
    print game_state.previous_moves
    print game_state.mana_used
    if game_state.mana_used < best_mana_usage:
      best_mana_usage = game_state.mana_used
      return
  # If we are here, the game is not yet won or lost
  # Cycle possible next turns with recursion
  for spell in game_state.spells.keys():
    if game_state.shield_timer > 1 and spell == "shield":
      continue
    if game_state.poison_timer > 1 and spell == "poison":
      continue
    if game_state.recharge_timer > 1 and spell == "recharge":
      continue
    simulate_turn(copy.deepcopy(game_state), spell)

def simulate_turn_iter(spells):
  game_state = GameState()
  for spell in spells:
    # Do the player turn and check if we won
    game_state.player["hp"] -= 1
    game_state.resolve_effects()
    game_state.cast_spell(spell)

    print spell
    print game_state.player
    print game_state.boss
    print game_state.shield_timer
    print game_state.poison_timer
    print game_state.recharge_timer

    # Do the enemy turn (if required)
    game_state.resolve_effects()
    game_state.boss_attack()

    print "attack"
    print game_state.player
    print game_state.boss
    print game_state.shield_timer
    print game_state.poison_timer
    print game_state.recharge_timer

game_state = GameState()
for spell in game_state.spells.keys():
  simulate_turn(copy.deepcopy(game_state), spell)

print wins
print losses
print prunes
print best_mana_usage

# # plan = ['magic_missile', 'shield', 'recharge', 'drain', 'magic_missile', 'recharge', 'shield', 'magic_missile', 'poison', 'recharge']
# plan = ['shield', 'recharge', 'poison', 'shield', 'recharge', 'poison', 'shield', 'recharge', 'poison', 'shield', 'magic_missile', 'poison', 'magic_missile']

# simulate_turn_iter(plan)