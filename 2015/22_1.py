#!/usr/local/bin/python
import sys
import math
import re
import operator
import copy

class GameManager:

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
    self.mana_costs = {
      "magic_missile": 53,
      "drain": 73,
      "shield": 113,
      "poison": 173,
      "recharge": 229
    }

    self.mana_used = 0
    self.action_log = []
    self.home_stretch = False
  # spells
  def magic_missile(self):
    print "Magic Missile!"
    self.action_log.append("magic missile")
    self.player["mana"] -= self.mana_costs["magic_missile"]
    self.mana_used += self.mana_costs["magic_missile"]
    self.boss["hp"] -= 4

  def drain(self):
    print "Drain!"
    self.action_log.append("drain")
    self.player["mana"] -= self.mana_costs["drain"]
    self.mana_used += self.mana_costs["drain"]
    self.boss["hp"] -= 2
    self.player["hp"] += 2

  def shield(self):
    print "Shield!"
    self.action_log.append("shield")
    self.player["mana"] -= self.mana_costs["shield"]
    self.mana_used += self.mana_costs["shield"]
    self.shield_timer = 6

  def poison(self):
    print "Poison!"
    self.action_log.append("poison")
    self.player["mana"] -= self.mana_costs["poison"]
    self.mana_used += self.mana_costs["poison"]
    self.poison_timer = 6

  def recharge(self):
    print "Recharge!"
    self.action_log.append("recharge")
    self.player["mana"] -= self.mana_costs["recharge"]
    self.mana_used += self.mana_costs["recharge"]
    self.recharge_timer = 5

  # effects
  def shield_effect(self):
    if self.shield_timer == 0:
      self.player["def"] = 0
    if self.shield_timer > 0:
      print "Shield Active"
      self.player["def"] = 7
      self.shield_timer -= 1
      print "Shield Timer: "+str(self.shield_timer)

  def poison_effect(self):
    if self.poison_timer > 0:
      print "Poison Active"
      self.boss["hp"] -= 3
      self.poison_timer -= 1
      print "Poison Timer: "+str(self.poison_timer)

  def recharge_effect(self):
    if self.recharge_timer > 0:
      print "Recharge Active"
      self.player["mana"] += 101
      self.recharge_timer -= 1
      print "Recharge Timer: "+str(self.recharge_timer)

  # boss
  def attack(self):
    print "Attack!"
    self.player["hp"] -= (self.boss["atk"] - self.player["def"])

  # AI
  # Best so far mana used: 2166
  def player_action(self, actual_turn):
    # If at this point we have enough hp and mana to last to the end,
    # just magic missile until we win
    turns_to_win = math.ceil(self.boss["hp"] / 4.0)
    virtual_hp = self.player["hp"]
    virtual_shield = self.shield_timer
    virtual_mana = self.player["mana"]
    for turn in range(turns_to_win):
      virtual_def = 0
      if virtual_shield > 0:
        virtual_shield -= 1
        virtual_def = 7
      virtual_hp = virtual_hp - (self.boss["atk"] - virtual_def)
      virtual_mana -= self.mana_costs["magic_missile"]
    if actual_turn == 25:
      self.shield()
    elif actual_turn > 22:
      self.magic_missile()
    elif virtual_hp > 0 and virtual_mana > 0:
      self.magic_missile()
    elif self.boss["hp"] <= 4 and \
         self.player["mana"] >= self.mana_costs["magic_missile"]:
      self.magic_missile()
    elif self.player["hp"] <= self.boss["atk"] and \
         self.player["mana"] >= self.mana_costs["drain"]:
      self.drain()
    elif self.shield_timer == 0 and \
         self.player["mana"] >= self.mana_costs["shield"]:
      self.shield()
    elif self.recharge_timer == 0 and \
         self.player["mana"] >= self.mana_costs["recharge"]:
      self.recharge()
    elif self.poison_timer == 0 and \
         self.player["mana"] >= self.mana_costs["poison"]:
      self.poison()
    else:
      self.magic_missile()

  def boss_action(self):
    self.attack()

  # Main loop
  def main(self):
    players_turn = True
    turn = 0
    while self.player["hp"] > 0 and self.boss["hp"] > 0 and self.player["mana"] > 0:
      turn += 1
      print "*** Turn "+str(turn)+" ***"
      print "--- Effects ---"
      self.shield_effect()
      self.poison_effect()
      self.recharge_effect()
      if players_turn:
        print "--- Player's Turn ---"
        self.player_action(turn)
      else:
        print "--- Boss's Turn ---"
        self.boss_action()
      players_turn = not players_turn
      print "Player Status:"
      print self.player
      print "Boss Status:"
      print self.boss
      print "Mana used: "+str(self.mana_used)
      print ' '

    if self.player["hp"] <= 0 or self.player["mana"] <= 0:
      print "You lose."
    else:
      print "You win."
    print "Mana used: "+str(self.mana_used)
    for action in self.action_log:
      print action

game = GameManager()
game.main()