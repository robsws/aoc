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

  # spells
  def magic_missile(self):
    self.player["mana"] -= 53
    self.mana_used += 53
    self.boss["hp"] -= 4

  def drain(self):
    self.player["mana"] -= 73
    self.mana_used += 73
    self.boss["hp"] -= 2
    self.player["hp"] += 2

  def shield(self):
    self.player["mana"] -= 113
    self.mana_used += 113
    self.shield_timer = 6

  def poison(self):
    self.player["mana"] -= 173
    self.mana_used += 173
    self.poison_timer = 6

  def recharge(self):
    self.player["mana"] -= 229
    self.mana_used += 229
    self.recharge_timer = 5

  spells = {
    "magic_missile": magic_missile,
    "drain": drain,
    "shield": shield,
    "poison": poison,
    "recharge": recharge
  }

  def cast_spell(self, spell):
    self.spells[spell]()

  # effects
  def shield_effect(self):
    if self.shield_timer > 0
      self.player["def"] = 7
    self.shield_timer -= 1

  def poison_effect(self):
    if self.poison_timer > 0
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
    self.player["hp"] -= 10

  # checks
  def lost(self):
    if self.player["hp"] <= 0 or self.player["mana"] < 53:
      return True
    else:
      return False

  def won(self):
    if self.player["hp"] > 0 and self.player["mana"] > 0 and self.boss["hp"] <= 0:
      return True
    else:
      return False

best_mana_usage = 100000
def simulate_turn(game_state, spell_to_cast):
  global best_mana_usage
  # Do the player turn and check if we won
  game_state.resolve_effects()
  game_state.cast_spell(spell_to_cast)
  if game_state.won():
    # Check mana used against current best
    if game_state.mana_used < best_mana_usage:
      best_mana_usage = game_state.mana_used
      return
  # Do the enemy turn (if required)
  game_state.resolve_effects()
  game_state.boss_attack()
  if game_state.lost():
    return
  if game_state.won():
    # Check mana used against current best
    if game_state.mana_used < best_mana_usage:
      best_mana_usage = game_state.mana_used
      return
  # If we are here, the game is not yet won or lost
  # Cycle possible next turns with recursion
  for spell in game_state.spells.keys():
    simulate_turn(copy.deepcopy(game_state), spell)

game_state = GameState()
for spell in game_state.spells.keys():
  simulate_turn(copy.deepcopy(game_state), spell)